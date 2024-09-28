#!/usr/bin/env python3

from init import CONN, CURSOR
from author import Author

class Book:
  def __init__(self, title, author_id=None, id=None):
    self.title = title
    self.author_id = author_id
    self.id = id


  def get_author_name(self):
    '''Fetch the author's name from the authors table using author_id'''
    CURSOR.execute("SELECT name FROM authors WHERE id = ?", (self.author_id,))
    author_row = CURSOR.fetchone()
    return author_row[0] if author_row else "Unknown Author"
  
  def save(self):
    '''inserts book into db if not exists, else retrieves book'''
    #check if book exists (id from where title and author_id = self instances
    CURSOR.execute("SELECT id FROM books WHERE title = ? AND author_id = ?", (self.title, self.author_id))
    result = CURSOR.fetchone()

    if result:
      #if book exists, grab id
      self.id = result[0]
    else:
      #book doesnt exist. Insert it into db (title, author_id)
      CURSOR.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (self.title, self.author_id))
      CONN.commit()
      self.id = CURSOR.lastrowid

  def delete(self):
    '''delete a book from db'''
    CURSOR.execute("DELETE FROM books WHERE id = ?", (self.id,))
    CONN.commit()

  def update_title(self, new_title):
    '''Update the book's title in the database and the object'''
    self.title = new_title
    CURSOR.execute("UPDATE books SET title = ? WHERE id = ?", (self.title, self.id))
    CONN.commit()


  @classmethod
  def list_books_by_author(cls, author_id):
    '''Fetch and list books by a specific author'''
    CURSOR.execute("SELECT * FROM books WHERE author_id = ?", (author_id,))
    book_rows = CURSOR.fetchall()
    return [cls(title=row[1], author_id=row[2], id=row[0]) for row in book_rows]

  @classmethod
  def all_books(cls):
    '''return books from db as a list'''
    CURSOR.execute("SELECT * FROM books")
    book_rows = CURSOR.fetchall()
    return [cls(title=row[1], author_id=row[2], id=row[0]) for row in book_rows]


  @classmethod
  def find_by_title(cls, title):
    '''find book by its title (duh)'''
    CURSOR.execute("SELECT * FROM books WHERE LOWER(title) = LOWER(?)",(title,))
    book_row = CURSOR.fetchone()
    if book_row:
      return cls(title=book_row[1], author_id=book_row[2], id=book_row[0])
    else:
      return None



  def __repr__(self):
    author_name = self.get_author_name()
    return f"`{self.title}`, by {author_name}"

it = Book("It", 1)
it.save()






