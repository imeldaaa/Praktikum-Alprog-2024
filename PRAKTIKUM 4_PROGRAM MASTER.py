import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''DATA'''
# Data 1
variabel = ["Iklan Fisik","Iklan Digital"]
iklan_fisik = []
iklan_digital = []
penjualan = []
# Data 2
# iklan_fisik
ss_error1 = []
ss_total1 = []
# iklan_digital
ss_error2 = []
# Data 4
list_biaya_iklan_fisik = []
list_biaya_iklan_digital = []
list_slope = []
list_intercept = []
list_target_penjualan = []
number_list = []

def login() :
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
    input_data()

def input_data() :
    global arr_penjualan,arr_iklan_digital,arr_iklan_fisik
    '''Input Manual'''
    print(f"Isi data dengan angka, jika sudah selesai ketik 'end'")
    print(f"Pengeluaran iklan_fisik dan iklan_digital satuannya RIBUAN, Penjualan satuannya BUAH")
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

    arr_iklan_fisik = np.array(iklan_fisik)
    arr_iklan_digital = np.array(iklan_digital)
    arr_iklan_fisik = arr_iklan_fisik.astype(np.float64)
    arr_iklan_digital = arr_iklan_digital.astype(np.float64)
    arr_penjualan = np.array(penjualan)
    tabel_data()

def perhitungan() :
    global k_determinasi,k_determinasi2,slope,slope2,intercept,intercept2
    '''Perhitungan'''
    # a. Data variabel 
    n = len(arr_iklan_fisik)
    total_iklan_fisik = np.sum(arr_iklan_fisik)
    total_iklan_digital = np.sum(arr_iklan_digital)
    total_penjualan = np.sum(arr_penjualan)
    total_k_iklan_fisik = total_iklan_fisik**2
    total_k_iklan_digital = total_iklan_digital**2

    # b. Menghitung persamaan regresi
    # 1) iklan_fisik-Penjualan
    iklan_fisik_x_penjualan = (arr_iklan_fisik*arr_penjualan)
    iklan_fisik_kuadrat = (arr_iklan_fisik**2)

    # 2) iklan_digital-Penjualan
    iklan_digital_x_penjualan = (arr_iklan_digital*arr_penjualan)
    iklan_digital_kuadrat = (arr_iklan_digital**2)
    sum_fp = np.sum(iklan_fisik_x_penjualan)
    sum_iklan_fisik_kuadrat = np.sum(iklan_fisik_kuadrat)
    sum_dp = np.sum(iklan_digital_x_penjualan)
    sum_iklan_digital_kuadrat = np.sum(iklan_digital_kuadrat)

    slope = ((n * sum_fp) - (total_iklan_fisik * total_penjualan)) / (n * (sum_iklan_fisik_kuadrat) - total_k_iklan_fisik)
    intercept =((total_penjualan) - (slope * total_iklan_fisik)) / n
    list_slope.append(slope)
    list_intercept.append(intercept)

    slope2 =  ((n * sum_dp) - (total_iklan_digital * total_penjualan)) / (n * (sum_iklan_digital_kuadrat) - total_k_iklan_digital)
    intercept2 =  ((total_penjualan) - (slope2 * total_iklan_digital)) / n
    list_slope.append(slope2)
    list_intercept.append(intercept2)


    # Koefisien determinasi
    penjualan_average = np.mean(arr_penjualan)
   
    # iklan_fisik
    y_perkiraan1 = ((slope*arr_iklan_fisik)+intercept)
    ss_error1 = ((arr_penjualan-y_perkiraan1)**2)

    # iklan_digital
    y_perkiraan2 = ((slope2*arr_iklan_digital)+intercept2)
    ss_error2 = ((arr_penjualan-y_perkiraan2)**2)

    # SS total
    ss_total = ((arr_penjualan-penjualan_average)**2)   
    
    # SUM
    sum_ss_error = np.sum(ss_error1)
    sum_ss_total = np.sum(ss_total)
    k_determinasi= 1-(sum_ss_error/sum_ss_total)

    # iklan_digital
    sum_ss_error2 = np.sum(ss_error2)
    k_determinasi2= 1-(sum_ss_error2/sum_ss_total)

    output()
    
def output() :
    global arr_biaya_iklan_digital,arr_target_penjualan,perkiraan_penjualan,arr_iklan_fisik_ke
    tabel_regresi()
    print(f"----------------------------------------------------------------------------------\n")
    if k_determinasi >= 0.7 or k_determinasi2 >= 0.7 :
        if k_determinasi >k_determinasi2 :
            number = 1
            input_number = int(input("Jumlah data yang diinginkan :"))
            while number <= input_number :
                try :
                    target_penjualan = int(input(f"{number}. Penjualan yang diinginkan :"))
                    list_target_penjualan.append(target_penjualan)
                    number_list.append(number)
                    number+=1
                except ValueError :
                    print(f"Input harus berupa angka bulat")  
            arr_target_penjualan = np.array(list_target_penjualan)
            perkiraan_biaya_iklan_fisik = np.round((arr_target_penjualan-intercept2)/slope2)
            list_perkiraan_biaya_iklan_fisik = perkiraan_biaya_iklan_fisik.tolist()
            for i in list_perkiraan_biaya_iklan_fisik :
                if i < 0 :
                   i = 0
                   list_biaya_iklan_fisik.append(i)
                else :
                    list_biaya_iklan_fisik.append(i)
            arr_iklan_fisik_ke = np.array(list_biaya_iklan_fisik) 
            perkiraan_penjualan = np.round(slope*arr_iklan_fisik_ke+intercept)
            tabel_iklan_fisik()
                
        elif k_determinasi >1 or k_determinasi2 >1 :
            print(f"Perhitungan salah")
            exit()

        else :
            print(f"Variabel IKLAN DIGITAL - PENJUALAN lebih sesuai dibandingkan dengan variabel IKLAN FISIK - PENJUALAN\n")
            print(f"Isi jumlah penjualan produk yang diinginkan dengan angka!\n")
            number = 1
            input_number = int(input("Jumlah data yang diinginkan :"))
            while number <= input_number :
                try :
                    target_penjualan = int(input(f"{number}. Penjualan yang diinginkan :"))
                    list_target_penjualan.append(target_penjualan)
                    number_list.append(number)
                    number+=1
                except ValueError :
                    print(f"Input harus berupa angka bulat")  
            arr_target_penjualan = np.array(list_target_penjualan)
            perkiraan_biaya_iklan_digital = np.round((arr_target_penjualan-intercept2)/slope2)
            list_perkiraan_biaya_iklan_digital = perkiraan_biaya_iklan_digital.tolist()
            for i in list_perkiraan_biaya_iklan_digital :
                if i < 0 :
                   i = 0
                   list_biaya_iklan_digital.append(i)
                else :
                    list_biaya_iklan_digital.append(i)
            arr_biaya_iklan_digital = np.array(list_biaya_iklan_digital)
            tabel_iklan_digital()
       
    elif k_determinasi and k_determinasi2 < 0.7 :
        print(f"Model tidak ada yang sesuai untuk memberikan prediksi")
        exit()

def tabel_data() :
    df1 = pd.DataFrame({'Biaya Iklan Fisik' : [f"Rp{a:,.2f}" for a in arr_iklan_fisik],
                       'Biaya Iklan Digital' :[f"Rp{b:,.2f}" for b in arr_iklan_digital] ,
                       'Penjualan' :[f"{c:,.0f} Buah" for c in penjualan] ,
                    })
    print(df1.to_string(index=False))

    perhitungan()

def tabel_regresi() :
    df2 = pd.DataFrame({'Variabel' : variabel,
                       'Slope' : list_slope ,
                       'Intercept' :list_intercept ,
                    })
    print(df2.to_string(index=False))

def tabel_iklan_fisik() :
    df3 = pd.DataFrame({})
    df3.to_excel(f'Data Excel Perkiraan Penjualan.xlsx',index=False)
    df4 = pd.DataFrame({'Penjualan' : perkiraan_penjualan,
                        'Biaya Iklan Fisik' : arr_iklan_fisik_ke, 
                        })
    
    df4.to_excel(f'Data Excel Perkiraan Penjualan Iklan Fisik.xlsx', index=False)
    grafik()

def tabel_iklan_digital() :
    df5 = pd.DataFrame({})
    df5.to_excel(f'Data Excel Perkiraan Biaya.xlsx',index=False)

    df6 = pd.DataFrame({'Target Penjualan' : arr_target_penjualan,
                        'Biaya Iklan Digital' : arr_biaya_iklan_digital })
    df6.to_excel(f'Data Excel Perkiraan Biaya Iklan Digital.xlsx',index=False)
    grafik()

def grafik() :
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), facecolor='white')

    # Scatter plot pertama pada ax1
    ax1.scatter(iklan_fisik, penjualan, s=85, c='blue', edgecolor='white', linewidth=1)
    ax1.set_title('Grafik Iklan Fisik-Penjualan', fontsize=18, color='black', fontweight='bold')
    ax1.set_xlabel('Iklan Fisik', color='black', fontweight='bold')
    ax1.set_ylabel('Penjualan (Unit)', color='black', fontweight='bold')
    ax1.set_facecolor('white')
    ax1.spines['top'].set_color('black')
    ax1.spines['bottom'].set_color('black')
    ax1.spines['left'].set_color('black')
    ax1.spines['right'].set_color('black')

    # Scatter plot kedua pada ax2
    ax2.scatter(iklan_digital, penjualan, s=85, c='red', edgecolor='black', linewidth=1)
    ax2.set_title('Grafik Iklan Digital-Penjualan', fontsize=18, color='black', fontweight='bold')
    ax2.set_xlabel('Iklan Digital', color='black', fontweight='bold')
    ax2.set_ylabel('Penjualan (Unit)', color='black', fontweight='bold')
    ax2.set_facecolor('white')
    ax2.spines['top'].set_color('black')
    ax2.spines['bottom'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')

    # Menampilkan window grafik
    plt.tight_layout()
    plt.show()
    print('Perhitungan Selesai, Terima Kasih telah memakai program kami')

login()
