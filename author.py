#!/usr/bin/env python3

from init import CONN, CURSOR

class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def save(self):
        '''Inserts author into the db only if not already present, otherwise retrieves the existing author'''
        # Check if the author already exists
        CURSOR.execute("SELECT id FROM authors WHERE name = ?", (self.name,))
        result = CURSOR.fetchone()  # fetchone() returns None if no result is found

        if result:
            # Author already exists, retrieve the id (result is a tuple containing the id)
            self.id = result[0]
        else:
            # Author doesn't exist, insert into the database
            CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def all_authors(cls):
        '''Return authors from db as a list'''
        CURSOR.execute("SELECT * FROM authors")
        author_rows = CURSOR.fetchall()
        return [cls(name=row[1], id=row[0]) for row in author_rows]

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"
    
    


# Create author/save to db
king = Author("Stephen King")
king.save()
print(king)

# Fetch and print all authors
authors = Author.all_authors()
for author in authors:
    print(author)


# def test():
#   print("working")

# test()