#!python3
import json
import sys
def LoginSystem():
    filename = "login.txt"   #notepad file to store login data
    login = None

    with open(filename) as fh:
        login = fh.read()
        login = eval(login)             # convert any string to python readable code
        fh.close()

    print("Welcome...")
    welcome = input("Do you have an acount? y/n  (press 'q' to exit): ")

    if welcome == "q":
        sys.exit()

    if welcome == "n":
        while True:
            print("To stop use username q")
            username = input("Enter a username:")
            if username == "q": sys.exit()
            password = input("Enter a password:")
            password1 = input("Confirm password:")
            if password == password1 and username not in login:
                login[username] = password
                welcome = "y"

                with open('login.txt', 'w') as file:
                    file.write(str(login))
                    file.close()
                break
            if username in login:
                print("username already in use")
            else:
                print("Passwords do NOT match!")


    if welcome == "y":
        while True:
            print("Please enter username(enter 'q' to go back) and password\n")
            username = input("Login:")
            if username == "q":
                LoginSystem()
            password = input("Password:")
            try:
                if login[username] == password:
                    print("Welcome  " + username)
                    break
            except:
                print("Incorrect username or password. if you want to go back press q.")

    else:
        print("please enter valid input")
        return LoginSystem()

    return username
