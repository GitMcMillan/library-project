#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()

#if table doesnt exist, create it
CURSOR.execute('''
  CREATE TABLE IF NOT EXISTS authors(
      id INTEGER PRIMARY KEY ,
      name TEXT UNIQUE 
      )               
''' )


#create books table if it doenst exist
CURSOR.execute('''
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author_id INTEGER,
    UNIQUE(title, author_id)
    FOREIGN KEY (author_id) REFERENCES authors(id)
  )
''')

CURSOR.execute("PRAGMA foreign_keys = ON;")
CONN.commit()