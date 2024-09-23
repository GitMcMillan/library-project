#!/usr/bin/env python3

from init import CONN, CURSOR

class Book:
  def __init__(self, title, author_id=None, id=None):
    self.title = title
    self.author_id = author_id
    self.id = id
  
  def save(self):
    '''inserts book into db if not exists, else retrieves book'''
    #check if book exists (id from where title and author_id = self instances
    CURSOR.execute("SELECT id FROM books WHERE title = ? AND author_id = ?", (self.title, self.author_id))
    result = CURSOR.fetchone()

    if result:
      #if book exists, grab id
      self.id = result[0]
    else:
      #book doesnt exist. Insertt it into db (title, author_id)
      CURSOR.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (self.title, self.author_id))
      CONN.commit()
      self.id = CURSOR.lastrowid

  def __repr__(self):
    return f"Book: {self.title}"

it = Book("It")
print(it)