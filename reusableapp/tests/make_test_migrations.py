import os
import sys

import django

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    django.setup()
    from django.core.management import execute_from_command_line
    args = sys.argv + ['makemigrations', 'tests']
    execute_from_command_line(args)
