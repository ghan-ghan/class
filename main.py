


# class parent:
#     def __init__(self, fname , lname) :
#         self.name = fname 
#         self.lname = lname 
        
        
        
#     def generataion(self):
#         return "First Generation"
    
    
    
    
# class child(parent):
#     def __init__(self, fname , lname , contact ):
#         self.contact = contact
#         parent.__init__(self,fname , lname )
        
        
        
#     def generatation(self):
#         return "Second Genertaion"


# # child1 = child("anna", "nndnd",00)
# # print(child1.generatation())

# class grandchild (child):
#     def _init_(self,fname , lname , contact, email):
#         self.email = email 
#         child.__init__(self, fname , lname , contact )
        
        
#     def generatation (self):
#         return "Third Genertaion"
    
    
#     def email_get(self):
        
#         return "your email id "
    
#     def print_name(self):
#         print("first_name" , self.name)
#         print("second_name" ,self.lname)
#         print(self.email)


# # child2 = grandchild("aaa",93939, "ghahha@gnail")
# # print(child2.generatation())
# # print(child2.email_get())
# # print(child2.email_gman = child("nae","an",000)
# child1 = grandchild("anna",000,00)
# print(child1.generatation())
# # print(child1.print_name())


# child1 = grandchild("name",33,'google@gmail.com')
# print(child1.print_name())


# class person :
#     def display(self):
#         print("hello ")



# p= person()
# p.display()


# class person:
#     def __init__(self, name ):
#         self.name = name 
        
#     def display(self):
#         print(self.name)
    
    
# p = person("amul").display()


# class student:
#     college = "Trichandra"
    
#     def __init__(self, rollno, name ):
#         self.name = name 
#         self.rollno = rollno 
        
        
#     def display (self):
#         print(self.name)
#         print(self.rollno)
#         print(student.college )
        
# student1 = student("001","hello ")
# student1.display()
        

#ise)
class animal :
    def eating(self):
        print("eating")
 
class dog(animal):
    def bark(self):
        
        print("bark")
        
        
d = dog ()
d.eating()
d.bark()
    
    
class animal :
    def __init__(self, name):
        self.name = name


class dog(animal):
    def display(self):
        print(self.name)
        
        
d = dog("hellodog")
d.display()



class  person  :
    def display(self):
        print("hello o ")
        
#     def __init__(self, name ):
#         self.name = name
        
        
        
        
class  employee(person) :
    def printing(self):
        print("hello .himal")
        
class programmer(employee):
    def show(self):
        print("Hellow i am the third man ")
        
p = programmer()
p.display()
p.printing()
p.show()
    
    
class land_animal:
    def printing(self):
        print("hello")
        
class water_animal:
    def shows(self):
        print("hellooooo")
        
class frog(land_animal, water_animal):
    pass 

f = frog()
f.shows()
f.printing()


class A:
    def display(self):
        print("mehtii")
        
class B :
    def display (self):
        print("dddd")
        
b =B()
b.display()


#Encapsualtion
class car :
    def __init__(self):
        self.__updatesoftware()
        
    def drive(self):
        print("driving")
        
    def __updatesoftware(self):
        print("updating software")
        
        
b= car ().drive()

class car :
    __maxspeed = 0 
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "supercar "
        
    def drive (self):
        print("driving")
        print(self.__maxspeed)
        
c = car ().drive()
        


