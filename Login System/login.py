# Login System project
# create an account, input a username, email, password
# store information in a text file/database
# Allow login as well and validate information 


import os, time, random, pwinput

def clear():
    os.system('cls')
    time.sleep(1)

def save(username, password):
    with open('user_info.txt', 'a') as file:
        file.write(f'{username}:{password}\n')

def check_credentials(username, password):
    if not os.path.exists('user_info.txt'):
        return False

    with open('user_info.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                return True
    return False

def LS():
    loggedin = 0
    
    ls = input("Do you want to \n[1] Sign Up\n[2] Login\n[3] Continue Without Login \n")

    if ls == "1":
        susername = input("Username: ")
        spassword = pwinput.pwinput("Password: ", mask = '*')
        save(susername, spassword)
        print("Successfully Logged In!")
        LS()
    elif ls == "2":
        username = input("Username: ")
        password = pwinput.pwinput("Password: ", mask = '*')
        if check_credentials(username, password):
            print("Login Successful")
            time.sleep(1)
            clear()
        else:
            print("Incorrect Username or Password!")
            time.sleep(1)
            clear()
    elif ls == "3":
        guestusername = "Guest" + str(random.randint(0, 999))
        print(f"Welcome, {guestusername}!")
    else:
        print("Not An Option!")

LS()
