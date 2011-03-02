import os, sys
import pymongo
import jinja2
from termcolor import colored

db = pymongo.Connection().cabinet

import controller

def main():
  execute(sys.argv)

def execute(args):
  cab = args.pop(0)
  command = args.pop(0)
  params = args

  print delegate(command, params)

def delegate(command, params):
  if command == 'list' and not params:
    return controller.all()
  elif command == 'list':
    return controller.type(params[0])
  elif command == 'add':
    return controller.add(*params)
  elif command == 'show':
    return controller.show(*params)
  return "cabinet"

def render(template, data):
  env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(
      os.path.abspath(__file__)), 'views')))

  env.filters['ljust'] = lambda s, w: s.ljust(w)
  return env.get_template(template).render(
        data).encode('utf-8')
