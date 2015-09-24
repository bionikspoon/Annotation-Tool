#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import os
import re
import warnings
from environ import environ
import sys

import logging

if sys.version < '3':
    # noinspection PyUnresolvedReferences
    text_type = unicode
else:
    text_type = str
    basestring = str
logger = logging.getLogger(__name__)


class Env(environ.Env):
    @staticmethod
    def read_env(env_file=None, **overrides):

        if env_file is None:
            frame = sys._getframe()
            env_file = os.path.join(os.path.dirname(frame.f_back.f_code.co_filename), '.env')
            if not os.path.exists(env_file):
                warnings.warn("not reading %s - it doesn't exist." % env_file)
                return

        try:
            with open(env_file) if isinstance(env_file, basestring) else env_file as f:
                content = f.read()
        except IOError:
            warnings.warn("not reading %s - it doesn't exist." % env_file)
            return

        logger.debug('Read environment variables from: {0}'.format(env_file))

        for line in content.splitlines():
            m1 = re.match(r'\A([A-Za-z_0-9]+) ?= ?(.*)\Z', line)
            if m1:
                key, val = m1.group(1), m1.group(2)
                m2 = re.match(r"\A'(.*)'\Z", val)
                if m2:
                    val = m2.group(1)
                m3 = re.match(r'\A"(.*)"\Z', val)
                if m3:
                    val = re.sub(r'\\(.)', r'\1', m3.group(1))
                os.environ.setdefault(key, text_type(val))

        # set defaults
        for key, value in overrides.items():
            os.environ.setdefault(key, value)
