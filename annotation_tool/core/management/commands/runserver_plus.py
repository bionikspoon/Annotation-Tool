"""
Override runserver_plus to add `extra_files` globbing.
"""

import logging
import glob
import itertools
import os
import re
import socket
import sys
import time

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django_extensions.management.commands.runserver_plus import Command as RunServerPlusCommand, \
    set_werkzeug_log_color, DEFAULT_PORT, naiveip_re, HAS_MIGRATIONS, USE_STATICFILES
from django.conf import settings
from django.core.management.base import CommandError
from django.core.exceptions import ImproperlyConfigured
from django_extensions.management.technical_response import null_technical_500_response
from django_extensions.management.utils import RedirectHandler, setup_logger, signalcommand, \
    has_ipdb

logger = logging.getLogger(__name__)


class Command(RunServerPlusCommand):
    """
    Runserver_plus_plus.
    """
    # noinspection PyAttributeOutsideInit,PyPep8Naming,PyDocstring
    @signalcommand
    def handle(self, addrport='', *args, **options):
        import django

        # Do not use default ending='\n', because StreamHandler() takes care of it
        if hasattr(self.stderr, 'ending'):
            self.stderr.ending = None

        setup_logger(logger, self.stderr,
                     filename=options.get('output_file', None))  # , fmt="[%(name)s] %(message)s")
        logredirect = RedirectHandler(__name__)

        # Redirect werkzeug log items
        werklogger = logging.getLogger('werkzeug')
        werklogger.setLevel(logging.INFO)
        werklogger.addHandler(logredirect)
        werklogger.propagate = False

        if options.get("print_sql", False):
            try:
                # Django 1.7 onwards
                from django.db.backends import utils
            except ImportError:
                # Django 1.6 below
                from django.db.backends import util as utils

            try:
                import sqlparse
            except ImportError:
                sqlparse = None  # noqa

            class PrintQueryWrapper(utils.CursorDebugWrapper):
                # noinspection PyDocstring
                def execute(self, sql, params=()):
                    starttime = time.time()
                    try:
                        return self.cursor.execute(sql, params)
                    finally:
                        raw_sql = self.db.ops.last_executed_query(self.cursor, sql, params)
                        execution_time = time.time() - starttime
                        therest = ' -- [Execution time: %.6fs] [Database: %s]' % (
                            execution_time, self.db.alias)
                        if sqlparse:
                            logger.info(sqlparse.format(raw_sql, reindent=True) + therest)
                        else:
                            logger.info(raw_sql + therest)

            utils.CursorDebugWrapper = PrintQueryWrapper

        try:
            # noinspection PyUnresolvedReferences
            from django.core.servers.basehttp import AdminMediaHandler
            USE_ADMINMEDIAHANDLER = True
        except ImportError:
            USE_ADMINMEDIAHANDLER = False

        try:
            from django.core.servers.basehttp import get_internal_wsgi_application as WSGIHandler
        except ImportError:
            from django.core.handlers.wsgi import WSGIHandler  # noqa

        try:
            # noinspection PyUnresolvedReferences
            from werkzeug import run_simple, DebuggedApplication

            # Set colored output
            if settings.DEBUG:
                # noinspection PyBroadException
                try:
                    set_werkzeug_log_color()
                except:  # We are dealing with some internals, anything could go wrong
                    print("Wrapping internal werkzeug logger for color highlighting has failed!")
                    pass

        except ImportError:
            raise CommandError("Werkzeug is required to use runserver_plus.  Please visit "
                               "http://werkzeug.pocoo.org/ or install via pip. (pip install "
                               "Werkzeug)")

        pdb_option = options.get('pdb', False)
        ipdb_option = options.get('ipdb', False)
        pm = options.get('pm', False)
        try:
            # noinspection PyUnresolvedReferences
            from django_pdb.middleware import PdbMiddleware
        except ImportError:
            if pdb_option or ipdb_option or pm:
                raise CommandError(
                    "django-pdb is required for --pdb, --ipdb and --pm options. Please visit "
                    "https://pypi.python.org/pypi/django-pdb or install via pip. (pip install "
                    "django-pdb)")
            pm = False
        else:
            # Add pdb middleware if --pdb is specified or if in DEBUG mode
            middleware = 'django_pdb.middleware.PdbMiddleware'
            debug_option = pdb_option or ipdb_option or settings.DEBUG
            if debug_option and middleware not in settings.MIDDLEWARE_CLASSES:
                settings.MIDDLEWARE_CLASSES += (middleware,)

            # If --pdb is specified then always break at the start of views.
            # Otherwise break only if a 'pdb' query parameter is set in the url
            if pdb_option:
                PdbMiddleware.always_break = 'pdb'
            elif ipdb_option:
                PdbMiddleware.always_break = 'ipdb'

            # noinspection PyDocstring
            def postmortem(_, exc_type, exc_value, tb):
                if has_ipdb():
                    import ipdb
                    p = ipdb
                else:
                    import pdb
                    p = pdb
                print("Exception occured: %s, %s" % (exc_type, exc_value), file=sys.stderr)
                p.post_mortem(tb)

        # usurp django's handler
        from django.views import debug
        # noinspection PyUnboundLocalVariable
        debug.technical_500_response = postmortem if pm else null_technical_500_response

        self.use_ipv6 = options.get('use_ipv6')
        if self.use_ipv6 and not socket.has_ipv6:
            raise CommandError('Your Python does not support IPv6.')
        self._raw_ipv6 = False
        if not addrport:
            try:
                addrport = settings.RUNSERVERPLUS_SERVER_ADDRESS_PORT
            except AttributeError:
                pass
        if not addrport:
            self.addr = ''
            self.port = DEFAULT_PORT
        else:
            m = re.match(naiveip_re, addrport)
            if m is None:
                raise CommandError('"%s" is not a valid port number '
                                   'or address:port pair.' % addrport)
            self.addr, _ipv4, _ipv6, _fqdn, self.port = m.groups()
            if not self.port.isdigit():
                raise CommandError("%r is not a valid port number." % self.port)
            if self.addr:
                if _ipv6:
                    self.addr = self.addr[1:-1]
                    self.use_ipv6 = True
                    self._raw_ipv6 = True
                elif self.use_ipv6 and not _fqdn:
                    raise CommandError('"%s" is not a valid IPv6 address.' % self.addr)
        if not self.addr:
            self.addr = '::1' if self.use_ipv6 else '127.0.0.1'

        threaded = options.get('threaded', True)
        use_reloader = options.get('use_reloader', True)
        open_browser = options.get('open_browser', False)
        cert_path = options.get("cert_path")
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'
        bind_url = "http://%s:%s/" % (
            self.addr if not self._raw_ipv6 else '[%s]' % self.addr, self.port)
        # glob `--extra-file` input
        extra_files = list(set(itertools.chain.from_iterable(
            glob.glob(nested_file) for nested_file in options.get('extra_files', None) or [])))

        reloader_interval = options.get('reloader_interval', 1)

        # noinspection PyDocstring
        def inner_run():
            if extra_files:
                print('Watching extra files:')
                for file in extra_files:
                    print(' * %s' % file)

            print("Performing system checks...\n")
            if hasattr(self, 'check'):
                self.check(display_num_errors=True)
            else:
                self.validate(display_num_errors=True)
            if HAS_MIGRATIONS:
                try:
                    self.check_migrations()
                except ImproperlyConfigured:
                    pass
            print("\nDjango version %s, using settings %r" % (
                django.get_version(), settings.SETTINGS_MODULE))
            print("Development server is running at %s" % (bind_url,))
            print("Using the Werkzeug debugger (http://werkzeug.pocoo.org/)")
            print("Quit the server with %s." % quit_command)
            path = options.get('admin_media_path', '')
            if not path:
                admin_media_path = os.path.join(django.__path__[0], 'contrib/admin/static/admin')
                if os.path.isdir(admin_media_path):
                    path = admin_media_path
                else:
                    path = os.path.join(django.__path__[0], 'contrib/admin/media')
            handler = WSGIHandler()
            if USE_ADMINMEDIAHANDLER:
                handler = AdminMediaHandler(handler, path)
            if USE_STATICFILES:
                use_static_handler = options.get('use_static_handler', True)
                insecure_serving = options.get('insecure_serving', False)
                if use_static_handler and (settings.DEBUG or insecure_serving):
                    handler = StaticFilesHandler(handler)
            if open_browser:
                import webbrowser
                webbrowser.open(bind_url)
            if cert_path:
                """
                OpenSSL is needed for SSL support.

                This will make flakes8 throw warning since OpenSSL is not used
                directly, alas, this is the only way to show meaningful error
                messages. See:
                http://lucumr.pocoo.org/2011/9/21/python-import-blackbox/
                for more information on python imports.
                """
                try:
                    # noinspection PyUnresolvedReferences
                    import OpenSSL  # NOQA
                except ImportError:
                    raise CommandError("Python OpenSSL Library is "
                                       "required to use runserver_plus with ssl support. "
                                       "Install via pip (pip install pyOpenSSL).")
                dir_path, cert_file = os.path.split(cert_path)
                if not dir_path:
                    dir_path = os.getcwd()
                root, ext = os.path.splitext(cert_file)
                certfile = os.path.join(dir_path, root + ".crt")
                keyfile = os.path.join(dir_path, root + ".key")
                try:
                    # noinspection PyUnresolvedReferences
                    from werkzeug.serving import make_ssl_devcert
                    if os.path.exists(certfile) and os.path.exists(keyfile):
                        ssl_context = (certfile, keyfile)
                    else:  # Create cert, key files ourselves.
                        ssl_context = make_ssl_devcert(os.path.join(dir_path, root),
                                                       host='localhost')
                except ImportError:
                    print("Werkzeug version is less than 0.9, trying adhoc certificate.")
                    ssl_context = "adhoc"

            else:
                ssl_context = None

            if use_reloader and settings.USE_I18N:
                try:
                    # noinspection PyUnresolvedReferences
                    from django.utils.autoreload import gen_filenames
                except ImportError:
                    pass
                else:
                    extra_files.extend(
                        filter(lambda filename: filename.endswith('.mo'), gen_filenames()))

            run_simple(self.addr, int(self.port), DebuggedApplication(handler, True),
                       use_reloader=use_reloader, use_debugger=True, extra_files=extra_files,
                       reloader_interval=reloader_interval, threaded=threaded,
                       ssl_context=ssl_context, )

        inner_run()
