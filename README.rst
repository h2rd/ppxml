pxml
====

Command-line tool to validate and pretty-print XML.

Setup
-----

    pip install git+https://github.com/h2rd/pxml

Examples
--------

Just prettify and colorize xml code::

    curl http://feeds.bbci.co.uk/news/rss.xml | pxml

Use xpath for get some elements::

    curl http://feeds.bbci.co.uk/news/rss.xml | pxml -x "//item"

Use xpath for get deeper elements::

    curl http://feeds.bbci.co.uk/news/rss.xml | pxml -x "//item/title"
