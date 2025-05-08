from services.film_service import FilmService
from services.customer_service import CustomerService

# Inisialisasi Service
film_service = FilmService()
customer_service = CustomerService()

# Load data
film_service.load_from_file()
customer_service.load_from_file(film_service.films)

# Buat film
film_service.add_film("Inception", "Sci-Fi")
film_service.add_film("Titanic", "Romance")

# Buat Pelanggan
customer_service.add_customer("Andi")
customer_service.add_customer("Rina")

# Meminjam Film
customer = customer_service.find_customer_by_id(1)
film = film_service.find_film_by_id(1)
customer.rent(film)


# Daftar Pelanggan
print(f"\nDaftar Pelanggan")
for customer in customer_service.customers:
    print(customer)
    print("Film Disewa")
    for film in customer.rented_films:
        print("     -", film.title)


# Cetak Daftar Pelanggan
print("\nDaftar Film")
film_service.list_films()


# Simpan data
film_service.save_to_file()
customer_service.save_to_file()