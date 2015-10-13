# -*- coding: utf-8 -*-
import environ
import warnings

ROOT_DIR = environ.Path(__file__) - 3  # server/
""":type: environ.Path"""
APPS_DIR = ROOT_DIR.path('annotation_tool')

env = environ.Env()

warnings.filterwarnings("ignore", category=RuntimeWarning, module='django.db.backends.sqlite3.base', lineno=57)
