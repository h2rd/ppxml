#!/usr/bin/env python
# unicode: utf-8

import sys

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import XmlLexer

import xml.dom.minidom as xml
import argparse

INDENT=' '*2

def format_code(data):
  return xml.parseString(data).toprettyxml(indent=INDENT)

def color_code(code):
  return highlight(code, XmlLexer(), TerminalFormatter())

def main():
  data=sys.stdin.read()
  data=color_code(format_code(data))

  return data

if __name__ == '__main__':
  print main()
