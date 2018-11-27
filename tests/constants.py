# -*- coding: utf-8 -*-

"""Testing constants for Bio2BEL FlyBase."""

import logging
import os

log = logging.getLogger(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

TEST_FILE = os.path.join(dir_path, 'test_gene_map_table.tsv.gz')
