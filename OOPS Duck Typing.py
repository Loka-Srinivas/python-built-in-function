# DUCK TYPING:- (Polymorphism)
# It is categorizing an object based on it's features irrespective of its type.


class Dog:
    def walk(self):
        print("Dog can walk")
        
    def speak(self):
        print("it braks")
        
class Horse:
    def walk(self):
        print("Horse can walk")
        
    def speak(self):
        print("It winess")
        
class Venu:
    def walk(self):
        print("Chance dorkithe Parigethura")
        
    def speak(self):
        print("Class lo matram Mataleeadu ra")
        
dog1=Dog()

horse1=Horse()  

venu1=Venu()      

def checking(being):
    being.walk()
    being.speak()
    print("Yes this is a animal")
    print("_______________________")   
    
    
checking(dog1)

checking(horse1)

checking(venu1)                     





class Phone:
    def work(self):
        print("It is Phone work")
        
    def speed(self):
        print("very speed")
        
class Watch:
    def work(self):
        print("It Is Titan model")
        
    def speed(self):
        print("serious 18")
        
class Saleem:
    def work(self):
        print("Saleem is a person")
        
    def speed(self):
        print("Saleem use the fast runner")
        print("Saleem is a human being")
 
 
 #objects
        
phone1=Phone()

watch1=Watch()  

saleem1=Saleem()      

#Duck Typing Function

def checking(being):
    being.work()
    being.speed()
   
    print("Yes It Is A Electronic Devices")
    print("_______________________")   
    
   #Calls
    
checking(phone1)

checking(watch1)

checking(saleem1)           