'''LOGIN'''
account = {"admin" :"123"}
coba = 0
while coba < 3 :
    username = input("Masukan username anda :")
    password = input("Masukan password anda :")
    if username in account and password==account[username] :
        print("Anda berhasil login")
        break
    elif coba==2 :
        print("Terminated")
        exit()
    else :
        print("Username atau password anda salah")
    coba+=1

'''DATA'''
iklan_fisik = []
iklan_digital = []
penjualan = []
list_target_penjualan = []
number_list = []

input_decision = "y"
while True :
    if input_decision == "y" :
        '''Input Manual'''
        print(f"Isi data dengan angka, jika sudah selesai ketik 'end'")
        print(f"Pengeluaran iklan satuannya RIBUAN, Penjualan satuannya BUAH")
        print(f'---------------------------------------------\n')

        i = 1
        while True :
            input_iklan_fisik = input(f"{i}.{'Data Pengeluaran Iklan Fisik (RP): ':<} ")
            try :
                if input_iklan_fisik=='end' :
                    break
                else :
                    input_iklan_fisik = int(input_iklan_fisik)
                    input_iklan_digital = int(input(f"{'Data Pengeluaran Iklan Digital (RP): ':>39}"))
                    input_penjualan = int(input(f"{'Data penjualan (BUAH): ':>25}"))
                    iklan_fisik.append(input_iklan_fisik)
                    iklan_digital.append(input_iklan_digital)
                    penjualan.append(input_penjualan)
                    i+=1   
            except ValueError :
                print("Input harus berupa angka")

        print(f"----------------------------------------------------------------------------------\n")
        print(f"|{'No':^6}|{'Pengeluaraan Iklan Fisik':^28}|{'Pengeluaraan Iklan Digital':^30}|{'Penjualan':^15}|")
        for a,(b,c,d) in enumerate(zip(iklan_fisik,iklan_digital,penjualan),start=1) :
            print(f"|{a:^6}|RP{b:^26,.2f}|RP{c:^28,.2f}|{d:^10,.0f} Buah|")

        '''Perhitungan'''
        # a. Data variabel 
        n = len(iklan_fisik)
        total_iklan_fisik = sum(iklan_fisik)
        total_iklan_digital = sum(iklan_digital)
        total_penjualan = sum(penjualan)

        iklan_fisik_kali_penjualan = []
        iklan_digital_kali_penjualan = []

        iklan_fisik_kuadrat = []
        iklan_digital_kuadrat = []
        penjualan_kuadrat= []

        total_k_iklan_fisik = total_iklan_fisik**2
        total_k_iklan_digital = total_iklan_digital**2
        total_k_penjualan = total_penjualan**2

        # b. Menghitung persamaan regresi
        for a,b,c in zip(iklan_fisik,penjualan,iklan_digital) :
        # 1) Iklan fisik-Penjualan
            ab = a*b
            kuadrat_a = a**2
            kuadrat_b= b**2

            iklan_fisik_kali_penjualan.append(ab)
            iklan_fisik_kuadrat.append(kuadrat_a)
            penjualan_kuadrat.append(kuadrat_b)

        # 2) Iklan digital-Penjualan
            cb = c*b
            kuadrat_c = c**2
            
            iklan_digital_kali_penjualan.append(cb)
            iklan_digital_kuadrat.append(kuadrat_c)

        # Perhitungan model Iklan Fisik
        sum_iklan_f_kali_p = sum(iklan_fisik_kali_penjualan)
        sum_iklan_fisik_kuadrat = sum(iklan_fisik_kuadrat)
        sum_penjualan_kuadrat = sum(penjualan_kuadrat)

        slope = ((n*sum_iklan_f_kali_p)-((total_iklan_fisik)*(total_penjualan)))/(n*(sum_iklan_fisik_kuadrat)-total_k_iklan_fisik)
        intercept = ((total_penjualan)-(slope*(total_iklan_fisik)))/n

         # Perhitungan model Iklan Digital
        sum_iklan_d_kali_p = sum(iklan_digital_kali_penjualan)
        sum_iklan_digital_kuadrat = sum(iklan_digital_kuadrat)

        slope2 = ((n*sum_iklan_d_kali_p)-((total_iklan_digital)*(total_penjualan)))/(n*(sum_iklan_digital_kuadrat)-total_k_iklan_digital)
        intercept2 = ((total_penjualan)-(slope2*(total_iklan_digital)))/n

        # c. Koefisien Determinasi
        penjualan_average = total_penjualan/n
        # Iklan fisik
        y_perkiraan = []
        # Iklan digital
        y_perkiraan2 = []

        for a,b in zip(iklan_fisik,iklan_digital) :
            # Iklan Fisik
            y_hitung = ((slope*a) + intercept)
            y_perkiraan.append(y_hitung)
            # Iklan Digital
            y_hitung2 = ((slope2*b) + intercept2)
            y_perkiraan2.append(y_hitung2)

        # Iklan Fisik
        ss_error1 = []
        ss_total1 = []
        # Iklan Digital
        ss_error2 = []

        for a,b,c in zip(penjualan,y_perkiraan,y_perkiraan2) :
            # Iklan fisik
            ss_error = (a-b)**2
            ss_error1.append(ss_error)
            # Iklan digital
            ss_error_2 = (a-c)**2
            ss_error2.append(ss_error_2)

            ss_total = (a-penjualan_average)**2
            ss_total1.append(ss_total)

        # Iklan fisik
        sum_ss_error = sum(ss_error1)
        sum_ss_total = sum(ss_total1)
        k_determinasi= 1-(sum_ss_error/sum_ss_total)

        # Iklan digital
        sum_ss_error2 = sum(ss_error2)
        k_determinasi2= 1-(sum_ss_error2/sum_ss_total)

        '''Output 1'''

        # Iklan fisik
        print(f"----------------------------------------------------------------------------------\n")
        print(f"Nilai Regresi variabel Iklan fisik dengan Penjualan\n")
        print (f"Nilai Slope adalah {slope}")
        print(f"Nilai Intercept adalah {intercept}")
        print(f'Koefisien determinasi adalah {k_determinasi}')

        # Iklan digital
        print(f"----------------------------------------------------------------------------------\n")
        print(f"Nilai Regresi variabel Pengeluaran Iklan digital dengan Penjualan\n")
        print (f"Nilai Slope adalah {slope2}")
        print(f"Nilai Intercept adalah {intercept2}")
        print(f'Koefisien determinasi adalah {k_determinasi2}')

        print(f"----------------------------------------------------------------------------------\n")
        if k_determinasi >= 0.7 or k_determinasi2 >= 0.7 :
            if k_determinasi >k_determinasi2 :
                number = 1
                print(f"Variabel IKLAN FISIK - PENJUALAN lebih sesuai dibandingkan dengan variabel IKLAN DIGITAL - PENJUALAN\n")
                print(f"Isi jumlah penjualan produk yang diinginkan dengan angka!\n")
                while True :
                    input_number = input("Jumlah data yang diinginkan :")
                    try :
                        input_number = int(input_number)
                        break
                    except ValueError :
                        print(f"Input harus berupa angka bulat")
                while number <= input_number :
                    input_number = input("Jumlah data yang diinginkan :")
                    try :
                        target_penjualan = int(input(f"{number}. Penjualan yang diinginkan :"))
                        list_target_penjualan.append(target_penjualan)
                        number_list.append(number)
                        number+=1
                    except ValueError :
                        print(f"Input harus berupa angka bulat")
                print(f"|{'No':^5}|{'Biaya Iklan Fisik':^25}|{'Target Penjualan':^20}|")
                for target,nomor in zip(list_target_penjualan,number_list) :
                    perkiraan_biaya_iklan_fisik = round((target - 655.3994)/0.00021)
                    if perkiraan_biaya_iklan_fisik < 0 :
                        perkiraan_biaya_iklan_fisik = 0
                    print(f"|{nomor:<5}|Rp{perkiraan_biaya_iklan_fisik:<23,.0f}|{target:<15} buah|")
                    
            elif k_determinasi >1 or k_determinasi2 >1 :
                print(f"Perhitungan salah")
                exit()

            else :
                print(f"Variabel IKLAN DIGITAL - PENJUALAN lebih sesuai dibandingkan dengan variabel IKLAN FISIK - PENJUALAN\n")
                print(f"Isi jumlah penjualan produk yang diinginkan dengan angka!\n")
                number = 1
                while True :
                    input_number = input("Jumlah data yang diinginkan :")
                    try :
                        input_number = int(input_number)
                        break
                    except ValueError :
                        print(f"Input harus berupa angka bulat")
                while number <= input_number :
                    try :
                        target_penjualan = int(input(f"{number}. Penjualan yang diinginkan :"))
                        list_target_penjualan.append(target_penjualan)
                        number_list.append(number)
                        number+=1
                    except ValueError :
                        print(f"Input harus berupa angka bulat")
                print(f"|{'No':^5}|{'Biaya Iklan Digital':^25}|{'Target Penjualan':^20}|")
                for target,nomor in zip(list_target_penjualan,number_list) :
                    perkiraan_biaya_iklan_digital = round((target -571.9346)/0.00022)
                    if perkiraan_biaya_iklan_digital < 0 :
                        perkiraan_biaya_iklan_digital = 0
                    print(f"|{nomor:^5}|Rp{perkiraan_biaya_iklan_digital:^23,.0f}|{target:^15} buah|")

        elif k_determinasi and k_determinasi2 < 0.7 :
            print(f"Model tidak ada yang sesuai untuk memberikan prediksi")
            exit()

    while True :
        try :
            print(f"Apakah ingin menghitung ulang?")
            input_decision = str(input("y/n? :"))
            if input_decision == 'y' or input_decision == 'n' :
                if input_decision == 'y' :
                    print(f"Apakah ingin menghapus data sebelumnya?")
                    while True :
                        try :
                            input_delete = str(input("y/n :"))
                            if input_delete == "y" :
                                iklan_fisik.clear()
                                iklan_digital.clear()
                                penjualan.clear()
                                list_target_penjualan.clear()
                                iklan_fisik_kali_penjualan.clear()
                                iklan_digital_kali_penjualan.clear()
                                iklan_fisik_kuadrat.clear()
                                iklan_digital_kuadrat.clear()
                                penjualan_kuadrat.clear()
                                y_perkiraan.clear()
                                y_perkiraan2.clear()
                                ss_error1.clear()
                                ss_total1.clear()
                                ss_error2.clear()
                                break

                            else :
                                list_target_penjualan.clear()
                                break
                        except ValueError :
                            print(f'Input tidak valid')
                    break

                else :
                    print(f'Perhitungan Selesai')
                    exit()

            else :
                print("Ulangi input")
        except ValueError :
            print(f'Input tidak valid')