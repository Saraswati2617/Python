'''PROJECT 2'''
'''***PASSWORD GENERATOR***'''

import random
nl=int(input("Enter the number of letters you want in your password:"))
ns=int(input("Enter the number of symbols:"))
nn=int(input("How many digits you want?:"))
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','$','&','*']
number=['1','2','3','4','5','6']
# ch=""
# for i in range(nl):
#     find=random.choice(letters)
#     ch=ch+find
# for i in range(ns):
#     find=random.choice(symbols)
#     ch=ch+find
# for i in range(nn):
#     find=random.choice(number)
#     ch=ch+find
# passw=ch
# print(f"your password is {passw}")

# ***list form***
ch=[]
for i in range(nl):
    find=random.choice(letters)
    ch=ch+list(find)
for i in range(ns):
    find=random.choice(symbols)
    ch=ch+list(find)
for i in range(nn):
    find=random.choice(number)
    ch=ch+list(find)
random.shuffle(ch)
print(ch)
stri=""
for i in range(nl+ns+nn):
    stri=stri+ch[i]
print(f"your password is {stri}")
