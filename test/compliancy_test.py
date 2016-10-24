#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, unittest

test_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(test_root))

class ComplianceTest(unittest.TestCase):

    def test_paragraphs(self):
        self.assertTrue('FOO'.isupper())

if __name__ == '__main__':
    unittest.main()
