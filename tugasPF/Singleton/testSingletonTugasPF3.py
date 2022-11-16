from Singleton import MahasiswaITK

mahasiswa = MahasiswaITK.getInstance()
dosen = MahasiswaITK.getInstance()

mahasiswa.bayarUKT = "Pembayaran UKT Semester 7"
mahasiswa.nim = 11191064

dosen.bayarUKT = "Dosen Tidak Bayar UKT"
dosen.nim = 0

print(mahasiswa.bayarUKT)
print(mahasiswa.nim)

#Hanya menerima satu instance