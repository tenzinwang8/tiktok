# LibraryManager.py

# Initialize empty data structures
books_list = []
authors_set = set()
books_dict = {}

# Add books to the library
books_list.append("Harry Potter")
authors_set.add("J.K. Rowling")
books_dict["Harry Potter"] = "J.K. Rowling"

books_list.append("Lord of the Rings")
authors_set.add("J.R.R. Tolkien")
books_dict["Lord of the Rings"] = "J.R.R. Tolkien"

books_list.append("To Kill a Mockingbird")
authors_set.add("Harper Lee")
books_dict["To Kill a Mockingbird"] = "Harper Lee"

# Searching for a Book
def search_book(title):
    if title in books_list:
        author = books_dict[title]
        print(f"Book found: {title} by {author}")
    else:
        print("Book not found.")

# Displaying All Books
def display_books():
    print("Books in the library:")
    for book in books_list:
        print(book)

# Removing a Book
def remove_book(title):
    if title in books_list:
        author = books_dict.pop(title)
        authors_set.remove(author)
        books_list.remove(title)
        print(f"{title} by {author} removed successfully.")
    else:
        print("Book not found.")

# Main function
def main():
    while True:
        print("\n1. Search for a book")
        print("2. Display all books")
        print("3. Remove a book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title of the book: ")
            search_book(title)
        elif choice == "2":
            display_books()
        elif choice == "3":
            title = input("Enter the title of the book to remove: ")
            remove_book(title)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
