# Book Library System

# List to store books
library = []

def add_book(title, author, year):
    """Add a new book to the library."""
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    library.append(book)
    print(f"Book '{title}' by {author} added.")

def view_books():
    """View all books in the library."""
    if library:
        print("Library Books:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print("No books found in the library.")

def search_books_by_title(title):
    """Search and display books by title."""
    found_books = [book for book in library if title.lower() in book['title'].lower()]
    if found_books:
        print("Books found:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print(f"No books found with title '{title}'.")

def search_books_by_author(author):
    """Search and display books by author."""
    found_books = [book for book in library if author.lower() in book['author'].lower()]
    if found_books:
        print("Books found:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        print(f"No books found by author '{author}'.")

def main():
    while True:
        print("\nBook Library Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books by Title")
        print("4. Search Books by Author")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            add_book(title, author, year)
        elif choice == '2':
            view_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_books_by_title(title)
        elif choice == '4':
            author = input("Enter author name to search: ")
            search_books_by_author(author)
        elif choice == '5':
            print("Exiting Book Library System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
