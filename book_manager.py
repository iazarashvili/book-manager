


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def show_all_books(self):
        if self.books:
            print("List of all books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print("No books in the list.")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print(f"Found {len(found_books)} book(s) with title '{title}':")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print(f"No books found with title '{title}'.")



