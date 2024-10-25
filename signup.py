import login

def signup(user_data):
    
    username = input("\nMasukkan username anda: ")
    password = input("Masukkan password anda: ")
    user_data[username] = password
        
    print("\nUsername anda adalah", username)
    print("Password anda adalah", password)

    login.login(user_data)
    


        

    

