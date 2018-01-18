Bio2BEL FlyBase |build| |coverage| |docs|
=========================================
This package converts FlyBase to a BEL namespace.

Citation
--------
Gramates LS, Marygold SJ, dos Santos G, Urbano J-M, Antonazzo G, Matthews BB, Rey AJ, Tabone CJ, Crosby MA, Emmert DB,
Falls K, Goodman JL, Hu Y, Ponting L, Schroeder AJ, Strelets VB, Thurmond J, Zhou P and the FlyBase Consortium. (2017)
FlyBase at 25: looking to the future. Nucleic Acids Res. 45(D1):D663-D671

Abstract
--------
Since 1992, FlyBase (flybase.org) has been an essential online resource for the Drosophila research community.
Concentrating on the most extensively studied species, Drosophila melanogaster, FlyBase includes information on genes
(molecular and genetic), transgenic constructs, phenotypes, genetic and physical interactions, and reagents such as
stocks and cDNAs. Access to data is provided through a number of tools, reports, and bulk-data downloads. Looking to
the future, FlyBase is expanding its focus to serve a broader scientific community. In this update, we describe new
features, datasets, reagent collections, and data presentations that address this goal, including enhanced orthology
data, Human Disease Model Reports, protein domain search and visualization, concise gene summaries, a portal for
external resources, video tutorials and the FlyBase Community Advisory Group.

Installation
------------
This code can be installed with :code:`pip3 install git+https://github.com/bio2bel/flybase.git`

Creating a Local Copy of the Namespace
--------------------------------------
A BEL namespace can be generated with :code:`python3 -m bio2bel_flybase write -o ~/Downloads/flybase.belns`

.. |build| image:: https://travis-ci.org/bio2bel/flybase.svg?branch=master
    :target: https://travis-ci.org/bio2bel/flybase
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/bio2bel/flybase/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/flybase?branch=master
    :alt: Coverage Status

.. |docs| image:: http://readthedocs.org/projects/bio2bel-flybase/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/flybase/en/latest/?badge=latest
    :alt: Documentation Status
