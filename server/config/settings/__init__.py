# -*- coding: utf-8 -*-
import environ

ROOT_DIR = environ.Path(__file__) - 3  # server/
""":type: environ.Path"""
APPS_DIR = ROOT_DIR.path('annotation_tool')

env = environ.Env()
