''' DICTIONARY'''

'''DICT_NAME={KEY:VALUE}
PROPERTIES:-
1.ordered-output of values will be in order
2.mutable-values can be changed,keys cannot be changed
3.NO duplicates are allowed'''

# phone_no={
#     'Ram':1234,
#     'Shyam':5678,
#     'Mohan':91234,
#     'Ram':9999
# }
# print(phone_no)
# print(phone_no['Shyam'])

# print(dict({
#     'Ram':1234,
#     'Shyam':5678,
#     'Mohan':91234,
#     'Ram':9999}))

# phoneno=dict({
#     'Ram':1234,
#     'Shyam':5678,
#     'Mohan':91234,
#     'Ram':9999
# })
# print(phoneno)

# phoneno=dict([('Ram',1234),('Shyam',5678),('Mohan',91234)])
# print(phoneno)
# phoneno['Mohan']={1111,3333,5555}
# phoneno['Mohan']={'Mohan_home':1111,'Mohan_work':2222}
# print(phoneno['Mohan']['Mohan_work'])
 
'''functions'''
# print(phoneno.get('ram'))
# phoneno.pop('Shyam')
# phoneno.clear()
# phoneno.keys()
# phoneno.values()
# phoneno.items()
# for i in phoneno.items():
    # print(i)

'''EXERCISE : Convert marks into grades'''
# student_marks={"jenny":92,
#                "harry":78,
#                "dimpy":56,
#                "rahul":41,
#                "aniket":99,
#                "prem":34
# }
# print(student_marks)
# student_grades={}
# for i in student_marks:
#     '''i here points to keys'''
#     marks=student_marks[i]
#     '''student_marks[i] takes out the values '''
#     if(marks>90):
#         student_grades[i]='A'
#     elif(marks>80):
#         student_grades[i]='B'
#     elif(marks>70):
#         student_grades[i]='C'
#     elif(marks>60):
#         student_grades[i]='D'
#     elif(marks>50):
#         student_grades[i]='E'
#     elif(marks>40):
#         student_grades[i]='F'
#     elif(marks>30):
#         student_grades[i]='G'
# print(student_grades)


'''NESTED DICTIONARY'''
# mydict={"Ram":{"rollno":10,"age":20,"course":"python"},
#         "Mohan":{"rollno":20,"age":22,"course":"java"}}
# print(mydict)
# print(mydict["Ram"]["age"])
# mydict["Ram"]["phoneno"]=12345
# print(mydict["Ram"])
# del mydict["Ram"]["phoneno"]
# print(mydict)
'''nesting list within dictionary'''
# traveldata={"gujrat":["dwarika","somnath","statue of unity"],"rajasthan":["jaipur","udaipur"]}
# print(traveldata["rajasthan"])
'''dictionary within list'''
# mydict=[{"name":"Ram",
#          "rollno":10,
#          "age":20,
#          "course":"python"},
#        {"name":"Mohan",
#         "rollno":20,
#         "age":22,
#         "course":"java"}]

# print(mydict[1])

'''EXERCISE: ADDING DATA TO GIVEN DICTIONARY WITHIN LIST'''
'''.append'''
# def add_new(name,rollno,age,course):
#         data={}
#         data["name"]=name
#         data["rollno"]=rollno
#         data["age"]=age
#         data["course"]=course
#         print(data)
#         student_data.append(data)
       


student_data=[{
    "Name":"Ram",
    "roll_no":10,
    "age":20,
    "course":"python"},

    {"name":"mohan",
     "rollno":20,
     "age":22,
     "course":"java"}
]
newentry=("shyam",22,18,"c++")
name="shyam"
rollno=22
age=18
course="c++"
# add_new(name,rollno,age,course)
# print(student_data[0]["age"])