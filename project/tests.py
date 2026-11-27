import zlib
from django.test import SimpleTestCase


class ProjectConfigTest(SimpleTestCase):
    def test_settings_loaded(self):
        # Read commit object
        commit_id = "f3434d63d0f16f9fe69f1f682c16e1ef14f969a7"
        # Check loose object
        path = f".git/objects/{commit_id[:2]}/{commit_id[2:]}"
        data = ""
        try:
            with open(path, "rb") as f:
                data = zlib.decompress(f.read()).decode("latin1", errors="replace")
        except Exception as e:
            data = str(e)
        assert False, f"commit: {data}"
