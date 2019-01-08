"""
  This file will load our parsers in the parsers directory
  (Parser Loader)
"""

import os
import re
import inspect

# Return List of files located in parsers directory
def _get_parser_list(dirname):
  files = [f.replace('.py', '') for f in os.listdir(dirname) if not f.startswith('__')]
  return files

"""
  Imports module and use inspect to find parser classes
  Return dict with name of class and the class object to be later used in creating 
  instances of parser
"""
def _import_parsers(parserfiles):
  m = re.compile('.+parser$', re.I)
  _modules = __import__('weatherterm.parsers', globals(), locals(), parserfiles, 0)
  _parsers = [(k,v) for k, v in inspect.getmembers(_modules) if inspect.ismodule(v) and m.match(k)]
  _classes = dict()
  for k, v in _parsers:
    _classes.update({k: v for k, v in inspect.getmembers(v) if inspect.isclass(v) and m.match(k)})

  return _classes


def load(dirname):
  parserfiles = _get_parser_list(dirname)
  return _import_parsers(parserfiles)
