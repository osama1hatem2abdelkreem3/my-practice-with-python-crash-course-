#functions 
# def hello():
#     print("Hello")
# hello()
#so we should define the function by def then the <function name > after that () which we can pass parameters to the function
# def HelloUser(username,age):
#     print(f"Hello {username.title()}" )
#     print(f'{username.title()} is  {age} years old')

# HelloUser(username='osama',age=22)
# HelloUser('ali',22)
# HelloUser('ahmed',25)

#I can put default values to the parameters
# def HelloUser(username,age=22): so age is by default 22 if not changed
# def HowOld(name,age=18):
#     print(f"hello {name.title()} you are  {age} years old")
# HowOld('osama')

#return values
# def  Add(a,b):
#     return a+b
# print(Add(5,6)) 

# def formatted_name(Fname,Lname,Mname='',age=None):
#     if Mname:
#         Full_Name= f'{Fname} {Mname} {Lname}'
#     else:
#         Full_Name=f'{Fname} {Lname}'
#     person={'first':Fname,'mid':Mname,'last':Lname}
#     if age:
#         person['age']=age
    
#     return Full_Name.title() , person
    
# person=formatted_name('osama','hatem',age=22)
# print(f'{person}')  




#function wit a while loop
# def areU_satisfied(satisfied=''):
#     while satisfied!='q':
#         satisfied=input('when you satisfied press  q\n')
#     print('you are out the loop now congrats')
# areU_satisfied()



#passing list  to a function
# def  MyFamily(names):
#     for name in names:
#         msg=f'your from my Family {name.title()}'
#         print(msg)

# MyFamily(['osama','ali','mohamed'])
        

#modify
# we have code we want to make functions of it
# 
# outzoom=['osama','ahmed','ali','mohamed']
# inzoom=[]
# while outzoom:
#     person=outzoom.pop()
#     print(f'{person} is entering the zoom')
#     inzoom.append(person)
# for  person in inzoom:
#     print(f'{person} is in the zoom')
# we want this as 2  functions separated
# def  enter_zoom(outzoom,inzoom):
#     while outzoom:
#         person=outzoom.pop()
#         print(f'{person} is entering the zoom')
#         inzoom.append(person)
# def   show_zoom(inzoom):
#     for  person in inzoom:
#         print(f'{person} is in the zoom')



# outerzoom=['osama','ahmed','ali','mohamed']
# inzoom=[]
# enter_zoom(outerzoom[:],inzoom)
# show_zoom(inzoom)
# print(outerzoom)


#*[:] prevent  the list from being modified it copy the list



#passing arbitrary num of arguments add (*) before  the argument name

# def  MyFamily(*names):
#     print('those are my family')
#     for  name in names:
#         print(f'-{name.title()}')
# MyFamily('osama','ali','ziad','ahmed')

#!key word  arguments


# def myclass(fname,lname,**sinfo):
#     sinfo['first _name']=fname
#     sinfo['last_name']=lname
#     return sinfo
# print(myclass('osama','ali',age=25,city='cairo'))
#it's  like dictionary but we can't use the same key twice
## *args and **kwargs we can add key-value



#import module
    #we have file  called pizza.py
    # pizza have function  called making_pizza()
    #this is how it looks like
    # def making_pizza(size,*topping):
    # print(f'making  a {size} inch pizza with the following toppings:')
    # for topping in topping:
    #     print(f'-{topping}')
    #when we call function  from another file we use <module name.function name> this is after importing  the module


    


# import pizza
# pizza.making_pizza(16,'pepperoni', 'mushrooms', 'extra cheese')




#importing specific function 
    #we imported  the whole module but we only need one function so we can import it like this
    #using as made us able to call the function what we want
#we can also use as on the file name
#import pizza as p


# from pizza  import making_pizza as mp
# mp(16,'pepperoni', 'mushrooms', 'extra cheese')


#if we want to import all the functions we can say
# from pizza import *
