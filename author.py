#!/usr/bin/env python3

from init import CONN, CURSOR
class Author:
  def __init__(self, name, id=None):
    self.name = name
    self.id = id

  def save(self):
    '''Inserts author table into db, saves id'''
    CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
    CONN.commit()
    self.id = CURSOR.lastrowid

  @classmethod
  def get_all_authors(cls):
    '''Return authors from db as a list'''
    CURSOR.execute("SELECT * FROM authors")
    author_rows= CURSOR.fetchall()
    return [cls(name=row[1], id=row[0]) for row in author_rows]
  
  def __repr__(self):
    return f"Author(id={self.id}, name={self.name})"

#create author/save to db
king = Author("Stephen King")
king.save()
print(king)

#fetch and print all authors
authors = Author.get_all_authors()
for author in authors:
  print(author)


# def test():
#   print("working")

# test()