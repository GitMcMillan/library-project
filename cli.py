from author import Author
from book import Book

def main_menu():
    while True:
        print("*******************")
        print("\nLibrary Menu:")
        print("1. List all authors")
        print("2. Add a new author")
        print("3. Delete an author")
        print("4. List all books")
        print("5. Add a new book")
        print("6. Delete a book")
        print("7. List books by author")
        print("8. Search for a book by title")
        print("9. Exit")
        print("*******************")

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

        elif choice == "2":
            # add author
            name = input("Enter the author's name: ")
            new_author = Author(name)
            new_author.save()
            print(f"Author '{name}' added.")
             
        elif choice == "3":
            # delete author
            author_name = input("Enter the author's name to delete: ")
            author = Author.find_by_name(author_name)
            if author:
                author.delete()
                print(f"Author '{author.name}' deleted.")
            else:
                print("Author not found.")

        elif choice == "4":
            # list books
            books = Book.all_books()
            if books:
                print("\nBooks:")
                for book in books:
                    print(book)
            else:
                print("No books found.")

        elif choice == "5":
            # add book
            title = input("Enter the book's title: ")
            author_name = input("Enter the author's name: ")
            author = Author.find_by_name(author_name)
            if author:
                new_book = Book(title, author.id)  # Pass author_id instead of name
                new_book.save()
                print(f"Book '{title}' added.")
            else:
                print("Invalid author name. Please try again.")

        elif choice == "6":
            # delete book
            book_title = input("Enter the book's title to delete: ")
            book = Book.find_by_title(book_title)
            if book:
                book.delete()
                print(f"Book '{book.title}' deleted.")
            else:
                print("Book not found.")
             
        elif choice == "7":
            # list books by author
            author_name = input("Enter the author's name: ")
            author = Author.find_by_name(author_name)
            if author:
                books_by_author = Book.list_books_by_author(author.id)
                if books_by_author:
                    print(f"\nBooks by {author.name}:")
                    for book in books_by_author:
                        print(book)
                else:
                    print(f"No books found for author {author.name}.")
            else:
                print("Author not found.")

        elif choice == "8":
            # search for a book by title
            book_title = input("Enter the book's title to search: ")
            book = Book.find_by_title(book_title)
            if book:
                print(f"Book found: {book}")
            else:
                print("Book not found.")

        elif choice == "9":
            # exit
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

        # Ask if the user wants to go back to the main menu
        continue_choice = input("\nDo you want to go back to the menu? (y/n): ").lower()
        if continue_choice != 'y':
            print("Goodbye!")
            break


# Helper function to validate author name
def validate_author_name(author_name):
    '''Check if author exists in db'''
    return Author.find_by_name(author_name) is not None

# Start the main menu
main_menu()
