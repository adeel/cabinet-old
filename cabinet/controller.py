import cabinet
from cabinet import *
from cabinet import etc, errors

import subprocess
import tempfile

def all():
  items = list(db.items.find())

  maxes = etc.get_max_widths(items, ('id', 'type'))

  output = []
  for i in items:
    line = "%s %s %s" % (
      colored(i['type'].ljust(maxes['type']), 'green'),
      str(i['id']).ljust(maxes['id']),
      colored(' '.join([t for t in i['tags']]), 'yellow'))
    if i['content']:
      line += " %s" % (
        colored(i['content'].splitlines()[0][:79 - len(line)], attrs=['bold']))
    output.append(line)

  return '\n'.join(output)

def type(name):
  items = list(db.items.find({'type': name}))

  maxes = etc.get_max_widths(items, ('id', 'type'))

  output = []
  for i in items:
    line = "%s %s" % (
      str(i['id']).ljust(maxes['id']),
      colored(' '.join([t for t in i['tags']]), 'yellow'))
    if i['content']:
      line += " %s" % (
        colored(i['content'].splitlines()[0][:79 - len(line)], attrs=['bold']))
    output.append(line)

  return '\n'.join(output)

def add(type, filename=None, *tags):
  if not filename:
    filename = tempfile.NamedTemporaryFile(mode='w+t', delete=False).name
    editor = os.path.expandvars('$EDITOR')
    subprocess.call([editor, filename])
  try:
    content = open(filename, 'r').read()
  except IOError:
    raise errors.FileNotReadable(filename)

  last = db.items.find_one({'type': type}, sort=[('id', pymongo.DESCENDING)])
  if last:
    id = last['id'] + 1
  else:
    id = 1

  db.items.insert({'id': id, 'type': type, 'content': content, 'tags': tags})

  return ''

def show(type, id):
  try:
    id = int(id)
  except ValueError:
    raise errors.NoSuchItem(id)
  item = db.items.find_one({'type': type, 'id': id})
  if not item:
    raise errors.NoSuchItem(id)

  return item['content']

def tag(type, id, *tags):
  try:
    id = int(id)
  except ValueError:
    raise errors.NoSuchItem(id)
  item = db.items.find_one({'type': type, 'id': id})
  if not item:
    raise errors.NoSuchItem(id)

  db.items.update({'_id': item['_id']}, {'$set': {'tags':
    item['tags'] + list(tags)}})

  return ''

def delete(type, id):
  try:
    id = int(id)
  except ValueError:
    raise errors.NoSuchItem(id)
  item = db.items.find_one({'type': type, 'id': id})
  if not item:
    raise errors.NoSuchItem(id)

  db.items.remove(item['_id'])
  return ''
