'''Question answer quiz game'''

import project10db
points=0
totalpoints=10
print("Let's begin the question quiz game:")
end=len(project10db.questions)
# print(end)
l=["1","2","3","4","5","6","7","8","9","10"]
for i in range(end):
    a=l[i]
    print(f"Question No.{i+1}")
    print(project10db.questions[a]["question"])
    print(project10db.questions[a]["options"])
    choose=input("Choose the correct answer:")
    if choose==(project10db.questions[a]["answer"]):
        points+=1
        print("You are correct!")
        print(f"Your point becomes{points}/{totalpoints}")
    else:
        print("OOPS! You are wrong.")
        print(f"Your point becomes{points}/{totalpoints}")
score=(points/10)*100
print(f"You have given {points} answers correct\nYour score is {score}%")
