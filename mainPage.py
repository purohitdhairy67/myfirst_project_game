from LoginPage import LoginSystem
import os
from alienscore import update_username
from alienDisplayScore import finalScoring
username = LoginSystem()

while True:
    print("Choose one of this:")
    print("Press 1: Space Invender.")
    print("Press 2: scores.")
    print("Press q to go back.")
    num = input()
    if num == "1":
        os.system("python alienGameMain.py")
        update_username(username)
    elif num == "2":
        finalScoring()
    elif num == "q":
        username = LoginSystem()