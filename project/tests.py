from django.conf import settings
from django.test import SimpleTestCase


class ProjectConfigTest(SimpleTestCase):
    def test_settings_loaded(self):
        self.assertTrue(settings.configured)
        self.assertIsNotNone(settings.SECRET_KEY)
