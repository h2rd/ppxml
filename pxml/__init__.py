#!/usr/bin/env python
# unicode: utf-8

import sys

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import XmlLexer

from xml.dom.minidom import parseString

INDENT=' '*2

def format_code(data):
  body = ''
  if data.startswith('HTTP'):
    end  = data.find("\r\n\r\n")
    body = data[0:end]
    data = data[end:].strip()

  lines = [line for line in parseString(data).toprettyxml(indent=INDENT).split('\n')
           if line.strip()]

  return "%s\n\n%s" % (body, '\n'.join(lines),)

def color_code(code):
  return highlight(code, XmlLexer(), TerminalFormatter())

def main():
  data = sys.stdin.read()
  data = color_code(format_code(data))

  return data

if __name__ == '__main__':
  print main()
