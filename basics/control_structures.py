#if else statment
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")
    
#for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
    
cities = ["pune","mumbai","banglore"]
for city in cities:
    print(city)
    
word = "hello"
for char in word:
    print(char)

for i in range(5):
    print(i)
for i in range(1, 6):
    print(i)
for i in range(1, 10, 3):
    print(i)
    
#while loops
secret_number =int(input("give a number"))
guess = None
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed right!")