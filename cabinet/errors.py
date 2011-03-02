class NoSuchItem(Exception):
  def __init__(self, id):
    self.value = id
  def __str__(self):
    return repr(self.value)

class FileNotReadable(Exception):
  def __init__(self, filename):
    self.value = filename
  def __str__(self):
    return repr(self.value)
