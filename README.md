# Minpro-2-DDP-SistemBanksoalHub-MultiAdminPanel
Nama : Debora Lintang Apsari | NIM : 2609116011 | Prodi : Sistem Informasi (A)

# Penjelasan Singkat Sistem Banksoal Hub-Multi Admin Panel
Sistem Banksoal Hub merupakan program berbasis Python yang digunakan untuk mengelola dan mengerjakan soal berdasarkan mata kuliah.

Program memiliki dua jenis pengguna, yaitu:

`Dosen` — dapat melihat, menambah, mengubah, dan menghapus soal. <br>
`Mahasiswa` — dapat melihat soal dan mengerjakan kuis.

Program menggunakan login dengan username/NIM dan password serta dilengkapi validasi input agar pilihan yang tidak sesuai dapat ditangani tanpa menghentikan program.

Sementara itu, Mahasiswa dapat melihat soal dan mengerjakan kuis untuk mendapatkan skor.
Program menggunakan sistem login berdasarkan username/NIM dan password serta menyediakan validasi input agar pilihan yang tidak sesuai tidak langsung menyebabkan program berhenti.

# Flowchart <br>
Berikut merupakan flowchart dari Sistem Banksoal Hub: <br>
<img width="2000" alt="Flowchart Sistem Banksoal Hub" src="https://github.com/user-attachments/assets/2dd13902-b451-4d62-89e6-a237bcd980f7" />

*Fitur Program :* <br>
*- Dosen*
1. Login menggunakan username dan password
2. Melihat soal
3. Menambah soal
4. Mengubah soal
5. Menghapus soal
6. Logout <br>

*- Mahasiswa*
1. Login menggunakan NIM dan password
2. Melihat soal
3. Mengerjakan kuis
4. Melihat skor
5. Logout

# Dokumentasi kode program & output 
**1. Menu Utama** <br>
<img width="434" height="168" alt="Screenshot 2026-10-06 164050" src="https://github.com/user-attachments/assets/061ef456-f04a-4e2b-9ddd-adcd602f6f44" /> <br>

Menu utama merupakan halaman awal Sistem Banksoal Hub. Pengguna dapat memilih untuk masuk sebagai Dosen, masuk sebagai Mahasiswa, atau Keluar dari program. <br>

**2. Login Dosen** <br>
<img width="424" height="132" alt="Screenshot 2026-10-06 164450" src="https://github.com/user-attachments/assets/f6df35ba-99ce-45d0-b8e5-90556f8498cc" /> <br>

Output kode diatas adalah apabila dosen salah memasukkan password dan dosen akan diminta untuk menekan tombol enter untuk kembali ke menu utama. <br>

<img width="425" height="144" alt="image" src="https://github.com/user-attachments/assets/9c61e1fe-5b39-4829-bd4d-26e524627464" /> <br>

Output kode diatas adalah apabila dosen salah memasukkan username dan dosen akan diminta untuk menekan tombol enter untuk kembali ke menu utama. <br>

<img width="425" height="131" alt="Screenshot 2026-10-06 164737" src="https://github.com/user-attachments/assets/4253a413-9b0e-43f2-8aa1-73582b7d7380" /> <br>

Output kode diatas adalah apabila dosen memasukkan username dan password dengan benar dan akan lanjut ke menu dosen, disini saya menggunakan username dosen_pti dan password pti012 sebagai contoh. <br>

**3. Menu Login** <br>
<img width="436" height="185" alt="image" src="https://github.com/user-attachments/assets/d3f3010f-e87b-46b0-8172-769af00fa4ae" /> <br>

Output diatas menampilkan menu login dosen, lalu dosen akan memilih menu yang ada. <br>

`If dosen pilih menu == 1` <br>

<img width="434" height="296" alt="Screenshot 2026-10-06 170346" src="https://github.com/user-attachments/assets/cc047ebb-cf6b-4035-a708-8f6138ae829f" /> <br>

Disini saya mencontohkan apabila dosen memilih menu 1 dan dalam keadaan soal belum ter-input, maka kita perlu melakukan tambah soal terlebih dahulu, maka dosen akan lanjut memilih menu 2 untuk menambahkan soal, dosen hanya perlu menekan tombol enter untuk kembali ke menu dosen. <br>

`if dosen pilih menu == 2` <br>

<img width="526" height="336" alt="image" src="https://github.com/user-attachments/assets/207f2cdc-ef78-400b-a21b-1e1487de93d0" /> <br>

Output diatas adalah apabila dosen memilih menu 2 yaitu menambahkan soal, dosen akan diminta untuk memasukkan pertanyaan, jawaban A,B,C,D serta kunci jawaban, disini saya akan mencoba untuk menambahkan 3 soal. <br>

Kita coba untuk kembali ke menu pertama yaitu lihat soal versi soal yang sudah di tambahkan melalui menu 2 <br>

`if dosen pilih menu == 1` <br>

<img width="650" height="227" alt="Screenshot 2026-10-06 172717" src="https://github.com/user-attachments/assets/54417df4-4d65-4ef4-b855-71523f26f2a7" /> <br>

Output program diatas adalah contoh penggunaan PrettyTabel. <br>

`if dosen pilih menu == 3` <br>

<img width="676" height="385" alt="Screenshot 2026-10-06 173301" src="https://github.com/user-attachments/assets/26a93679-f255-4c1c-89e0-22fd6c851c00" />

Saat dosen memilih menu 3 maka program akan meminta dosen memilih nomor berapa yang ingin diubah, pada contoh diatas saya menggunakan contoh mengubah soal no 2. Dan jika sudah, dosen hanya perlu menekan tombol enter untuk kembali ke menu dosen.

`if dosen memilih menu == 4` <br>

<img width="670" height="273" alt="image" src="https://github.com/user-attachments/assets/6b13ac63-f6b5-47c5-8801-4df68547597c" /> <br>

Output program diatas adalah contoh dalam menghapus soal, disini saya mencontohkan untuk menghapuskan soal nomor 3. <br>

`if dosen memilih menu == 5` <br>
<img width="293" height="185" alt="image" src="https://github.com/user-attachments/assets/9b98772b-ab6b-4f85-bc45-8b731c3cb283" /> <br>

Pada output diatas, program akan menampilkan "logout berhasil" namun tidak dapat saya perlihatkan pada dokumentasi dikarenakan dia akan ter-clear otomatis dengan fungsi os. <br>
<br>

**4. Login Mahasiswa** <br>

<img width="280" height="167" alt="image" src="https://github.com/user-attachments/assets/8a0fe71f-81b0-4e14-a30d-1ccce023973c" /> <br>

Output diatas adalah apabila mahasiswa salah memasukkan NIM atau ada NIM yang belum ter-input, disini saya memasukkan 5 NIM saja di dalam program, disini mahasiswa hanya perlu menekan tombol enter untuk kembali ke menu utama

<img width="283" height="176" alt="image" src="https://github.com/user-attachments/assets/2e4da753-db1c-4873-9142-cd80b2d03d50" /> <br>

Output diatas adalah apabila mahasiswa salah memasukkan password, lalu mahasiswa akan diarahkan untuk menekan tombol enter dan akan otomatis kembali ke menu utama 

<img width="278" height="143" alt="image" src="https://github.com/user-attachments/assets/9a7ee53d-ab0e-49fb-b963-da3fbeb0e714" /> <br>

Output diatas adalah apabila mahasiswa memasukkan NIM dan password dengan benar, dengan menekan tombol enter maka mahasiswa akan di arahkan ke menu mahasiswa

**5. Menu Mahasiswa** <br>

`if mahasiswa pilih menu == 1` <br>

<img width="595" height="377" alt="Screenshot 2026-10-06 180028" src="https://github.com/user-attachments/assets/42a35b3e-ce57-4377-8b92-6b31ceb5d72c" /> <br>

Output diatas adalah saat mahasiswa memilih menu lihat soal, dan sebelumnya dosen telah menambahkan soal, jadi soal sudah bisa di akses, bedanya dengan menu dosen adalah, dosen memiliki kunci jawaban, sedangkan mahasiswa tidak. <br>

`if mahasiswa pilih menu == 2` <br>
<img width="286" height="424" alt="image" src="https://github.com/user-attachments/assets/21d56d26-a41b-4330-895e-deb0649c63d6" /> <br>

Output diatas adalah saat mahasiswa memilih menu kerjakan kuis, dan setelah kuis dikerjakan, program akan menampilkan skor penilaian dari apa yang sudah dikerjakan oleh mahasiswa.

`if mahasiswa pilih menu == 3` <br>
<img width="274" height="185" alt="image" src="https://github.com/user-attachments/assets/bda0b6c6-12ff-479a-9871-b9c284d6d355" /><br>

Output diatas adalah saat mahasiswa ingin logout, program akan menampilkan kata `logout berhasil `, tetapi pada dokumentasi tidak dapat terlihat dikarenakan fitur os yang ada di program <br>


**6. Menu Keluar** <br>
<img width="404" height="188" alt="Screenshot 2026-10-06 180747" src="https://github.com/user-attachments/assets/a687585e-d983-4900-9e6f-51d9e7628854" /> <br>

Pada saat user (mahasiswa/dosen) memilih menu ke 3 yaitu keluar, maka program akan menampilkan seperti dokumentasi diatas.

# Penjelasan Penerapan validasi input & penggunaan library 
**1. Validasi Input -> Menggunakan error handling** <br>

Program ini sudah ada validasi input. Jadi kalau pengguna salah memasukkan pilihan, program tidak langsung berhenti, tetapi akan muncul pesan “Pilihan tidak valid!” dan pengguna bisa memasukkan pilihan lagi. <br>

`Kode Program :`  <br>

<img width="326" height="248" alt="image" src="https://github.com/user-attachments/assets/23cb4fb3-04b1-4e1d-a050-5cbe8f2a4284" /> <br>

`contoh output` <br>

<img width="270" height="161" alt="image" src="https://github.com/user-attachments/assets/fd7d4bbc-8a86-4c16-8544-1bf72a62aebf" /> <br>

atau <br>

<img width="487" height="199" alt="image" src="https://github.com/user-attachments/assets/ace390e5-2c18-4911-9ef9-e9a38d539179" /> <br>

**2. Penggunaan Library** <br>

Disini saya menggunakan 3 library 
- os
- PrettyTabel
- pwinput

`kode` <br>

<img width="248" height="56" alt="image" src="https://github.com/user-attachments/assets/a161aadf-bcbc-493b-9c9d-efbfb789bf8f" /> <br>

os digunakan untuk membersihkan tampilan terminal. <br>
PrettyTable digunakan untuk menampilkan daftar soal dalam bentuk tabel. <br>
pwinput digunakan untuk menyembunyikan password saat proses login. <br>












































