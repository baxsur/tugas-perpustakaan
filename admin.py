import signup
import login

user_data = {}
def admin():
    print("Selamat datang admin!\n")
    print("masukan angka 1 bila sudah punya akun")
    print("masukan angka 2 tidak punya akun")
    print("1.login")
    print("2.signup")    
    admin_masuk = input("pilihan anda: ")

    if admin_masuk == "1":
        login.login(user_data)
    elif admin_masuk == "2":
        signup.signup(user_data)
    else:
        print("ya")    
