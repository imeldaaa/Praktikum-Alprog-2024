def nilai_siswa() :
    global dict_siswa,input_siswa_baru,input_nilai_baru
    dict_siswa = {"Anji" :65,"Faris" :75,"Dita" :85}
    print(f"Daftar nilai siswa sekarang : {dict_siswa}")
    while True:
        input_decision = input("Apakah ingin menambah data siswa?(y/n) : ").lower()
        if input_decision == "y":
            while True:
                input_siswa_baru = input("Masukan nama siswa : ")
                if input_siswa_baru.isalpha() :
                    while True :
                        input_nilai_baru = input("Masukan nilai siswa : ")
                        try :
                            input_nilai_baru = int(input_nilai_baru)
                            break
                        except ValueError :
                            print("Input harus berupa angka!")
                    break
                else:
                    print("Input harus alfabet!")
        elif input_decision == "n":
            break
        else:
            print("Mohon masukkan y/n!")
    
    try :
        print(f"{daftar_baru()}")
    except NameError :
        print("Program selesai, terimakasih sudah menggunakan program ini!") 
    
def jumlah_siswa():
    return len(dict_siswa)

def daftar_baru() :
    return f"Berikut merupakan daftar baru nilai siswa {sorting_daftar(input_siswa_baru,input_nilai_baru)} dengan jumlah siswa sebanyak {jumlah_siswa()}"

def sorting_daftar(nama_baru,nilai_baru) :
    dict_siswa.update({nama_baru : nilai_baru})
    sorted_dict_daftar_baru = dict(sorted(dict_siswa.items()))
    return sorted_dict_daftar_baru
   
nilai_siswa()
