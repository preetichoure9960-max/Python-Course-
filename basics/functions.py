
def greet(name, greet="Hello"):
    print(f"{greet}, {name}!")
    
a=int(input("Enter a number"))
b=int(input("Enter a number"))
def add(a, b):
    return a + b
def diff(a,b):
    return a-b 
greet("John")
result = add(a, b)
print(result)

greet("John")  # Output: Hello, John!
greet(name="John", greet="Hi")  # Output: Hi, John!