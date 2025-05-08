from services.book_service import BookService
from services.member_service import MemberService

# Inisialisasi Service
book_service = BookService()
member_service = MemberService()

# Tambah Buku
book_service.add_book("Python Dasar", "Asep")
book_service.add_book("Flask untuk pemula", "Nanda")

# Tambah Member
member_service.add_member("Budi")
member_service.add_member("Siti")

# Pinjam buku
member = member_service.find_member_by_id(1)
book = book_service.find_book_by_id(1)
member.borrow(book)

# Cetak data anggota dan pinjaman
print("\nDaftar Anggota:")
for m in member_service.members:
    print(m)
    print("  Buku Dipinjam:")
    for b in m.borrowed_books:
        print("    -", b.title)

# Cetak daftar buku
print("\nDaftar Buku:")
book_service.list_books()