#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('author.db')
CURSOR = CONN.cursor()