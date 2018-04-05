from django.test import TestCase


class MyAppTestCase(TestCase):
    def test_one(self):
        self.assertEqual(1, 1)
