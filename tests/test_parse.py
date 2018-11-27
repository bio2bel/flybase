# -*- coding: utf-8 -*-

"""Tests for Bio2BEL FlyBase."""

import unittest

import pandas as pd

from bio2bel_flybase.parser import get_mapping_df
from tests.constants import TEST_FILE


class TestStuff(unittest.TestCase):
    """Tests for the FlyBase parsers."""

    def test_parser(self):
        """Test getting the mapping dataframe."""
        df = get_mapping_df(TEST_FILE)
        self.assertIsInstance(df, pd.DataFrame)
