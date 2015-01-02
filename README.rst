ppxml
=====

Command-line tool to validate and pretty-print XML.

Setup
-----

Install throught git:: python

    pip install git+https://github.com/h2rd/ppxml

or without cache:: python

    cd /tmp
    git clone https://github.com/h2rd/ppxml
    cd ppxml
    python setup.py install

Examples
--------

Just prettify and colorize xml code:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml

Use xpath for get some elements:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item"

Use xpath for get deeper elements:: bash

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item/title"
