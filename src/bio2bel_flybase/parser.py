# -*- coding: utf-8 -*-

import pandas as pd

from .constants import url


def get_data(path=None):
    """Gets FlyBase data

    :param Optional[str] path: A custom path to FlyBase data
    :rtype: pandas.DataFrame
    """
    return pd.read_csv(
        path or url,
        sep='\t',
        comment='#',
        header=None,
        compression='gzip'
    )
