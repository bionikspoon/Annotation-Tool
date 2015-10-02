# -*- coding: utf-8 -*-
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
""":type: environ.Path"""
APPS_DIR = ROOT_DIR.path('annotation_tool')

env = environ.Env()
