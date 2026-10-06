import os 
from prettytable import PrettyTable
import pwinput

data_matkul = {
    "pti" : {
        "nama" : "Pengantar Teknologi Informasi",
        "dosen" : "dosen_pti"
    },
    "ksi" : {
        "nama" : "Konsep Sistem Informasi",
        "dosen" : "dosen_ksi",
    },
    "dp" : {
        "nama" : "Dasar Pemrograman",
        "dosen" : "dosen_dp",
    },
    "panca" : {
        "nama" : "Pendidikan Pancasila", 
        "dosen" : "dosen_panca",
    },
    "matdis" : {
        "nama" : "Matematika Diskrit",
        "dosen" : "dosen_matdis",
    },
    "basing" : {
        "nama" : "Bahasa Inggris",
        "dosen" : "dosen_basing"
    }
}

data_soal = {
    "pti" : [],
    "ksi" : [],
    "dp" : [],        
    "panca" : [],
    "matdis" : [],
    "basing" : []
}

akun_dosen = {
    "dosen_pti" : "pti012",
    "dosen_ksi" : "ksi023",
    "dosen_dp" : "dp034",
    "dosen_panca" : "panca045",
    "dosen_matdis" : "matdis056",
    "dosen_basing" : "basing067"    
}

akun_mahasiswa = {
    "2609116011" : "mhs001",
    "2609116012" : "mhs002",
    "2609116013" : "mhs003",
    "2609116014" : "mhs004",
    "2609116015" : "mhs005",
}

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda() : 
    input("\nTekan enter untuk kembali ke menu...")

def validasi_menu(pesan, pilihan_valid) : 
    while True : 
        pilihan = input(pesan)
        if pilihan in pilihan_valid : 
            return pilihan 
        print ("Pilihan tidak valid!")

def validasi_nomor (pesan, jumlah) : 
    pilihan_valid = []
    for i in range(1, jumlah + 1) : 
        pilihan_valid.append(str(i))
    while True : 
        nomor = input(pesan)
        if nomor in pilihan_valid : 
            return int(nomor) - 1
        print("Nomor tidak valid!")

def input_kunci() : 
    while True : 
        kunci = input("Kunci jawaban A/B/C/D : ").upper()
        if kunci == "A" : 
            return kunci
        elif kunci == "B" :
            return kunci
        elif kunci == "C" :
            return kunci
        elif kunci == "D" :
            return kunci
        else:
            print("Kunci tidak valid")

def tampilkan_soal (kode) : 
    print("\n=======================================================")
    print("DAFTAR SOAL")
    print(data_matkul[kode]["nama"])
    print("========================================================")

    if len(data_soal[kode]) == 0 :
        print("Belum ada soal")
    else : 
        tabel = PrettyTable()
        tabel.field_names = [
            "No",
            "Pertanyaan",
            "A", 
            "B",
            "C",
            "D",
            "Kunci"
        ]

        nomor = 1
        for soal in data_soal[kode] : 
            tabel.add_row([
                nomor,
                soal[0],
                soal[1],
                soal[2],
                soal[3],    
                soal[4],
                soal[5] 
            ])
            nomor = nomor + 1
        print(tabel)

def tampilkan_soal_mahasiswa(kode) : 
    print("\n=======================================================")
    print("DAFTAR SOAL")
    print(data_matkul[kode]["nama"])
    print("========================================================")

    if len(data_soal[kode]) == 0:
        print("Belum ada soal")
    else:
        tabel = PrettyTable()

        tabel.field_names = [
            "No",
            "Pertanyaan",
            "A",
            "B",
            "C",
            "D"
        ]
        nomor = 1

        for soal in data_soal[kode] : 
            tabel.add_row([
                nomor,
                soal[0],
                soal[1],
                soal[2],
                soal[3],
                soal[4]
            ])
            nomor = nomor + 1
        print(tabel)

def tambah_soal(kode) : 
    print("\n=======================================================")
    print("TAMBAH SOAL")
    print("========================================================")

    pertanyaan = input("Pertanyaan : ")
    opsi_a = input("Opsi A : ")
    opsi_b = input("Opsi B : ")
    opsi_c = input("Opsi C : ")
    opsi_d = input("Opsi D : ")
    kunci = input_kunci()

    soal_baru = (
        pertanyaan,
        opsi_a,
        opsi_b,
        opsi_c,
        opsi_d,
        kunci
    )
    data_soal[kode].append(soal_baru)
    print("\nSoal berhasil ditambahkan!")

def ubah_soal(kode):
    if len(data_soal[kode]) == 0:
        print("\nBelum ada soal")
    else:
        tampilkan_soal(kode)

        nomor = validasi_nomor(
            "\nMasukkan nomor soal yang ingin diubah: ",
            len(data_soal[kode])
        )

        print("\nMasukkan data soal baru.")

        pertanyaan = input("Pertanyaan baru: ")
        opsi_a = input("Opsi A baru: ")
        opsi_b = input("Opsi B baru: ")
        opsi_c = input("Opsi C baru: ")
        opsi_d = input("Opsi D baru: ")

        kunci = input_kunci()

        soal_baru = (
            pertanyaan,
            opsi_a,
            opsi_b,
            opsi_c,
            opsi_d,
            kunci
        )

        data_soal[kode][nomor] = soal_baru

        print("\nSoal berhasil diubah!")

def hapus_soal(kode):
    if len(data_soal[kode]) == 0:
        print("\nBelum ada soal.")
    else:
        tampilkan_soal(kode)

        nomor = validasi_nomor(
            "\nMasukkan nomor soal yang ingin dihapus: ",
            len(data_soal[kode])
        )

        del data_soal[kode][nomor]

        print("\nSoal berhasil dihapus!")

def pilih_matkul():
    while True:
        print("\n==============================================")
        print("PILIH MATA KULIAH")
        print("==============================================")
        print("1. Pengantar Teknologi Informasi")
        print("2. Konsep Sistem Informasi")
        print("3. Dasar Pemrograman")
        print("4. Pendidikan Pancasila")
        print("5. Matematika Diskrit")
        print("6. Bahasa Inggris")
        print("==============================================")

        pilihan = input("Pilih mata kuliah: ")

        if pilihan == "1":
            return "pti"
        elif pilihan == "2":
            return "ksi"
        elif pilihan == "3":
            return "dp"
        elif pilihan == "4":
            return "panca"
        elif pilihan == "5":
            return "matdis"
        elif pilihan == "6":
            return "basing"
        else:
            print("Pilihan tidak valid!")

def menu_dosen(username):
    kode_matkul = ""

    for kode in data_matkul:
        if data_matkul[kode]["dosen"] == username:
            kode_matkul = kode

    while True:
        bersihkan_layar()

        print("\n==============================================")
        print("                  MENU DOSEN")
        print("==============================================")
        print("Mata Kuliah :", data_matkul[kode_matkul]["nama"])
        print("----------------------------------------------")
        print("1. Lihat Soal")
        print("2. Tambah Soal")
        print("3. Ubah Soal")
        print("4. Hapus Soal")
        print("5. Logout")
        print("==============================================")

        pilihan = validasi_menu(
            "Pilih menu: ",
            ["1", "2", "3", "4", "5"]
        )

        if pilihan == "1":
            tampilkan_soal(kode_matkul)
            jeda()

        elif pilihan == "2":
            tambah_soal(kode_matkul)
            jeda()

        elif pilihan == "3":
            ubah_soal(kode_matkul)
            jeda()

        elif pilihan == "4":
            hapus_soal(kode_matkul)
            jeda()

        elif pilihan == "5":
            print("\nLogout berhasil!")
            break


def kerjakan_soal(kode):
    if len(data_soal[kode]) == 0:
        print("\nBelum ada soal untuk mata kuliah ini.")
    else:
        skor = 0

        print("\n==============================================")
        print("                  MULAI KUIS")
        print("==============================================")

        nomor = 1

        for soal in data_soal[kode]:
            print("\n" + str(nomor) + ". " + soal[0])
            print("A. " + soal[1])
            print("B. " + soal[2])
            print("C. " + soal[3])
            print("D. " + soal[4])

            jawaban = input_kunci()

            if jawaban == soal[5]:
                print("Jawaban benar!")
                skor = skor + 1
            else:
                print("Jawaban salah!")

            nomor = nomor + 1

        print("\n==============================================")
        print("                 KUIS SELESAI")
        print("==============================================")
        print("Skor akhir:", str(skor) + "/" + str(len(data_soal[kode])))


def menu_mahasiswa(nim):
    while True:
        bersihkan_layar()

        print("\n==============================================")
        print("               MENU MAHASISWA")
        print("==============================================")
        print("NIM :", nim)
        print("----------------------------------------------")
        print("1. Lihat Soal")
        print("2. Kerjakan Kuis")
        print("3. Logout")
        print("==============================================")

        pilihan = validasi_menu(
            "Pilih menu: ",
            ["1", "2", "3"]
        )

        if pilihan == "1":
            kode = pilih_matkul()
            tampilkan_soal_mahasiswa(kode)
            jeda()

        elif pilihan == "2":
            kode = pilih_matkul()
            kerjakan_soal(kode)
            jeda()

        elif pilihan == "3":
            print("\nLogout berhasil!")
            break


def login_dosen():
    bersihkan_layar()

    print("\n==============================================")
    print("                 LOGIN DOSEN")
    print("==============================================")

    username = input("Username: ")
    password = pwinput.pwinput("Password: ")

    if username in akun_dosen:
        if akun_dosen[username] == password:
            print("\nLogin dosen berhasil!")
            jeda()
            menu_dosen(username)
        else:
            print("\nPassword salah!")
            jeda()
    else:
        print("\nUsername tidak ditemukan!")
        jeda()


def login_mahasiswa():
    bersihkan_layar()

    print("\n==============================================")
    print("              LOGIN MAHASISWA")
    print("==============================================")

    nim = input("NIM: ")
    password = pwinput.pwinput("Password: ")

    if nim in akun_mahasiswa:
        if akun_mahasiswa[nim] == password:
            print("\nLogin mahasiswa berhasil!")
            jeda()
            menu_mahasiswa(nim)
        else:
            print("\nPassword salah!")
            jeda()
    else:
        print("\nNIM tidak ditemukan!")
        jeda()


def main():
    while True:
        bersihkan_layar()

        print("\n==============================================")
        print("            SISTEM BANKSOAL HUB")
        print("==============================================")
        print("1. Login Dosen")
        print("2. Login Mahasiswa")
        print("3. Keluar")
        print("==============================================")

        pilihan = validasi_menu(
            "Pilih menu: ",
            ["1", "2", "3"]
        )

        if pilihan == "1":
            login_dosen()

        elif pilihan == "2":
            login_mahasiswa()

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan")
            print("Sistem Banksoal Hub!")
            break

main()
