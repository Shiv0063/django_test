"""
WSGI config for error_page project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
import sys

# assuming your Django settings file is at
# '/home/myusername/mysite/mysite/settings.py'
path = '/error_page'
if path not in sys.path:
     sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'error_page.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()