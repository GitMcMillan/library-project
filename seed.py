from init import CONN, CURSOR
from author import Author
from book import Book

def seed_authors():
  '''seed authors into db'''
  #list of authors
  authors = [
    "Stephen King",
    "Dean Koontz",
    "Michael Crichton",
    "Agatha Christie",
    "J.K. Rowling"
  ]

  #save the authors
  for author_name in authors:
    author = Author(author_name)
    author.save()

def seed_books():
  '''seed books into db (by author)'''
  #dictionary of books, key: author, value: list of books
  books_by_author = {
    "Stephen King": [
      "It", "The Shining", "Carrie", "Misery", "The Dark Tower", "The Green Mile", "The Long Walk"
    ],
    "Dean Koontz": [
      "Phantoms", "Watchers", "Odd Thomas", "Intensity", "Darkfall", "Cold Fire"
    ],
    "Michael Crichton": [
      "Jurassic Park", "The Lost World", "Sphere", "The Andromeda Strain", "Congo"
    ],
    "Agatha Christie": [
      "Murder on the Orient Express", "The ABC Murders", "And Then THere Were None", "The Murder of Roger Ackroyd", "Death on the Nile"
    ],
    "J.K. Rowling": [
      "Harry Potter and the Sorcereor's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows",
    ]
  }

  for author_name, titles in books_by_author.items():
    author = Author.find_by_name(author_name)
    if author:
      for title in titles:
        book = Book(title, author.id)
        book.save()

if __name__ == "__main__":
  seed_authors()
  seed_books()
  print("Database seeded successfully")



  [expression for value in (list)]