import os
import json
from models.film import Film

class FilmService:
    def __init__(self):
        self.films = []
        self.next_id = 1
    
    
    def add_film(self, title, genre):
        film = Film(self.next_id, title, genre)
        self.films.append(film)
        self.next_id += 1


    def list_films(self):
        for film in self.films:
            print(film)
    
    
    def find_film_by_id(self, id):
        for film in self.films:
            if film.id == id:
                return film
        return None     
    
    
    def save_to_file(self, filename="films.json"):
        with open(filename, "w") as f:
            json.dump([film.to_dict() for film in self.films], f)


    def load_from_file(self, filename="films.json"):
        if not os.path.exists(filename):
            # File tidak ada, anggap data kosong
            self.films = []
            return

        with open(filename, "r") as f:
            content = f.read().strip()
            if not content:
                # File kosong, anggap data kosong
                self.films = []
                return

            try:
                data = json.loads(content)
                self.films = [Film(**d) for d in data]
                self.next_id = max(film.id for film in self.films) + 1 if self.films else 1
            except json.JSONDecodeError:
                print(f"File '{filename}' tidak berisi JSON yang valid.")
                self.films = []