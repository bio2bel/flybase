# -*- coding: utf-8 -*-

import logging

from pybel.constants import NAMESPACE_DOMAIN_GENE
from pybel.resources.arty import get_today_arty_namespace
from pybel.resources.definitions import write_namespace
from pybel.resources.deploy import deploy_namespace

from .constants import url
from .parser import get_data

log = logging.getLogger(__name__)

MODULE_NAME = 'flybase'


def get_values(path=None):
    """Gets the names from FlyBase

    :param Optional[str] path: A custom path to FlyBase data
    :rtype:
    """
    df = get_data(path=path)
    values = list(map(str, df[0]))
    return values


def write_belns(file=None, path=None):
    """Writes the FlyBase names as a BEL namespace

    :param file:
    :param Optional[str] path: A custom path to FlyBase data
    :return:
    """
    values = get_values(path=path)

    write_namespace(
        namespace_name="FlyBase Names",
        namespace_keyword="FLYBASE",
        namespace_domain=NAMESPACE_DOMAIN_GENE,
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
    """Gets the data, writes BEL namespace, and writes BEL knowledge to Artifactory

    :rtype: Optional[str]
    """
    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_belns(file)

    namespace_deploy_success = deploy_namespace(file_name, MODULE_NAME)

    if not namespace_deploy_success and quit_fail_redeploy:
        log.warning('did not redeploy')
        return False

    return namespace_deploy_success
