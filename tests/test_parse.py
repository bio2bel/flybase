# -*- coding: utf-8 -*-

import unittest

import pandas as pd

from bio2bel_flybase.parser import get_data
from tests.constants import TEST_FILE


class TestStuff(unittest.TestCase):
    def test_parser(self):
        df = get_data(path=TEST_FILE)
        self.assertIsInstance(df, pd.DataFrame)
