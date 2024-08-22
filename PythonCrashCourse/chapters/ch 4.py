#working with lists


#1.looping
#   for loop
 
# friends =['ali','omer','mohammed']
# for friend in friends:
#     print(friend)

# in for loop space / tab matters 

# friends =['ali','omer','mohammed']
# for friend in friends:
#     print(f"you are invited to my birthday {friend.title()}\n")
# print("thank you everyone for coming to my birthday")
 

#indenting is important to for loop


#2.numerical list
#   range(b,n) 
#       starts at b and end at n-1
#       if range(n) it starts at 0 and end in n-1
# for value in range(21):
#     print('I love python',value)




# #list of numbers
# #   jump j
# #     in range(b,n,j)
# numbers=list(range(0,21,2))
# print (numbers)

# #SQnum
# squares=[]
# for value in range(11):
#     square =value **2
#     squares.append(square)
#     print("we have added square",square)
# print(squares)


#Working with a part of a list
#   slice[b:n] ## ends at n-1
# friends =['ali','omer','mohammed','osama']
# print(friends[0:3])
#if b or n is missing the slicer will start tell the end of the list [b:] or will start from the beginning of the list [:n]


# friends =['ali','omer','mohammed','osama']
# print(friends[-3:])

###res ['omer' as -3, 'mohammed' as -2, 'osama' as -1]


#loop & slice
# players=['CR7','R9','Mo11','R4','P3','Z5']
# print('my team players are')
# for player in players[0:3]:
#     print(player)

#copy list

# my_friends=['omer', 'mohammed', 'osama']
# axis_friends=my_friends[:]
# print(my_friends,'\n')
# print(axis_friends)

#tuples
#   lists that cannot be changed after defined
# my_range=(1,2,3,4,5)

# print(my_range)


# my_range[0]=18#### the error: TypeError: 'tuple' object does not support item assignment

# my_range.append(10)#### the error :AttributeError: 'tuple' object has no attribute 'append'

#but we can overwrite on tuples

# my_range=(1,2,3,4,5)

# print(my_range)

# my_range=(9,10,11,12,13,14)

# print(my_range)