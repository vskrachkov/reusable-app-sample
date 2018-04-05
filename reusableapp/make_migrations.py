import os
import sys

import django

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "myapp"]
    execute_from_command_line(args)
