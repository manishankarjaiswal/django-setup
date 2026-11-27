from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase


class ProjectConfigTest(SimpleTestCase):
    def test_settings_loaded(self):
        self.assertTrue(settings.SECRET_KEY)
        self.assertEqual(settings.ROOT_URLCONF, "project.urls")
        self.assertIn("django.contrib.admin", settings.INSTALLED_APPS)

    def test_system_check(self):
        call_command("check")
