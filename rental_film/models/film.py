class Film:
    def __init__(self, id, title, genre):
        self.id = id
        self.title = title
        self.genre = genre
        self.is_rented = False
    
    
    def __str__(self):
        status = "Tersedia" if self.is_rented else "Disewa"
        return f"{self.id} - {self.title} - {self.genre} [{status}]"
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "is_rented": self.is_rented
        }
    
    @staticmethod
    def from_dict(data):
        film = Film(data["id"], data["title"], data["genre"])
        film.is_rented = data["is_rented"]
        return film