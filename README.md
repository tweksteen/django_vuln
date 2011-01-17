django_vuln
===========

django_vuln is a Django project to test your pentester skills. It
can also be used to test your favorite penetration tool.

To install it, clone it and run:

    $ ./manage.py syncdb
    $ ./manage.py runserver

Then go to : http://127.0.0.1:8000

Currently, there are four applications:

 * SQL injection
 * XPath injection
 * Path traversal
 * XSS
