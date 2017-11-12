# -*- coding: utf-8 -*-

from __future__ import print_function

import logging

import pandas as pd

from pybel.resources.arty import get_today_arty_namespace
from pybel.resources.definitions import write_namespace
from pybel.resources.deploy import deploy_namespace
from .constants import url

log = logging.getLogger(__name__)

MODULE_NAME = 'flybase'


def get_data():
    df = pd.read_csv(url, sep='\t', comment='#', header=None, compression='gzip')
    return df


def get_values():
    df = get_data()
    values = list(map(str, df[0]))
    return values


def write_belns(file):
    values = get_values()

    write_namespace(
        namespace_name="FlyBase Names",
        namespace_keyword="FLYBASE",
        namespace_domain="Gene and Gene Products",
        author_name='Charles Tapley Hoyt',
        citation_name=url,
        values=values,
        namespace_species='7227',
        namespace_description="FlyBase names for Drosophila Melanogaster Genes",
        author_copyright='Creative Commons by 4.0',
        functions="GRP",
        author_contact="charles.hoyt@scai.fraunhofer.de",
        file=file
    )


def deploy_to_arty(quit_fail_redeploy=True):
    """Gets the data, writes BEL namespace, and writes BEL knowledge to Artifactory"""
    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_belns(file)

    namespace_deploy_success = deploy_namespace(file_name, MODULE_NAME)

    if not namespace_deploy_success and quit_fail_redeploy:
        log.warning('did not redeploy')
        return False
