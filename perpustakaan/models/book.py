class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = True

    
    def __str__(self):
        status = "Tersedia" if self.is_available else "Dipinjam"
        return f"{self.id} - {self.title} - {self.author} [{status}]"