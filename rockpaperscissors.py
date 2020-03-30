def rps():
    import random
    import os
    import time
    os.system('cls')
    choose = ['rock','paper','scissors']
    cpu_choice = choose.index(random.choice(choose))
    user = input("Enter choice {}:: ".format(choose))
    os.system('cls')
    if user not in choose:
        print("Wrong input")
    else:
        user=choose.index(user)
        print("Computer:: {}".format(choose[cpu_choice]))
        print("User:: {}".format(choose[user]))
        if user==cpu_choice:
            print("Draw")
        else:
            cpu_choice += 1
            if cpu_choice ==3:
                cpu_choice = 0
            if user==cpu_choice:
                print("User wins")
            else:
                print("CPU wins")
    time.sleep(2)     

