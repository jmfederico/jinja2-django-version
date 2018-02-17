"""Define tests for jinja2-django-version."""

import unittest

import django
from jinja2 import Environment


class TestPackagePath(unittest.TestCase):
    """Define test case for extension importing paths."""

    def test_package_path(self):
        """Test DjangoVersionExtensions can be loaded at package level."""
        try:
            Environment(extensions=['jinja2_django_version.DjangoVersionExtension'])
        except AttributeError:
            self.fail("AttributeError raised unexpectedly.")


class TestGlobalIsLoaded(unittest.TestCase):
    """Define test case for template global variable."""

    def setUp(self):
        """Set up test case."""
        self.environment = Environment(extensions=['jinja2_django_version.DjangoVersionExtension'])

    def test_global_is_set(self):
        """Test global variable is loaded."""
        self.assertIn('django_version', self.environment.globals)


class TestVersionOutput(unittest.TestCase):
    """Define test case for version output."""

    def setUp(self):
        """Set up test case."""
        self.environment = Environment(extensions=['jinja2_django_version.DjangoVersionExtension'])
        self.version = [str(x) for x in django.VERSION]

    def test_micro_versions(self):
        """Test micro version output."""
        template = self.environment.from_string('{{ django_version.micro }}')
        output = template.render()
        minor_version = '.'.join(self.version[:3])
        self.assertEqual(minor_version, output)

    def test_minor_versions(self):
        """Test minor version output."""
        template = self.environment.from_string('{{ django_version.minor }}')
        output = template.render()
        minor_version = '.'.join(self.version[:2])
        self.assertEqual(minor_version, output)

    def test_major_versions(self):
        """Test major version output."""
        template = self.environment.from_string('{{ django_version.major }}')
        output = template.render()
        minor_version = '.'.join(self.version[:1])
        self.assertEqual(minor_version, output)

    def test_versions(self):
        """Test version output."""
        template = self.environment.from_string('{{ django_version }}')
        output = template.render()
        minor_version = '.'.join(self.version[:2])
        self.assertEqual(minor_version, output)


if __name__ == '__main__':
    unittest.main()
