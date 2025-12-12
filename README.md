# Pelanggaran SRP, OCP, dan DIP Pada Kode Sebelum Refactoring
1. Pelanggaran SRP: Satu class memiliki beberapa fungsi yang memiliki tugas yang berbeda, Satu class memiliki beban banyak fungsi.
2. Pelanggaran OCP: Penambahan fitur lebih menjadi modifikasi class utama dengan menambahkan elif, Tidak hanya memperbanyak penulisan kode tetapi juga membuat penambahan fitur menjadi sesuatu yang susah dikelola dan susah dibaca.
3. Pelanggaran DIP: Penyimpanan database terlalu kaku pada satu class dengan implementasi konkret tanpa adanya abstraksi, Ini dapat mengakibatkan pembeda logika yang agak membingungkan untuk dipelihara dan dipahami. Takutnya akan terjadi kesalahan logika jika aksi bentrok dengan aksi lain yang terkait dengan fungsi.
