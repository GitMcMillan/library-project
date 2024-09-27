from author import Author
from book import Book

def main_menu():
  while True:
    print("\nLibrary Menu")
    print("1. List all authors")
    print("2. Add a new author")
    print("3. List all books")
    print("4. Add a new book")
    print("5. Delete a book")
    print("6. List books by author")
    print("7. Search for a book by title")
    print("8. Exit")

    choice = input("Select an option")

    if choice == "1":
      #list all author
      authors = Author.all_authors()
      if authors:
        print("\nAuthors:")
        for author in authors:
          print(author)

    if choice == "2":
      #add new author
      name = input("Enter the authors name: ")
      new_author = Author(name)
      new_author.save()
      print(f"Author '{name}' added.") 

    if choice == "3":
      #list all books
      books = Book.all_books()
      if books:
        print("\nBooks:")
        for book in books:
          print(book)
      else:
        print("No books found.")
      #Add new book
      #delete a book
      #list by author
      #search by title
      #exit
  