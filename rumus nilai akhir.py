print ("=========================================")
nama = (input ("Masukan Nama Anda : "))
kls = int (input ("masukan kelas anda : "))
daftar_hadir = input ("masukan Daftar Hadir Anda :")
tugassaya = int (input ("masukan tugas anda :"))
print ("Nilai Uas Anda Adalah 40 %")
print ("Nilai Absen Anda 20 %")
print ("Nilai Tugas Anda 10 %")
print ("Nilai Uts Anda 30 %")
uas = 0.4
absen = 0.2
tugas = 0.1
uts = 0.3
masukan = tugassaya * tugas
masukan2 = tugassaya * uas
masuk3 = tugassaya * absen
masukan4 = tugassaya * uts
nilaikeseluruhan = masukan + masukan2 + masukan4 + masuk3

print ("==========================================")
print ("nama anda adalah",nama)
print ("kelas anda sekarang",kls)
print ("Daftar Hadir Anda Adalah",daftar_hadir)
print ("Daftar Tugas Selesai Anda Adalah",tugassaya)
print ("Tugas : ",masukan)
print ("Uas : ",masukan2)
print ("Absen : ",masuk3)
print ("Uts : ",masukan4)
print (f"nilai akhir anda adalah : {nilaikeseluruhan}")


if nilaikeseluruhan >= 10.0 :
    print ("Selamat Anda Lulus")
else : 
    print ("Mohon Maaf Anda Tidak Lulus")