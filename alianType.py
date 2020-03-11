def choose_player():
    print("PLease enter player type")
    print("1. Dark Knight")
    print("2. Legend")
    playerImg = input()
    if playerImg == '1':
        return "c_spaceship.png", (255, 255, 255)
    elif playerImg == '2':
        return "spaceship.png", (0, 255, 40)
    else:
        print("please choose from given")
        return choose_player()
