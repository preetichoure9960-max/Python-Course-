#Numeric Types
myint =int(input("enter a number"))
myfloat = float(input("enter a number"))
mycomplex = 3+4j
print(myint, type(myint))
print(myfloat, type(myfloat))
print(mycomplex, type(mycomplex))

#Text Type
mystring = "Hello, World!"
print(mystring, type(mystring))

#Boolean Type
mybool = True
print(mybool, type(mybool))

#Sequence Types
mylist = [1, 2, 3]
mytuple = ("a", "b", "c")
myset = {1,2,3}
print(mylist, type(mylist))
print(mytuple, type(mytuple))
print(myset, type(myset))
#Mapping Type
mydict = {"name": "John", "age": 30}
print(mydict, type(mydict))