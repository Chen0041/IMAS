from time import sleep

from django.test import TestCase


# Create your tests here.
class SmokeTestCase(TestCase):
    def test_smoke(self):
        sleep(168.5)
        self.assertEqual(1 + 1, 2)