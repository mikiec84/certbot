import unittest

from certbot.compat import os


class OsTest(unittest.TestCase):
    """Unit tests for os module."""
    def test_forbidden_methods(self):
        for method in ['chmod']:
            self.assertRaises(RuntimeError, getattr(os, method))