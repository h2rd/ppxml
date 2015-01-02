ppxml
====

Command-line tool to validate and pretty-print XML.

Setup
-----

Install throught git::

    pip install git+https://github.com/h2rd/ppxml
    
or without cache::

    cd /tmp
    git clone https://github.com/h2rd/ppxml
    cd ppxml
    python setup.py install

Examples
--------

Just prettify and colorize xml code::

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml

Use xpath for get some elements::

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item"

Use xpath for get deeper elements::

    curl http://feeds.bbci.co.uk/news/rss.xml | ppxml -x "//item/title"
