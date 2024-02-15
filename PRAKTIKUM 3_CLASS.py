'''Basic'''
# class Siswa:
#     jumlah = 0
#     def __init__(self,nama,nilai):
#         # instance variable
#         self.nama = nama
#         self.nilai= nilai
#         Siswa.jumlah += 1
    
#     def kelulusan(self,nama_siswa,nilai_siswa) :
#         if nilai_siswa >= 70 :
#             print(f"{nama_siswa} LULUS")
#         else :
#             print(f"{nama_siswa} TIDAK LULUS")

# agus = Siswa('Agus',75)
# vincen = Siswa("Vincen", 65)

# agus.kelulusan(agus.nama,agus.nilai)
# vincen.kelulusan(vincen.nama,vincen.nilai)
# print(f'Jumlah Siswa : {Siswa.jumlah}')

# '''Encasulaption'''
# class Siswa:
#     jumlah = 0
#     def __init__(self,nama,nilai):
#         # instance variable
#         self.__nama = nama
#         self.__nilai= nilai
#         Siswa.jumlah += 1

#     def getName(self):
#         return self.__nama
#     def getValue(self):
#         return self.__nilai
#     def changeValue(self,nilai_baru) :
#         self.__nilai = nilai_baru

#     def kelulusan(self,nama_siswa,nilai_siswa) :
#         if nilai_siswa >= 70 :
#             print(f"{nama_siswa} LULUS dengan nilai {nilai_siswa}")
#         else :
#             print(f"{nama_siswa} TIDAK LULUS dengan nilai {nilai_siswa}")

# agus = Siswa('Agus',75)
# vincen = Siswa("Vincen", 65)

# input_decision = input("Apakah ingin mengubah nilai Vincen?y/n : ")
# if  input_decision.lower() == 'y' :
#     new_value = int(input("Masukkan nilai baru : "))
#     vincen.changeValue(new_value)
# else :
#     pass

# agus.kelulusan(agus.getName(),agus.getValue())
# vincen.kelulusan(vincen.getName(),vincen.getValue())
# print(f'Jumlah Siswa : {Siswa.jumlah}')

'''Inheritance'''
class Sekolah :
    def __init__(self,jenjang,nama_sekolah):
        self.jenjang = jenjang
        self.nama_sekolah = nama_sekolah

class Kelas(Sekolah) :
    def __init__(self,jenjang,nama_sekolah,jenis_kelas,nama_kelas):
        super().__init__(jenjang,nama_sekolah)
        self.jenis_kelas = jenis_kelas
        self.nama_kelas = nama_kelas
    
class Siswa(Kelas) :
    def __init__(self,jenjang,nama_sekolah,jenis_kelas,nama_kelas,nama_siswa,nilai):
        super().__init__(jenjang,nama_sekolah,jenis_kelas,nama_kelas)
        self.__nama_siswa= nama_siswa
        self.__nilai = nilai
    def getName(self):
        return self.__nama_siswa
    def getValue(self):
        return self.__nilai
    def changeValue(self,nilai_baru) :
        self.__nilai = nilai_baru

    def Kelulusan(self) :
        return self.__nilai >= 70
        
agus = Siswa('SMA',"Brawijaya","Mipa","6","Agus",80 )
vincen = Siswa('SMA',"Raden","IPS","1","Vincen",65 )

input_decision = input("Apakah ingin mengubah nilai Vincen?y/n : ")
if  input_decision.lower() == 'y' :
    new_value = int(input("Masukkan nilai baru : "))
    vincen.changeValue(new_value)
else :
    pass

lulus_agus = agus.Kelulusan()
lulus_vincen = vincen.Kelulusan()
for i,x in zip([lulus_agus,lulus_vincen],[agus,vincen]) :
    if i:
        print(f"{x.getName()} bersekolah di {x.jenjang} {x.nama_sekolah}, berada di kelas {x.jenis_kelas} {x.nama_kelas} dan lulus dengan nilai {x.getValue()} ")
    else :
        print(f"{x.getName()} bersekolah di {x.jenjang} {x.nama_sekolah}, berada di kelas {x.jenis_kelas} {x.nama_kelas} dan tidak lulus dengan nilai {x.getValue()} ")


