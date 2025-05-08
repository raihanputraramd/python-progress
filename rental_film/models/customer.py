class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rented_films = []
 
    
    def rent(self, film):
        if film.is_rented:
            self.rented_films.append(film)
        else:
            print("Film '{film.name}' Sedang dipinjam oleh orang lain")
    
    
    def return_film(self, film):
        if not film.is_rented:
            self.rented_films.append(film)
            film.is_rented = True
        else:
            print(f"Film '{film.title}' sedang dipinjam orang lain.")
    
    
    def __str__(self):
        return f"{self.id} - {self.name}"
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rented_film_ids": [film.id for film in self.rented_films]
        }

    @staticmethod
    def from_dict(data, films_lookup):
        customer = Customer(data["id"], data["name"])
        customer.rented_films = [films_lookup[fid] for fid in data["rented_film_ids"] if fid in films_lookup]
        return customer