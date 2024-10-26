import os

data_user ={}

def menu_akun():
    while True:
        os.system('cls')
        print("=============================================")
        print("            Membuat akun admin")
        print("=============================================")

        masukan_user = input("Masukan User Admin: ")
        masukan_password = input("Masukan Password Admin: ")
        data_user[masukan_user] = masukan_user
        data_user[masukan_password] = masukan_password

        print("User Admin adalah ",masukan_user)
        print("Password Admin adalah ", masukan_password)
        os.system('pause')
        
        os.system('cls')
        print("=============================================")
        print("             Login akun admin")
        print("=============================================")

        username_login = input("Masukkan username yang sudah ada: ")
        password_login = input("Masukkan password yang sudah ada: ")

        if username_login in data_user[masukan_user] and password_login in data_user[masukan_password]:
                print("Selamat, login berhasil!")
                input("\nklik enter untuk lanjut")
        else:
                print("Username atau password salah.")

        os.system('pause')

menu_akun()          