import project8logo
import project8db
import random
import os
print(project8logo.game_logo)

def display(select):
    name=select["name"]
    description=select["description"]
    country=select["country"]
    return f"{name} , a {description} , from {country}"

def check(userin,follower1,follower2):
    if follower1>follower2:
        if userin==1:
            return True
        else:
            return False
    if follower2>follower1:
        if userin==2:
            return True
        else:
            return False


stop=False
points=0
select1=random.choice(project8db.data)
while stop!=True:
    select2=random.choice(project8db.data)
    while select1 == select2:
        select2=random.choice(project8db.data)
    print(f"Compare 1: {display(select1)}")
    print(project8logo.vs)
    print(f"Compare 2: {display(select2)}")

    follower1=select1["follower_count"]
    follower2=select2["follower_count"]
    print(f"{follower1} {follower2}")

    userin=int(input("Enter your choice 1 or 2 :"))
    calc=check(userin,follower1,follower2)
    if calc==True:
        points+=1
        print(os.system('cls'))
        print(f"You are right!! Your score is {points}")
        if userin==1:
            select1=select1
        else:
            select1=select2

       
    else:
        print(f"You are wrong!! Your final score is {points}")
        stop=True