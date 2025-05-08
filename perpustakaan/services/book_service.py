from models.book import Book

class BookService:
    def __init__(self):
        self.books = []
        self.next_id = 1


    def add_book(self, title, author):
        book = Book(self.next_id, title, author)
        self.books.append(book)
        self.next_id += 1


    def list_books(self):
        for book in self.books:
            print(book)
    

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None