'''lec 31 onwards'''

'''***RANDOM module to get random numbers***'''

'''Head or tail game random module use: 0-head,1-tail'''
# import random
# x=random.randint(0,1)
# if(x==0):
#     print("head")
# else:
#     print("tail")


'''input list of names and randomly generate who will pay the bill'''
# import random
# names=input("enter all names separated by comma:")
# splitname=names.split(",")
# print(splitname)
# x=random.randint(0,(len(splitname)-1)) *****GIVES THE RANDOM INDEX****
# print(f"{splitname[x]} will pay the bill")

# x=random.choice(splitname)   ****DIRECTLY GIVES THE RANDOM  NAME****
# print(f"{x} will pay the bill")


'''suppose we have matrix 3X3 having values 1 in all...i gave  an index as an input..output should come in that place of matrix'''
# row1=['😊','😊','😊']
# row2=['😊','😊','😊']
# row3=['😊','😊','😊']
# matrix=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("enter the position you want to hide your money: ")
# row=int(position[0])
# col=int(position[1])
# matrix[row-1][col-1]='X'
# print(f"{row1}\n{row2}\n{row3}")


'''for else loop****'''
# tuple1=(1,2,3,4,0,5,90)
# for i in tuple1:
#     print(i)
#     # if(i==0):
#     #     break
# else:
#     print("successfully completed.")


'''calculate avg height from list of heights ..taking user input
ans should be in whole number'''

# heights=input('enter height using commas:')
# print(heights)
# print(type(heights))
# hlist=heights.split(",")
# count=0
# for i in hlist:
#     count=count+1
# print(f"number of heights:{count}")
# for i in range(0,count):
#     hlist[i]=int(hlist[i])
# print(type(hlist))
# sum=0
# for i  in range(0,count):
#     sum=sum+hlist[i]
# avg=round(sum/count)
# print(avg)

'''Find maximum number from a list of numbers'''
# number=input("Enter the numbers separated by comma:")
# splitnum=number.split(",")
# count=0
# for i in splitnum:
#     count=count+1
# for i in range(count):
#     splitnum[i]=int(splitnum[i])
# max=splitnum[0]
# for i in range(count):
#     if(splitnum[i]>max):
#         max=splitnum[i]
# print(f"maximum is {max}")

'''Calculate sum of even number from 1 to 100'''
# sum=0
# for i in range(2,101,2):
#     sum=sum+i
# print(f"sum is {sum}")

''''FizzBuzz job interview question
1 to n 
if number divisible by 3 print"fizz"
if number divisble by 5 print "buzz"
if number divisible by 3&5 print "Fizzbuzz"'''

# n=int(input("Enter the limit:"))
# for i in range(1,(n+1)):
#     if(i%3==0 and i%5==0):
#         print("FIZZBUZZ")
#     elif(i%3==0):
#         print("FIZZ")
#     elif(i%5==0):
#         print("BUZZ")
#     else:
#         print(i)   


'''while...else loop'''
# count=1
# while(count!=10):
#     print(count)
#     if(count==5):
#         break
#     count=count+1
# else:
#     print("first out")
# print("final out")

'''***break continue pass***
break:- out of loop
continue:- goes to beginning of loop
pass:- to define an empty loop/function'''
# for i in range (9):
#     pass