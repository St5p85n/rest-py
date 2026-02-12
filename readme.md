## pip install psycopg2-binary gunicorn dj-database-url
## pip freeze > requirements.txt
# dans le setting
**
import os
import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

DEBUG = False

ALLOWED_HOSTS = ['.onrender.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://rest-py.onrender.com']

**
## creer un bd postgres sur render
## creer un service 
## gunicorn nomduprojet.wsgi:application
