#!/usr/bin/env python3

from init import CONN, CURSOR
class Author:
  def __init__(self, name, id=None):
    self.name = name
    self.id = id


king = Author("Stephen King")

print(king)



# def test():
#   print("working")

# test()