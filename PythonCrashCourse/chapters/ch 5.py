#- control flow :if statement
# cars=['audi','bmw','toyota','kia']
# for car in cars:
#     if car=='bmw':
#         print(car.upper(),'my favorite car')
#     else:
#         print(car.title())

# in if  statement

    # you should also use ==  to compare the value of the variable or && or  || for logical operators 
    #after the statement  you should put a colon : to indicate the start of the block of code that will be executed 
    # if the  condition is false  you can use else statement to execute a block of code
# age1=20
# age2=22
# if( age1>=19 ) and  (age2>=23):
#     print("you are welcome to the party you age is suitable",age1,age2)
# else:
#     print("you are not welcome to the party")


# range_of_nums=50
# if  (range_of_nums<=20) or (range_of_nums>=60):
#     print("you are in range ")
# else:
#     print("you are out of range")
#!by the way I wanted it out of range
# if - elif -else  statement
# MyAge=100
# if MyAge<18:
#     print('I\'m not adult yet')
# elif MyAge <21:
#     print('I\'m a young adult')
# elif (MyAge >=21) and (MyAge<64):
#     print("I\'m adult now , I have to be responsible")
# elif MyAge  >=65 :
#     print("I\'m old man I have to retired")
# else:
#     print("I don't know what to say")

#! elif executes  only if the previous conditions are false and  the current condition is true
    #it executes the first  true condition and skips the rest of the conditions
    
    
#!pizza time V1

# toppings=['pepperoni','sauce','cheese','chicken','green  pepper']
# for pizza in toppings:
    
#     if pizza=='pepperoni':
#         print(f'sorry we are out of {pizza}.')
#     elif pizza=='green  pepper':
#         print(f'sorry we are out of {pizza}')
#     else:
#         print(f'adding {pizza} to your pizza')
# print("pizza is ready")

#!pizza  time V2
# available_toppings=['pepperoni','sauce','cheese','chicken','green  pepper','olive']
# requested_toppings=['mushroom','sauce','pineapple','pepperoni']
# for pizza in  requested_toppings:
#     if pizza in  available_toppings:
#         print(f'adding {pizza} to your pizza')
#     else:
#         print(f'sorry we are out of {pizza}')
# print("pizza is  ready")



# #*pizza time V2 was a very important example  of using if-else statement in a loop
#     so what happened 
#     first declare the  available toppings and the requested toppings
#     we will compare between them 
#     after that create the loop  to check each topping in the requested toppings list
#     we should compare between pizza which is the counter in requested topping  list and the available topping list 
#       #!so that the pizza now is the counter and side in if statement at the same time


