import re
import datetime
import urlparse
import hashlib

from elixir import *
from elixir.events import *

metadata.bind = 'sqlite:///db.sqlite'
metadata.bind.echo = False

class Item(Entity):
  id = Field(Integer, primary_key=True)
  content = Field(UnicodeText)

  type = ManyToOne('Type')
  tags = ManyToMany('Tag')

class Type(Entity):
  id = Field(Integer, primary_key=True)
  name = Field(Unicode)
  items = OneToMany('Item')

class Tag(Entity):
  id = Field(Integer, primary_key=True)
  name = Field(Unicode)
  items = ManyToMany('Item')

create_all()
setup_all()

if __name__ == '__main__':
  setup_all(create_tables=True)

  # Populate.

  types = {
    'mail': Type(name='mail'),
    'todo': Type(name='todo')}
  tags = {
    'math': Tag(name='math'),
    'school': Tag(name='school')}

  types['mail'].items = [
    Item(content="Message 1.", tags=[tags['math']]),
    Item(content="Message 2.", tags=[tags['school']])]
  types['todo'].items = [
    Item(content="Todo 1.", tags=[tags['math']]),
    Item(content="Todo 2.", tags=[tags['school']]),
  ]

  session.commit()

  print "Saved %d items." % Item.query.count()