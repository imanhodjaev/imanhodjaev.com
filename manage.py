#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'imanhodjaev'))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imanhodjaev.settings")

    execute_from_command_line(sys.argv)
