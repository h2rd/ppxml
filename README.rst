ppxml
=====

Command-line tool to validate and pretty-print XML.

Setup
-----

.. code-block:: bash

  # Install through pip
  pip install ppxml

  # Install through git
  pip install git+https://github.com/h2rd/ppxml

  # or without cache
  cd /tmp
  git clone https://github.com/h2rd/ppxml
  cd ppxml
  python setup.py install

Examples
--------

Just prettify and colorize xml code:

.. code-block:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml

Use xpath for get some elements:

.. code-block:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item"

Use xpath for get deeper elements:

.. code-block:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item/title"
