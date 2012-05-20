import re
import unittest
import er

class TestEr(unittest.TestCase):
    def test_generate(self):
        self.assertEqual(er.generate(r'1'), '1')

    def test_generate_digits(self):
        password = er.generate(r'[0-9]{10}')
        self.assertTrue(re.search(r'^[0-9]{10}$', password))

    def test_generate_positional(self):
        self.assertNotEqual(re.search('^[0-9]', er.generate('^[0-9]m^oose$', shuffle=True)), None)