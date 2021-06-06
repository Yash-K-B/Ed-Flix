import os
import sys

# assuming your django settings file is at '/home/edflix5/mysite/mysite/settings.py'
# and your manage.py is is at '/home/edflix5/mysite/manage.py'
path = '/home/edflix5/Ed-Flix'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'edflix.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
