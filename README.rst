uavcontrol
=============================

.. image:: https://readthedocs.org/projects/uavcontrol/badge/?version=latest
   :target: https://uavcontrol.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://github.com/huln24/uavcontrol/actions/workflows/test.yml/badge.svg
   :target: https://github.com/huln24/uavcontrol/actions/workflows/test.yml
   :alt: Tests
      

.. image:: https://codecov.io/gh/huln24/uavcontrol/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/huln24/uavcontrol
   :alt: Coverage


Getting Started
~~~~~~~~~~~~~~~



Layout
~~~~~~

.. code-block:: bash

   <uavcontrol>/
   ├── .github                   # CI jobs to run on every push
   │   └── workflows
   │       └── test.yml
   ├── docs                      # Sphinx documentation of this package
   │   └── conf.py               
   ├── scripts                   # Helper script for launching
   │   └── run.sh
   ├── uavcontrol
   │   └── main.py               # main uav script
   ├── tests                     # testing
   │   ├── test_model.py 
   |   └── test_loader.py
   ├── .readthedocs.yml          # how to generate the docs in readthedocs
   ├── LICENSE                   # 
   ├── README.rst                # description of current project
   ├── requirements.txt          # requirements of this package
   ├── setup.py                  # installation configuration
   └── tox.ini                   # used to configure test/coverage
