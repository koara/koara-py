#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, unittest

test_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(test_root))

from koara import Koara

class StringReaderTest(unittest.TestCase):

    def test_paragraphs(self):
        self.assertEqual("a", "a")

if __name__ == '__main__':
    unittest.main()
