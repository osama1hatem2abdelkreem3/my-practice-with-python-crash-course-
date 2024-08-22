#list sesion 
#chapter 3 intro to lists

#############################################
#osama_friends=['Ahmed','ali','abdo']
#print(osama_friends[1].title())


##############################################

'''
cars=['bmw','honda','tyota','kia']
mesage=f"my first car is {cars[0].upper()}"
print(mesage)
'''

#title()## look more presentable
#cars=['bmw','honda','tyota','kia']
#print(cars[0].title())



# f-string
# you should get the element so cars.upper() is error ### cars[0].upper() is correct
'''
cars=['bmw','honda','tyota','kia']
message = f"my favourite car is {cars[0].upper()}"
print(message)
'''
#try yourself 
'''
people=['ahmed','osama','abdo','ali']
message = f"good night {people[1].title()}"
print(message)
'''

#Modify

'''
people=['ahmed','osama','abdo','ali']
people[0]='mohammed'
print(people)
'''



#adding 
#in adding it add to the last element 
'''
people=['ahmed','osama','abdo','ali']
people.append('nour')
print(people)
'''

#insert
#insert take no = , it takes 2 parameters (<index>,<name>)
'''
people=['ahmed','osama','abdo','ali']
people.insert(0,'moha')
print(people)
'''
#Remove
#we have pop() ,del
#del 
'''
del people[0]

'''

#pop()
#pop the last element on the list and save it in <list>.pop()
'''
people.pop()=<popped element>
'''

'''
people=['ahmed','osama','abdo','ali']
last_person=people.pop()
message=f"last person was in list was {last_person.title()}"
print(message)
print("and the list =",people)
'''
#you can pop elemnt as pop(0)

#remove by value 
'''
<list name>.remove(<value name>)
'''
#try yourself
#guest invetation 
'''
guests =['ali','ahmed','mohammed']
guests.insert(0,'osama')
guests.append('moha')
print(guests)
message1=f"I invite you to attend my birthday sir, {guests[0].title()}"
message2=f"I invite you to attend my birthday don't forget your prisent , {guests[2].title()}"
message3=f"I would like to invite you to my birthday ,sir {guests[4].title()} "
print(message1)
print(message2)
print(message3)
guests.pop(0)
guests.pop(2)
guests.pop(2)
print('the remaining guests are =',guests)
'''

#organize list
#sort
#don't forget the () for the func

# cars=['bmw','honda','tyota','kia']
# cars.sort()
# print(cars)



# to comment effectivly ctrl + /

#sorted(<list name>)



#reverse()


# cars=['bmw','honda','tyota','kia']
# cars.reverse()
# print(cars)

#len(<list name>)= number of elements
 

# cars=['bmw','honda','tyota','kia']
# print(len(cars))

