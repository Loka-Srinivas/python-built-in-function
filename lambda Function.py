# lambda with single arguments:
sq= lambda x:x*x
print(sq(6))


#lambda with two arguments:
add=lambda a,b: a+b
print(add(4,5))

#lambda with default arguments:
default1=lambda a=10,b=20: a+b
print(default1())



#nested lambda:
mul1=lambda x: lambda y: x*y
print(mul1(3)(4))

#lambda with no arguments:
name=lambda:"venkat"
print(name())



# RECURSION FUNCTION:-