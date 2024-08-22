#*Dictionary
#### student={'name':'osama','id':1}
#### print(f'student name is : {student["name"].title()} \nstudent  id is : {student["id"]}')
#so from that dictionary is a list can connect relation  between some data 
#we start by {'<the name of key>':<value of the key>}



#adding to a dictionary
# students={}
# students['name']='osama'
# students['id']=11
# students['age']=22
# print(students)   

#output: {'name': 'osama', 'id': 11, 'age': 22}

#modifying the  value of a key in a dictionary
# school V1

# student={'name':'osama','id':1}
# print(f'student name is : {student["name"].title()} \nstudent  id is : {student["id"]}')
# student['id']=10
# print(f'{student["name"].title()}\'s new id is \n {student["id"]}')
# print(f'we are searching for {student["name"]}')
# if student["id"]==11:
#     print(f'we found {student["name"].title()} ')
# else:
#     print(f'we did not find {student["name"].title()}')



#removing  a key from a dictionary
# student={'name':'osama','id':1,'age':22}
# print(student)
# del student['age']
# print(student)
#output: {'name': 'osama', 'id': 1}
#we use del <name of dictionary>['key']


#what if we need to get a key that doesn't  exist in the dictionary?
#we use get()  ### <dictionary name>.get(<key name >, <value  if key doesn't exist>)
# student={'name':'osama','id':1,'age':22}
# print(student.get('grade','its secret shhhhhh'))
#if grade exist the output will be : its secret shhhhhh
#else the output will be whatever grade it's

# people={'osama':'Egypt','nour':'saudi','jake':'usa','june':'uk','muller':'germany'}
# for names, country in people.items():
#     print(f'{names.title()} is from {country.title()}')
    
# .items() return sequence of key-value pairs
#  .keys() return sequence of keys
#  .values() return sequence of values


# people={'osama':'Egypt','nour':'saudi','jake':'usa','june':'uk','muller':'germany'}

# for names, country in sorted(people.items()):
#     print(f'{names.title()} is from {country.title()}')
# for  names in sorted(people.keys()):
#     print('my name is',names.title())
# for  country in sorted(people.values()):
#     print('I\'m from ',country.title())
    
    
#here sorted function sorts the dictionary by the name  of the key or the value
# we also have set() which  returns a set object which is an unordered collection of unique elements
# we can use set() to remove duplicates from a list or a dictionary

#!!!! Nesting
    #*1.list of dictionaries
    #*2.dictionaries of dictionaries
    #*3.list inside a dictionary
    #*4.dictionary inside a dictionary
#*1.list of dictionaries
# TeamLeader1={'id':1,'city':'fayoum','name':'osama'}
# TeamLeader2={'id':2,'city':'cairo','name':'ali'}
# TeamLeader3={'id':3,'city':'alex','name':'omar'}
# TeamLeaders=[TeamLeader1,TeamLeader2,TeamLeader3]
# for group in TeamLeaders:
#     print(group['id'],group['name'])
# for group in  range(1,21):
#     if group>=4:
#         NewTeamLeader={'id':group,'city':'Unn','name':'Unn'}
#         TeamLeaders.append(NewTeamLeader)
#         print('the new team leader',NewTeamLeader)
#     else:

#         print('no  new team leader')

#?what I wanted to is to check in the second loop for the id and add more ids
    #! I used AI and here is it's answer
#     # Define the initial team leaders
# team_leaders = [
#     {'id': 1, 'city': 'fayoum', 'name': 'osama'},
#     {'id': 2, 'city': 'cairo', 'name': 'ali'},
#     {'id': 3, 'city': 'alex', 'name': 'omar'}
# ]

# # Print the initial team leaders
# for leader in team_leaders:
#     print(leader['id'], leader['name'])

# # Add new team leaders
# for i in range(1, 21):
#     existing_leader = next((leader for leader in team_leaders if leader['id'] == i), None)
#     if existing_leader:
#         print(f"Team leader with ID {i} already exists:", existing_leader)
#     else:
#         new_leader = {'id': i, 'city': 'Unn', 'name': 'Unn'}
#         team_leaders.append(new_leader)
#         print(f"New team leader added:", new_leader)

# # Print the updated team leaders
# for leader in team_leaders:
#     print(leader['id'], leader['name'])
    
#!!! The output is more organized 

#list in a dictionary
# programmers={'osama':['c','c++','linux','python'],'ali':['c','python']
#              ,'mohammed':['c++','java']}
# for  name,skills in programmers.items():
#     print(f'\n{name.title()} have skills like:')
#     for  skill in skills:
#         print(skill.title())

#! keep an eye for the indent




#dictionary in dictionary


# team1={'member1':{'id':1,'name':'osama','age':22,'city':'fayoum'},
#        'member2':{'id':2,'name':'Ali','age':22,'city':'fayoum'},
#        'member3':{'id':3,'name':'omar','age':18,'city':'cairo'},
#        'member4':{'id':4,'name':'june','age':24,'city':'LA'}}
# print('our team  is:')

# for  member,info in team1.items():
#     print(f'\n Hello I\'m {member} {info['name']} I\'m {info['age']} and from {info['city']}')
