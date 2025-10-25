# def greeting():
#     name=input("enter the name:")
#     course=input("enter the course")
#     print('welcome',name,'to' ,'course' ,'10k coders')
#     print(f'welcome {name} to {course} 10k coders')

# greeting()    


# def num():
#     a=int(input("enter a number:"))
#     for i in range(a):
#         print(i)
        
# num()
   

# Task: Perform Addition, Substraction, Multiplication, and Division(07/08/2025)


# def num():
#     num1=int(input("enter a number:"))
#     num2=int(input("enter a number:"))
#     print(num1*num2)
# num()






# Parameters:

# def add():
#     a=25
#     b=50
#     print(a+b)
# add()    


# Without parameters:

# Task: Writ four more function for Add, Sub ,Mul, Div.... 
# use return keyword in it also perform some other action on the result obtained from the function.
# def add(a,b):
#     return(a+b)

# print(add(10,20)-10)



# def sub a,b:
#     return(a-b)

# print(sub(30,50)+100)


# def mul(a,b):
#     return a*b

# print(mul(10,30)%20)



# Task: Write a function that takes a list as input and 
# find nut all the even numbers in that list and return sum of those even numbers.

# def evensum(l):
#     sum=0
#     for i in l:
#         if i%2==0:
#             print(i)
#             sum+=i
#     return sum        

#     list1=[1,2,3,4,5,56,7,8,9,10]
#     print('sum of even number is:', evensum(list1))





# defulat parameters: we use default parameters incase we don't pass arguments while function calling.



# def greetings(name, course, institute):
#     print(f'welcome {name} to {course} to {institute}')


# greetings('loka srinivas', 'python', '10k coders')
    

# key node: Arguments


def greetings(name='student', course='your course', institute='your choose institute'):
    print(f'welcome {name} to {course} to {institute}')


greetings()
