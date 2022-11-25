#!/usr/bin/python3

import unittest
from prime import if_prime


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(if_prime(5), False)

    def testCase2(self):
        self.assertEqual(if_prime(20), True)


if __name__ == '__main__':
    unittest.main()