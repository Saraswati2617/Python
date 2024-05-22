'''PROJECT 3'''
'''HANGMAN GAME'''
''' generate random word...show blank spaces...player have to guess word within limited chance'''

import random
words=['apple','beautiful','potato','ramen']
choose=random.choice(words)
print(choose)
show=""
for i in range(len(choose)):
    show=show+"_"
# showlist=list(show)
print(show)
print("Guess the word in 6 attempts:")

i1=''' +---+
       |   |
       O   |
           |
           |
           |
    ============       '''
i2=''' +---+
       |   |
       O   |
       |   |
           |
           |
    ============       '''
i3=''' +---+
       |   |
       O   |
       |\  |
           |
           |
    ============       '''
i4=''' +---+
       |   |
       O   |
      /|\  |
           |
           |
    ============       '''
i5=''' +---+
       |   |
       O   |
      /|\  |
      /    |
    ============       '''
i6=''' +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ============       '''
lives=6
game_over=False 
while not game_over: 
    guess=input("enter the guessed letter:")
    for position in range(len(choose)):
        letter=choose[position]
        if (letter==guess):
            print("correct! matched")
            show[position]=guess
    print(show)       

    if(guess.lower() not in choose):
        print("wrong")
        lives-=1
        if lives==0:
            game_over=True
            print("you lose!")
    if "_" not in show:
        game_over=True
        print("You win!")