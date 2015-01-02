#!/usr/bin/env python
# unicode: utf-8

from __future__ import print_function
import sys
import argparse

from lxml import etree
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import XmlLexer
import chardet


def format_code(xml):
    lines = [line for line in str(xml).split('\n') if line.strip()]
    return '\n'.join(lines)


def color_code(code):
    return highlight(code, XmlLexer(), TerminalFormatter())


def get_xml(xml, xpath=None):
    parser = etree.XMLParser(remove_blank_text=True, encoding=chardet.detect(xml)['encoding'])
    root = etree.fromstring(xml, parser)
    if xpath:
        return "\n".join([etree.tostring(i, pretty_print=True)
                          for i in root.xpath(xpath)])

    return etree.tostring(root, pretty_print=True)


def main():
    parser = argparse.ArgumentParser(description="Command-line tool to pretty-print XML with xpath")
    parser.add_argument("-x", '--xpath', help="Use xpath", default="")
    args = parser.parse_args()

    if sys.stdin.isatty():
        return 'Please use stdin'

    data = sys.stdin.read()
    try:
        data = color_code(format_code(get_xml(data, args.xpath)))
    except ValueError as e:
        print(e)

    return data or ''


if __name__ == '__main__':
    print(main())
