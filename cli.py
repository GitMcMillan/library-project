from author import Author
from book import Book
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to print a separator line
def print_separator():
    print(Fore.MAGENTA + "************************************************" + Style.RESET_ALL)

# Success message with green color
def success_message(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

# Error message with red color
def error_message(message):
    print(Fore.RED + message + Style.RESET_ALL)

# Prompt message with yellow color
def prompt_message(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

def main_menu():
    while True:
        print_separator()
        print(Fore.CYAN + "\nLibrary Menu:")
        print(Fore.CYAN + "1. List all authors")
        print(Fore.CYAN + "2. Add a new author")
        print(Fore.CYAN + "3. Delete an author")
        print(Fore.CYAN + "4. List all books")
        print(Fore.CYAN + "5. Add a new book")
        print(Fore.CYAN + "6. Delete a book")
        print(Fore.CYAN + "7. List books by author")
        print(Fore.CYAN + "8. Search for a book by title")
        print(Fore.CYAN + "9. Update author name")  
        print(Fore.CYAN + "10. Update book title")  
        print(Fore.CYAN + "11. Exit")
        print_separator()

        choice = input(Fore.YELLOW + "Select an option: " + Style.RESET_ALL)

        if choice == "1":
            # list authors
            authors = Author.all_authors()
            if authors:
                print_separator()
                prompt_message("\nAuthors:")
                for i, author in enumerate(authors, start=1):
                    print(f"{i}. {author}")
                print_separator()
            else:
                error_message("No authors found.")

        elif choice == "2":
            # add author
            name = input(Fore.YELLOW + "Enter the author's name: " + Style.RESET_ALL)
            new_author = Author(name)
            new_author.save()
            success_message(f"Author '{name}' added.")
             
        elif choice == "3":
            # delete author
            author_name = input(Fore.YELLOW + "Enter the author's name to delete: " + Style.RESET_ALL)
            author = Author.find_by_name(author_name)
            if author:
                author.delete()
                success_message(f"Author '{author.name}' deleted.")
            else:
                error_message("Author not found.")

        elif choice == "4":
            # list books
            books = Book.all_books()
            if books:
                print_separator()
                prompt_message("\nBooks:")
                for i, book in enumerate(books, start=1):
                    print(f"{i}. {book}")
                print_separator()
            else:
                error_message("No books found.")

        elif choice == "5":
            # add book
            title = input(Fore.YELLOW + "Enter the book's title: " + Style.RESET_ALL)
            author_name = input(Fore.YELLOW + "Enter the author's name: " + Style.RESET_ALL)
            author = Author.find_by_name(author_name)
            if author:
                new_book = Book(title, author.id)  # Pass author_id instead of name
                new_book.save()
                success_message(f"Book '{title}' added.")
            else:
                error_message("Invalid author name. Please try again.")

        elif choice == "6":
            # delete book
            book_title = input(Fore.YELLOW + "Enter the book's title to delete: " + Style.RESET_ALL)
            book = Book.find_by_title(book_title)
            if book:
                book.delete()
                success_message(f"Book '{book.title}' deleted.")
            else:
                error_message("Book not found.")
             
        elif choice == "7":
            # list books by author
            author_name = input(Fore.YELLOW + "Enter the author's name: " + Style.RESET_ALL)
            author = Author.find_by_name(author_name)
            if author:
                books_by_author = Book.list_books_by_author(author.id)
                if books_by_author:
                    print_separator()
                    prompt_message(f"\nBooks by {author.name}:")
                    for i, book in enumerate(books_by_author, start=1):
                        print(f"{i}. {book}")
                    print_separator()
                else:
                    error_message(f"No books found for author {author.name}.")
            else:
                error_message("Author not found.")

        elif choice == "8":
            # search for a book by title
            book_title = input(Fore.YELLOW + "Enter the book's title to search: " + Style.RESET_ALL)
            book = Book.find_by_title(book_title)
            if book:
                success_message(f"Book found: {book}")
            else:
                error_message("Book not found.")

        elif choice == "9":
            # update author name
            author_name = input(Fore.YELLOW + "Enter the author's current name: " + Style.RESET_ALL)
            author = Author.find_by_name(author_name)
            if author:
                new_name = input(Fore.YELLOW + "Enter the new name for the author: " + Style.RESET_ALL)
                author.update_name(new_name)
                success_message(f"Author's name updated to '{new_name}'.")
            else:
                error_message("Author not found.")
        
        elif choice == "10":
            # update book title
            book_title = input(Fore.YELLOW + "Enter the book's current title: " + Style.RESET_ALL)
            book = Book.find_by_title(book_title)
            if book:
                new_title = input(Fore.YELLOW + "Enter the new title for the book: " + Style.RESET_ALL)
                book.update_title(new_title)
                success_message(f"Book's title updated to '{new_title}'.")
            else:
                error_message("Book not found.")

        elif choice == "11":
            # exit
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break

        else:
            error_message("Invalid option, please try again.")

        # Ask if the user wants to go back to the main menu
        continue_choice = input(Fore.YELLOW + "\nDo you want to go back to the menu? (y/n): " + Style.RESET_ALL).lower()
        if continue_choice != 'y':
            print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
            break


# Helper function to validate author name
def validate_author_name(author_name):
    '''Check if author exists in db'''
    return Author.find_by_name(author_name) is not None

# Start the main menu
main_menu()


