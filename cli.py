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

        choice = input("Select an option: ")

        if choice == "1":
            # list authors
            authors = Author.all_authors()
            if authors:
                print("\nAuthors:")
                for author in authors:
                    print(author)
            else:
                print("No authors found.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
            

        elif choice == "2":
            # add author
            name = input("Enter the author's name: ")
            new_author = Author(name)
            new_author.save()
            print(f"Author '{name}' added.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
             

        elif choice == "3":
            #list books
            books = Book.all_books()
            if books:
                print("\nBooks:")
                for book in books:
                    print(book)
            else:
                print("No books found.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
            

        elif choice == "4":
            #add book
            title = input("Enter the book's title: ")
            author_id = input("Enter the author ID: ")
            if validate_author_id(author_id):
                new_book = Book(title, author_id)
                new_book.save()
                print(f"Book '{title}' added.")
            else:
                print("Invalid author ID. Please try again.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
            

        elif choice == "5":
            #delete book
            book_title = input("Enter the book's title to delete: ")
            book = Book.find_by_title(book_title)
            if book:
                book.delete()
                print(f"Book '{book.title}' deleted.")
            else:
                print("Book not found.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
             

        elif choice == "6":
            #list by author
            author_id = input("Enter the author ID: ")
            if validate_author_id(author_id):
                books_by_author = Book.list_books_by_author(author_id)
                if books_by_author:
                    print(f"\nBooks by Author ID {author_id}:")
                    for book in books_by_author:
                        print(book)
                else:
                    print("No books found for this author.")
            else:
                print("Invalid author ID.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
             

        elif choice == "7":
            #find by title
            book_title = input("Enter the book's title to search: ")
            book = Book.find_by_title(book_title)
            if book:
                print(f"Book found: {book}")
            else:
                print("Book not found.")

            continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
            if continue_choice != 'y':
              print("Goodbye!")
              break
            

        elif choice == "8":
            #exit
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")




# Helper function to validate author ID
def validate_author_id(author_id):
    '''Check if author exists in db'''
    return Author.find_by_id(author_id) is not None

# Start the main menu
main_menu()