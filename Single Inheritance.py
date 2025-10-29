#SINGLE INHERITANCE:-

class Parent:
    def greet(self):
        print("Thy great and provide hospitallity!!")
        
class Child(Parent):
    pass        

c1=Child()

c1.greet()


         #OR



class Parent:
    def greet(self):
        print("Thy great and provide hospitallity!!")
        
class Child(Parent):
    def heist(self):
        print("Enact hospitallity to take money from relatives")
    pass        

c1=Child()

c1.greet()

c1.heist()


class Parent:
    def Land(self):
        print("A land tharatharalluga nadhi")
        
class Child(Parent):
    def Own(self):
        print("This my land")   
        pass       

c1=Child()

c1.Land()

c1.Own()
#-----------------------------------------------------------------------------------------------------------------------------------------------


#MULITPLE INHERITANCE:-


class Father:
    def skill(self):
        print("Driving and padesi Kottudu")
        
class Mother:
    def skill(self):
        print("Cocking and double agent")
        
class Child(Father, Mother):
    def skill(self):
        father.skill()
        mother.skill()
        print("python Developer")
        
        
father=Father()
mother=Mother()

prasanna=Child()

prasanna.skill()        


     #OR             
     
     
class Friend1:
    def course(self):
        print("Python Course Choice")
        
class Friend2:
    def course(self):
        print("Java Course Chouce")     
        
class Friend3(Friend1,Friend2):
    def course(self):
        print("My course is SQL")
        
        
friend1=Friend1()
friend2=Friend2()

friend3=Friend3()  
friend3.course()  
 
#-----------------------------------------------------------------------------------------------------------------------------------------------
                  
                  
#MULTI-LEVEL INHERITANCE:-

class School:
    def knowledge(self):
        print("Gaynam Ra Metharamma") 
        
class College(School):
    def skills(self):
        print("Devuni Karugukuthoonammu Exam Marks Akuvaga ravalli Anni")
        
class Institute(College):
    def usefulskills(self):
        print("Master of Computer Applications")  
        
        
student1=Institute()               
student1.knowledge() 
student1.skills()  
student1.usefulskills()             

        #OR


class School:
    def knowledge(self):
        print("Dreams") 
        
class College(School):
    def skills(self):
        print("AMMAILNI PADEDDHAMANNI")
        
class Institute(College):
    def usefulskills(self):
        print("Master of Computer Applications")  
        
        
msnvl1=Institute()               
msnvl1.knowledge() 
msnvl1.skills()  
msnvl1.usefulskills()   


#---------------------------------------------------------------------------------------------------------------------------------------------

# HIERARCHICAL INHERITANCE:-



class Vehicle:
    def fuel(self):
        print("All vehicle use fuels")
        
class Car(Vehicle):
    def petrol(self):
        print("This car uses petrol")
        
class Bike(Vehicle):
    def petrol(self):
        print("Bike uses the petrol")
        
        
        
car1=Car() 
car1.fuel()
car1.petrol()  
car1.petrol()                 



#---------------------------------------------------------------------------------------------------------------------------------------------



#HYBRID INHERITANCE:-



class Parent:
    def work(self):
        print("i can work")
        
class Child1(Parent):
    def skill(self):
        print("i have playing")
        
class Child2(Parent):
    def skill(self):    
        print("i can dance")
        
class GrandChild(Child1, Child2)  :
    def sleep(self) :
        print("i can sleep")
        
GrandChild1=GrandChild()   
GrandChild1.work()
GrandChild1.skill() 
GrandChild1.skill()
GrandChild1.sleep()   

print(GrandChild.__mro__) 


class Restauarnt:
    def bill(self):
        print("how much")
        
class Rajesh(Restauarnt):
    def paid(self):
        print("they paid noo.....")
        
class Ramesh(Restauarnt):
    def paid(self):
        print("Naa dhagra 100 ee Uvvnaee Ra")
        
class Rakesh(Restauarnt):
    def paid(self):
        print ("Anna Cleaning Section Akkada")
        
Friend=Rakesh()
Friend.paid()      

print(Rakesh.__mro__)          
      
                   
        
