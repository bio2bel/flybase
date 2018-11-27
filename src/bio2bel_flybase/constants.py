# -*- coding: utf-8 -*-

"""Constants for Bio2BEL FlyBase."""

import os

from bio2bel import get_data_dir

VERSION = '0.0.1-dev'

MODULE_NAME = 'fb'
DATA_DIR = get_data_dir(MODULE_NAME)

BASE_URL = 'ftp://ftp.flybase.net/releases/current/precomputed_files/genes'
DATE = '2018_05'

GENE_MAPPING_FNAME = f'gene_map_table_fb_{DATE}.tsv.gz'

#: Location of mapping table. Needs to be manually updated, or a scraper should be written (eww)
GENE_MAPPING_URL = f'{BASE_URL}/{GENE_MAPPING_FNAME}'
GENE_MAPPING_PATH = os.path.join(DATA_DIR, GENE_MAPPING_FNAME)
