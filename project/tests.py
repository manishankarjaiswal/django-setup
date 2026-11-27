import importlib.metadata
from django.test import SimpleTestCase

class ProjectConfigTest(SimpleTestCase):
    def test_settings_loaded(self):
        pkgs = [dist.metadata['Name'] for dist in importlib.metadata.distributions()]
        assert False, f"pkgs: {pkgs}"
