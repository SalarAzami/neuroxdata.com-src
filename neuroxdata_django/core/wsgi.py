import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neuroxdata_django.core.settings')
application = get_wsgi_application()