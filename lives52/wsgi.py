"""
WSGI config for lives52 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

# Python 2 threading problems
if sys.version_info < (3,):
    import _strptime  # noqa

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# New Relic
if os.environ.get('NEW_RELIC_LICENSE_KEY') is not None:
    import newrelic.agent
    newrelic.agent.initialize()
    application = newrelic.agent.WSGIApplicationWrapper(application)
