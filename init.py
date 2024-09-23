#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()

#if table doesnt exist, create it
CURSOR.execute('''
  CREATE TABLE IF NOT EXISTS authors(
      id INTEGER PRIMARY KEY,
      name TEXT
      )               
''' )
CONN.commit()