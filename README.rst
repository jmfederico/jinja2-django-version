==================
🔔 PROJECT STATUS 🔔
==================
Life has taken me to now work in GO_, and do not have the time to actively maintain this project.

.. _GO: https://go.dev/

Which means this project is looking for new maintainer, please `open an issue and postulate yourself`_ if interested.


.. _`open an issue and postulate yourself`: https://github.com/jmfederico/jinja2-django-version/issues/new

=====================
Jinja2 Django Version
=====================

.. image:: https://badge.fury.io/py/jinja2-django-version.svg
    :target: https://badge.fury.io/py/jinja2-django-version

.. image:: https://github.com/jmfederico/jinja2-django-version/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/jmfederico/jinja2-django-version/actions/workflows/tests.yml

A Jinja extension that creates a global variable with Django version
information for your Jinja2 templates:

Usage
-----
.. code-block:: console

    $ pip install jinja2-django-version

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_django_version.DjangoVersionExtension'])

    # 2.0
    template = env.from_string("{{ django_version }}")

    # 2.0
    template = env.from_string("{{ django_version.minor }}")

    # 2
    template = env.from_string("{{ django_version.major }}")

    # 2.0.2
    template = env.from_string("{{ django_version.micro }}")

    template.render()
