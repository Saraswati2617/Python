'''upto lec no.31'''

'''add  two numbers input logic'''
#  *** integer cannot be indexed ... X int(input)  ****

# number = (input("enter the digits to be added "))
# num1=number[0]
# num2=number[1]
# num3=number[2]
# print(int(num1)+int(num2)+int(num3))

'''******
# floor division returns integer part of quotient
# power operator **
# pemdas
*******'''

'''calculate bmi'''
# weight=int(input("enter weight in kg: "))
# height=float(input("enter height in meters: "))
# bmi=weight/(height**2)
# print(f"{bmi} is your body mass index")


'''calculate the number of years weeks and days left if one lives for 90 days'''
# output:- you have a years b months c days left
# age=int(input("enter the age of your:"))
# years_left=90-age
# days_left=years_left * 365
# months_left=years_left * 12
# weeks_left=years_left*52
# print(f"you have {years_left} years {months_left} months {weeks_left} weeks and {days_left} days left until 90 years")


'''find leap year or not *** if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))'''
# year=int(input("enter the year:"))
# if(year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")


'''****...pizza...****'''
# s_p=100
# m_p=200
# l_p=300
# print("prize of normal pizza:\nlarge size:300\nmedum size:200\nsmall size:100")
# size=input("enter the size of pizza:\nL for Large\nM for medium\nS for small\n input:")
# if size=='S':
#     f_p=s_p
# elif size=='M':
#     f_p=m_p
# else:
#     f_p=l_p

# pep_s=30
# pep_ml=50
# print("Price with pepporoni:\npepporoni for small pizza:30\nnpepporoni for medium and large pizza:50")
# pep=input("do you want it?yes or no:")
# if(pep=='yes'):
#     if(size=='S'):
#         f_p=f_p+pep_s
#     else:
#         f_p=f_p+pep_ml
# else:
#     print("ok.")
# print("Price for exttra cheese with any sized pizza:20")
# cheese=input("Do you want extra cheese?yes or no:")
# if(cheese=='yes'):
#     f_p=f_p+20
# else:
#     print("thanku for answering")

# print(f"Your total bill is {f_p}")


''' *** LOVE CALCULATOR *** '''
# boy=input("enetr boy's name")
# girl=input("enter girl's name")
# boylo=boy.lower()
# girllo=girl.lower()
# true=(boylo.count('t') + girllo.count('t'))+(boylo.count('r') + girllo.count('r'))+(boylo.count('u') + girllo.count('u'))+(boylo.count('e') + girllo.count('e'))
# love=(boylo.count('l') + girllo.count('l'))+(boylo.count('o') + girllo.count('o'))+(boylo.count('v') + girllo.count('v'))+(boylo.count('e') + girllo.count('e'))
# per=str(true)+str(love)
# print(f"the love percenetage is {per}%")






