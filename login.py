def login(user_data):
    username_login = input("Masukkan username yang sudah ada: ")
    password_login = input("Masukkan password yang sudah ada: ")

    if username_login in user_data and user_data[username_login] == password_login:
        print("Selamat, login berhasil!")
        input("\nklik enter untuk lanjut")
    else:
        print("Username atau password salah.")
