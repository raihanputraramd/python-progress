class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

    
    def borrow(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
        else:
            print(f"Buku '{book.title}' Sedang dipinjam orang lain")
    

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
    
    def __str__(self):
        return f"{self.id}. {self.name}"