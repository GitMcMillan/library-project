#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()


#if table doesnt exist, create it
CURSOR.execute('''
  CREATE TABLE IF NOT EXISTS authors(
      id INTEGER PRIMARY KEY ,
      name TEXT NOT NULL 
      )               
''' )


#create books table if it doenst exist
CURSOR.execute('''
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    UNIQUE(title, author_id),
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
  )
''')

CURSOR.execute("PRAGMA foreign_keys = ON;")
CONN.commit()