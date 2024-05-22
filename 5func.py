''' .....lec 73 onwards....'''
'''return statement
def add(3,4):
    c=a+b
    return c '''

# def add(a,b):
#     c=a+b
#     return c

# sum=add(4,5)
# print(sum)

# def formatname(firstn,lastn):
#     first=firstn.title()
#     last=lastn.title()
    # print(first,end=" ")
    # print(last)
    # return(f"{first} {last}")
# naming=formatname("SarAswAtI","YADAV")
# print(formatname("SarAswAtI","YADAV"))


'''multiple return values'''
# import statistics
# def meanmedianmode(list1):
#     return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
# print(meanmedianmode([3,5,7,4,2,1,1,3]))
# x,y,z=meanmedianmode([3,5,7,4,2,1,1,3])
# print(f"mean is {x}\nmedian is {y}\nmode is {z}")

'''User enters month and output is number of days in that month...*leap year then february has 29 days'''
'''****it became a long program***'''
# def leapyear(year):
#     if ((year%4==0 and year%100 !=0)or(year %400==0)):
#         return True
#     else:
#         return False

# def dayscalculate(leapcheck,month):
#     if (leapcheck==True and month=="february"):
#         return 29
#     else:
#         if (month=="january"or"march"or"may"or"july"or"august"or"october"or"december"):
#             return 31
#         if(month=="february"):
#             return 28
#         else:
#             return 30
# year=int(input("Enter the year:"))
# month=(input("enter the month:")).lower()
# leapcheck=leapyear(year)
# # print(leapcheck)
# dayscheck=dayscalculate(leapcheck,month)
# print(f"{year} has {dayscheck} in {month}")

'''**shorter'''
# def leapyear(year):
#     if ((year%4==0 and year%100 !=0)or(year %400==0)):
#         return True
#     else:
#         return False
# def days(leapcheck,month):
#     dayslist=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if(leapcheck==True and month==2):
#         return 29
#     else:
#         return(dayslist[month-1])
# year=int(input("enter your year: "))
# month=int(input("enter your month: "))
# leapcheck=leapyear(year)
# dayscheck=days(leapcheck,month)
# print(f"{year} has {dayscheck} in {month}th month")