'''calculator'''
def cal1(firstnum,choice,secnum):
    if(choice=='+'):
        return firstnum + secnum
    elif(choice=='-'):
        return firstnum-secnum
    elif(choice=='*'):
        return firstnum*secnum
    elif(choice=='/'):
        return firstnum /secnum
    else:
        return("wronginput")

firstnum=int(input("Enter first number: "))
choice=input("+\n-\n*\n/\npick an operation")
secnum=int(input("enter next number"))
value1=cal1(firstnum,choice,secnum)
print(f"{firstnum} {choice} {secnum} = {value1}")
choice2=input(f"Enter 'y' to continue calculation with{value1} or 'n' to start new calculation or 'x' to exit:")
while choice2=='y'or'n':
    if choice2=='y':
        choice=input("+\n-\n*\n/\npick an operation")
        secnum=int(input("enter next number"))
        value2=cal1(value1,choice,secnum)
        print(f"{value1} {choice} {secnum} = {value2}")
    if choice2=='n':
        firstnum=int(input("Enter first number: "))
        choice=input("+\n-\n*\n/\npick an operation")
        secnum=int(input("enter next number"))
        value1=cal1(firstnum,choice,secnum)
        print(f"{firstnum} {choice} {secnum} = {value1}")
    if choice2=='x':
        print("Thank you!!")
        break
    choice2=input(f"Enter 'y' to continue calculation with{value1} or 'n' to start new calculation or 'x' to exit:")