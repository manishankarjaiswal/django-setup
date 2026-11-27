from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase
from django.urls import reverse


class ProjectConfigTest(SimpleTestCase):
    def test_settings_loaded(self):
        self.assertTrue(settings.SECRET_KEY)
        self.assertEqual(settings.ROOT_URLCONF, "project.urls")
        self.assertIn("django.contrib.admin", settings.INSTALLED_APPS)

    def test_system_check(self):
        call_command("check")


class HealthCheckTest(SimpleTestCase):
    def test_health_check(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_health_check_reverse(self):
        response = self.client.get(reverse("health_check"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
