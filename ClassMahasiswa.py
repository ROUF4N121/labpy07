class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nim, nilai):
        self.data_mahasiswa.append({
            'nama': nama,
            'nim': nim,
            'nilai': nilai
        })
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            print("================================")
            for idx, mhs in enumerate(self.data_mahasiswa, start=1):
                print(f"{idx}. Nama: {mhs['nama']}, NIM: {mhs['nim']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                self.data_mahasiswa.remove(mhs)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                nim = input("Masukkan NIM baru (tekan Enter jika tidak ingin mengubah): ")
                nilai = input("Masukkan nilai baru (tekan Enter jika tidak ingin mengubah): ")
                if nim:
                    mhs['nim'] = nim
                if nilai:
                    try:
                        mhs['nilai'] = int(nilai)
                    except ValueError:
                        print("Nilai harus berupa angka. Data tidak diubah.")
                print(f"Data mahasiswa {nama} berhasil diubah.")
                return
        print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")


if __name__ == "__main__":
    daftar_nilai = DaftarNilaiMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah data mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Hapus data mahasiswa")
        print("4. Ubah data mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nim = input("Masukkan NIM: ")
            try:
                nilai = int(input("Masukkan nilai: "))
                daftar_nilai.tambah(nama, nim, nilai)
            except ValueError:
                print("Nilai harus berupa angka. Data tidak ditambahkan.")
        
        elif pilihan == "2":
            daftar_nilai.tampilkan()

        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            daftar_nilai.hapus(nama)

        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            daftar_nilai.ubah(nama)

        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
