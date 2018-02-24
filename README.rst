=============================
Django Username Tools
=============================

.. image:: https://img.shields.io/travis/poudel/django-username-tools/master.svg?branch=master
    :target: http://travis-ci.org/poudel/django-username-tools

.. image:: https://img.shields.io/pypi/v/django-username-tools.svg
    :target: https://pypi.python.org/pypi/django-username-tools/

.. image:: https://img.shields.io/pypi/l/django-username-tools.svg
    :target: https://pypi.python.org/pypi/django-username-tools/

.. image:: https://img.shields.io/codecov/c/github/poudel/django-username-tools/master.svg
    :target: https://codecov.io/github/poudel/django-username-tools?branch=master

Utilities and fields that validate usernames during registration.
Useful for Django projects that allow public user registration.


Documentation
-------------

The full documentation is at https://django-username-tools.readthedocs.io.


Features
--------

* Validates using a blacklist of usernames. Comes with a default set of blacklisted usernames taken from `the-big-username-blacklist`_ project
* A ready-to-use `UsernameModelField` for custom user models and `UsernameFormField` for user registration form.
* Readable source code with 100% test coverage.


Installation
------------

See :doc:`./installation` for installation.


Usage
-----

See :doc:`./usage` for usage info.


Why use model to store the blocked usernames?
---------------------------------------------

Using database to store blacklisted username has several advantages. I belive that a blacklist of usernames should
be treated like any other data in the project. 

* The list can be updated dynamically from code or by using the django admin.
* The list can vary depending on different factors such as locality, and the scope of project etc.
* Database backend allows more sophisticated lookups that we can leverage if required.


TODO
----

* Add email username field
* A default blacklist of disposable email domains
* API docs for modules, classes and functions


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _the-big-username-blacklist: https://github.com/marteinn/The-Big-Username-Blacklist
