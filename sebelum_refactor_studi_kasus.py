# Kode yang melanggar SRP, OCP, dan DIP
# Melanggar SRP karena 1 class melakukan 3 tugas yaitu mengelola, menampilkan, dan menyimpan ke database
class Cafe:
    def kelola_menu(self, aksi, nama_menu, harga):
        if aksi == "tambah":
            print(f"Menu {nama_menu} ditambahkan dengan harga {harga}")
        # Melanggar OCP untuk penambahan fitur baru dan akan memberatkan banyak fitur dalam satu class
        elif aksi == "tampil":
            print("Menampilkan semua menu")
        # Melanggar DIP karena class langsung melakukan penyimpanan yang merupakan tindakan konkret tanpa abstraksi
        print("Menyimpan ke database")
