import os, sys
import pymongo
from termcolor import colored

db = pymongo.Connection().cabinet

import controller

def main():
  execute(sys.argv)

def execute(args):
  cab = args.pop(0)
  command = args.pop(0)
  params = args

  output = delegate(command, params)
  if output:
    print output

def delegate(command, params):
  if command == 'list' and not params:
    return controller.all()
  elif command == 'list':
    return controller.type(params[0])
  elif command == 'add':
    return controller.add(*params)
  elif command == 'show':
    return controller.show(*params)
  elif command == 'tag':
    return controller.tag(*params)
  elif command == 'archive':
    return controller.archive(*params)
  elif command == 'delete':
    return controller.delete(*params)
  return "cabinet"
