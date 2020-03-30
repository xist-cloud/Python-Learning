import hangman as hang
import guess_the_number as guess
import rockpaperscissors as rock
import os
os.system('cls')
print("Which game do you want to play")
games = ['1-Hangman','2-Guess the number','3-Rock Paper Scissors']
for x in games:
    print(x)
x = int(input("Enter the corresponding number:: "))
os.system('cls')
if x==1:
    hang.hangman()
elif x==2:
    guess.guess_the_number()
elif x==3:
    rock.rps()
else:
    print("Wrong Input")