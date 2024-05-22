'''Game of guessing number'''


import random
# three quotes to print in different lines
print("""               _                                _              _   _                                           
 __      _____| | ___ ___  _ __ ___   ___      | |_ ___       | |_| |__   ___        __ _  __ _ _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \     | __/ _ \      | __| '_ \ / _ \      / _` |/ _` | '_ ` _ \ / _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/     | || (_) |     | |_| | | |  __/     | (_| | (_| | | | | | |  __/
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|      \__\___/       \__|_| |_|\___|      \__, |\__,_|_| |_| |_|\___|
                                                                                    |___/                      """)
def func(num,level):
    for i in range(level):
        guess=int(input("Make a guess"))
        if guess==num:
            break
        elif guess>num:
            print("Guess is too high\nguess again")
            print(f"you have {10-(i+1)} remaining guesses left:")
        elif guess<num:
            print("guess is too low\nguess again")
            print(f"you have {10-(i+1)} remaining guesses left:")
        else:
            print("You lost :(")
    print("You are right!! :)")

print("Let me think of number between 1 to 50")
level=input("Choose level of difficulty...Type 'easy' or 'hard'")
number=random.randint(1,50)
if level=='easy':
    func(number,10)
elif level=='hard':
    func(number,5)
else:
    print("wrong input")
    