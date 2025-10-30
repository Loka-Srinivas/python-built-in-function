# # OOPs:- Introducation Programs

# class Car:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model
        
        
# car1=Car("audi","A6")
# print(f'The first car is of brand:{car1.brand}')    
# 
# car2=Car("Lamborgini", "Avendator0")
# print(f'The second car is a brand:{car2.brand}')


# class Bike:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model
# bike1=Bike("KTM","Duke") 
# print(f'The Bike is a Full Controal of a Raider:{bike1.brand}')       


class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        
    def engineStart(self):
        print(f'The {self.brand}, {self.model} has started!!!')
        
    def engineStop(self):   
        print('The all new {self.model} has stopped!!!')
        
car1=Car("Audi","A6")
# print(f'The first car is of brand:{car1.brand}')    
car1.engineStart()
car1.engineStop()
car2=Car("Lamborgini", "Avendator0")
# print(f'The second car is a brand:{car2.brand}')




