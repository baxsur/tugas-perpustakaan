from dashboard_admin import dashboard_admin
import os

#data_user ={}

def akunAdmin():
     while True:

        #Menampung inputan
        data_user ={
          
        }
        os.system('cls')
        print("=============================================")
        print("            Membuat akun admin")
        print("=============================================")
        print("0.Kembali ke menu utama")
        print("1. Buat akun admin")

        masukan_pilihan = int(input("Masukan pilihan anda: "))
        
        if masukan_pilihan == 1:
              
                #memasukan user dan password admin yang akan dibuat
                masukan_user = input("Masukan User Admin: ")
                masukan_password = input("Masukan Password Admin: ")

                #menyimpan masukan user dan password admin ke dalam Dictionaries data_user
                data_user[masukan_user] = masukan_user
                data_user[masukan_password] = masukan_password

                #Mendeklarasikan variabel input dari masukan_user dan masukan_password
                print("User Admin adalah ",masukan_user)
                print("Password Admin adalah ", masukan_password)
                
                os.system('cls')
                #Memasukan kembali akun admin yang sudah dibuat untuk memverifikasinya
                print("=============================================")
                print("             Login akun admin")
                print("=============================================")

                #Memasukan user dan password Admin yang sudah dibuat(yang ada di dalam dictionaries)
                username_login = input("Masukkan username yang sudah ada: ")
                password_login = input("Masukkan password yang sudah ada: ")

                #mengecek kebenaran akun yang sudah dibuat(yang ada didalam dictionaries)
                if username_login in data_user[masukan_user] == username_login and password_login in data_user[masukan_password] == password_login:
                        dashboard_admin()

                #mengecek kesalahan akun yang sudah dibuat(yang ada didalam dictionaries)
                else:
                        print("Username atau password salah.")
        elif masukan_pilihan == 0:
                break
        else:
              print("Pilihan yang anda masukan tidak ada didalam daftar!")

        os.system('pause')

          
