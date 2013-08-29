JayW-CheckIn
============
Django How To:
0. Try sudo if you got permission denied error.
1. Install pip so that you will easy to install other packages
 - Download https://raw.github.com/pypa/pip/master/contrib/get-pip.py
 - $ python get-pip.py 
2. Install Django
 - $ pip install django
 - $ pip install PIL (optional if you want to process image)
 - $ pip install django-social-auth (optional if you want to enable login by Facebook)
3. Pull JayW-Checkin
4. Inside project directory, run:
 - $ python manage.py syncdb
 - $ python manage.py runserver
5. Visit: http://127.0.0.1:8000
