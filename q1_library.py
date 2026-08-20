class Book:
    next_id = 1

    def __init__(self, title, author):
        self.book_id = Book.next_id
        Book.next_id += 1

        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("No books found.")
            return

        for book in self.books:
            print(book)

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(book)
                return
        print("Book not found.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully.")
                return
        print("Book not found.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")


library = Library()

library.add_book("Python Crash Course", "Eric Matthes")
library.add_book("Atomic Habits", "James Clear")
library.add_book("Deep Work", "Cal Newport")

library.view_books()

print("\n-- Issue --")

library.issue_book(1)

library.view_books()

print("\n-- Return --")

library.return_book(1)

print("\n-- Remove --")

library.remove_book(2)

library.view_books()