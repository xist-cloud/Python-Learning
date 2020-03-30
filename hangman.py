def hangman():
    import os
    import random
    os.system('cls')
    word = ['hello','Austria','Lamborghini','Python']
    word = (random.choice(word)).casefold()
    turns = 5
    guesses=''
    while turns > 0:
        flag = 0
        print("Turns:: ",turns)
        for char in word:
            if char in guesses:
                print(char,end='')
            else:
                print("-",end='')
                flag += 1
        print()
        if flag == 0:
            print("You Won")
            input()
            break
        guess = input("Enter guess:: ")
        guess = guess.casefold()
        guesses += guess
        if guess not in word:
            turns -= 1
        os.system('cls')
        if turns == 0:
            print("You Lose")
            input()