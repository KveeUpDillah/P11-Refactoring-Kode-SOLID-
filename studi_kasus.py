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

# Kode setelah refactoring
# Memisahkan class agar memenuhi SRP
from abc import ABC, abstractmethod

class MenuAction(ABC): 
    # Class interface abstraksi yang akan digunakan untuk class lain untuk pengelolaan
    @abstractmethod
    def execute(self, nama1=None, nama2=None, harga=None):
        pass

# Class yang menyimpan nama menu dan digunakan semua aksi
class MenuStorage:
    def __init__(self):
        self.menu = {}   # Diisi dengan dictionary {"nama": harga}

    def tambah_menu(self, nama, harga):
        self.menu[nama] = harga

    def edit_nama(self, nama_lama, nama_baru):
        if nama_lama in self.menu:
            self.menu[nama_baru] = self.menu.pop(nama_lama)
        else:
            print("Menu tidak ditemukan!")

    def tampilkan(self):
        if not self.menu:
            print("Belum ada menu.")
            return
        for nama, harga in self.menu.items():
            print(f"{nama} - {harga}")

# Class aksi untuk pengelolaan menu cafe yang memenuhi OCP
# (Tinggal tambah class baru untuk menambah fitur tanpa mengubah class lain)
class AddMenuAction(MenuAction): 
    # Aksi untuk menambah menu
    def __init__(self, storage):
        self.storage = storage

    def execute(self, nama1=None, nama2=None, harga=None):
        self.storage.tambah_menu(nama1, harga)
        print(f"Menu {nama1} ditambahkan dengan harga {harga}")
        print("Menyimpan ke database (simulasi)")

class ShowMenuAction(MenuAction): 
    # Aksi untuk menampilkan menu
    def __init__(self, storage):
        self.storage = storage

    def execute(self, nama1=None, nama2=None, harga=None):
        print("Menampilkan semua menu")
        self.storage.tampilkan()

# Class registrasi aksi yang terdaftar dengan interface "MenuAction"
class ActionRegistry:
    def __init__(self):
        self._actions = {}

    def register(self, key, factory):
        self._actions[key] = factory

    def get_action(self, key):
        if key not in self._actions:
            raise ValueError("Aksi tidak terdaftar")
        return self._actions[key]()   # panggil factory

# Modul High level yang bergantung pada interface (DIP)
# Kelas koordinator
class Cafe: 
    # Class mengeksekusi aksi
    def __init__(self, registry: ActionRegistry):   # Dependency Injection
        self.registry = registry

    def kelola_menu(self, aksi, nama1=None, nama2=None, harga=None):
        menu_action = self.registry.get_action(aksi)
        menu_action.execute(nama1, nama2, harga)

# Inisialisasi penyimpanan
storage = MenuStorage()

# Buat registry dan daftar aksi
registry = ActionRegistry()
registry.register("tambah", lambda: AddMenuAction(storage))
registry.register("tampil", lambda: ShowMenuAction(storage))
registry.register("edit",   lambda: EditMenuAction(storage))   # fitur baru

# Injeksi ke Cafe
cafe = Cafe(registry)

# Tambah menu
cafe.kelola_menu("tambah", nama1="Latte", harga=20000)
cafe.kelola_menu("tambah", nama1="Espresso", harga=15000)

class EditMenuAction(MenuAction):
    # Aksi untuk mengedit nama menu (FITUR BARU)
    def __init__(self, storage: MenuStorage):
        self.storage = storage

    def execute(self, nama1=None, nama2=None, harga=None):
        print(f"Mengubah nama menu '{nama1}' menjadi '{nama2}'")
        self.storage.edit_nama(nama1, nama2)

# Edit menu (FITUR BARU)
cafe.kelola_menu("edit", nama1="Latte", nama2="Magic Latte")

# Tampilkan menu
cafe.kelola_menu("tampil")