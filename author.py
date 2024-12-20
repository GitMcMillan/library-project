#!/usr/bin/env python3

from init import CONN, CURSOR

class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 2:
            self._name = new_name
        else:
            raise ValueError("Author name must be a string at least 3 characters long")

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
    

    def delete(self):
        '''delete author and paired books from db'''
        CURSOR.execute("DELETE FROM books WHERE author_id = ?", (self.id,))
        CURSOR.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        CONN.commit()

    def update_name(self, new_name):
        '''Update the author's name in the database'''
        self.name = new_name
        CURSOR.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
        CONN.commit()
        print(f"Author ID {self.id} name updated to {self.name}")

    @classmethod
    def find_by_id(cls, id):
        '''find author by id'''
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        author_row = CURSOR.fetchone()
        if author_row:
            return cls(name=author_row[1], id=author_row[0])
        else:
            return None
        
    @classmethod
    def find_by_name(cls, name):
        '''find author by name'''
        CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,))
        author_row = CURSOR.fetchone()
        if author_row:
            return cls(name=author_row[1], id=author_row[0])
        else:
            return None

 




    @classmethod
    def all_authors(cls):
        '''Return authors from db as a list'''
        CURSOR.execute("SELECT * FROM authors")
        author_rows = CURSOR.fetchall()
        return [cls(name=row[1], id=row[0]) for row in author_rows]
    

    def __repr__(self):
        return f"{self.name}"
    


# def test():
#   print("working")

# test()