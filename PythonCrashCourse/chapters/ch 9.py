# #classes (oop)
# class student:
#     def __init__(self, name, id, age, grade):
#         self.name=name
#         self.id=id
#         self.age=age
#         self.grade=grade
#         self.city='fayoum'
    
    
#     def  present(self):
#         print(f'{self.name.title()} is present')
    
    
#     def  absent(self):
#         print(f'{self.name.title()} is absent')
    
    
#     def   details(self):
#         print(f'Name: {self.name.title()}')
#         print("Welcome to the student management system")
#         print(f'ID: {self.id}')
#         print(f'Age: {self.age}')
#         print(f'Grade: {self.grade}')
#         all_data=f'here is all your data name:{self.name} , id:{self.id} in the id card ,city :{self.city}'
#         return all_data
#     #when we called function in student.details it came with printing function 
#     #but when  we called student.details() it came with return function in print function

# # student1=student('john', 1, 20, 'A')
# # student1.details()
# # student1.present()
# # print(f'you are a good student {student1.name.title()}')
# # print(student1.details())  
# # student1.city='cairo'

# # student2=student('jane', 2, 21, 'B')
# # student2.details()
# # student2.absent()
# # print(f'you are a lazy student {student2.name.title()}')

# # print(student2.details())     
# #we are making    
# class school_name :
#     def __init__(self, name='stem'):
#         self.name=name
       
        

# #we have some important functions related to classes like update and insert 
# #let's talk about child  class and parent class
# class class_room(student):
#     def __init__(self, name, id, age, grade, room_number='a10'):
#         super().__init__(name, id, age, grade)
#         self.room_number=room_number
#         self.school=school_name()
        
        

# myclass=class_room('osama',1,22,'A','B-22')

# print(f'{myclass.name}  is in room {myclass.room_number}\n he is in {myclass.school.name}')    




#!That's it 
#######################################*Thank you python crash course*#######################################################################