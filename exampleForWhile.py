class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print(f"✅ Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("⚠️ No books available in the library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)

    def search_book(self, title):
        found = [book for book in self.books if book.title.lower() == title.lower()]
        if not found:
            print("❌ Book not found.")
        else:
            for book in found:
                print("🎯 Found:", book)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"📖 Book '{book.title}' issued successfully!")
                else:
                    print("⚠️ Book is already issued.")
                return
        print("❌ Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"📚 Book '{book.title}' returned successfully!")
                else:
                    print("⚠️ Book was not issued.")
                return
        print("❌ Book ID not found.")


def main():
    library = Library()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter Book Title to search: ")
            library.search_book(title)

        elif choice == "4":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "5":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "6":
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
