"""
Unit test of compute function
"""

import unittest

import stuff


class TestCompute(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(2.0, stuff.compute(1.0))
        self.assertEqual(4.0, stuff.compute(2.0))

    def testMore(self):
        self.assertEqual(2.2, stuff.compute(1.1))
