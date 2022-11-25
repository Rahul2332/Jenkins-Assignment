#!/usr/bin/python3

import unittest
from prime import if_prime


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(if_prime(17), True)

    def testCase2(self):
        self.assertEqual(if_prime(100), False)

    def testCase3(self):
        self.assertEqual(if_prime(31), True)


if __name__ == '__main__':
    unittest.main()