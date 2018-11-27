# -*- coding: utf-8 -*-

"""Parsers for FlyBase."""

from bio2bel.downloading import make_df_getter
from .constants import GENE_MAPPING_PATH, GENE_MAPPING_URL

__all__ = [
    'get_mapping_df',
]

get_mapping_df = make_df_getter(
    GENE_MAPPING_URL,
    GENE_MAPPING_PATH,
    sep='\t',
    comment='#',
    compression='gzip',
    names=[
        'symbol',
        'flybase_id',
    ],
    usecols=[
        1,
        2,
    ],
    na_filter=False,
)
