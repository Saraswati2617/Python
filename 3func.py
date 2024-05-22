'''from lecture 55 onwards...function---'''

'''def <function name>(parameter):
        function body
        return expression
   <function name>(arguments) 
   
   ***parameter-formal...arguments-actual parameter'''


# def greet(name):
#     print(f"hi{name}")
# greet("jenny")


# def sum(a,b):
#     sum=a+b
#     return sum
# a,b=10,20
# print(f"sum of a and b is {sum(a,b)}")

# def add(a,b):    ***error***
#     c=a+b
#     print(f"sum is {c}")
# add(5)

'''Types of arguments'''
'''order of passing arguments:- <(normal argument,arbitary positional,keyword,*args,**kwargs)>'''
# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are you from {dept} department?")
# greet("jenny","CS") ***positional arguments
# greet(name="jenny",dept="CS")**keyword arguments
# greet("jenny",dept="Cs") ***positional,keyword
# greet(dept="cs","jenny") ***ERROR-- positional must be before keyword
  

''' ARGS ARGUMENTS--- single*---only accepts positional arguments '''
# def add(*numbers):
#     c=0
#     for i in numbers:
#         c=c+i
#     print(f"sum of {c}")
# add(1,2,3,4,5)

# def add(*numbers,name):
#     c=0
#     for i in numbers:
#         c=c+i
#     print(f"Sum is {c}")
#     print(name)
# add(1,2,3,4,name="jenny")


'''KWARGS ARGUMENTS---double **---only keyword arguments is passed'''

# def infoperson(**kwargs):
#     for key,value in kwargs.items():
#          print(key,value)
    
# infoperson(name="ram",age=30,dept="cse")
# infoperson(name="shyam",dept="cse")


'''calculate number of cans needed to paint wall
   1 can=7 sq.meter
   no of cans=(height*width)/coverage'''
# import math
# def cans(h,w):
#     c1=7
#     nc=math.ceil((h*w)/c1)
#     print(f"number of cans needed is {nc}")
# height=10
# width=12
# cans(height,width)

'''no is prime or not'''
# def prime(n):
#         fact=0
#         for j in range(1,n):
#             if(n%j==0):
#                 fact+=1
#         if fact>1:
#             print(f"{n} is not prime")
#         else:
#             print(f"{n} is prime")

# number=int(input("enter the numbers to be checked separated by commas:"))
# prime(number)