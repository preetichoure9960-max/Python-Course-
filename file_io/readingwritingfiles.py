with open("student.txt","w") as file:
    file.write("Preeti\n")
    file.write("Computer Engineering\n")#\n is used for breaking it or else it will come without spacing 
    file.close()
    
with open('student.txt', 'a') as file:
    file.write("MIT ADT University\n")
    file.close()

with open('student.txt', 'r') as file: #we have to use it after performin all operations so that it can print the content
    content = file.read()
    print(content)#if we are using this below syntax then we dont have to use this syntax
    
with open("student.txt", "r") as file:
    print("\nReading Line by Line:")
    for line in file:
        print(line.strip())#after writing this we dont have to close the file coz it reads line by line the content 
       
       
       
       #for adding before and after concept 
with open("sample.txt", "w") as file:
    file.write("Python Programming")    
    
with open("sample.txt", "r+") as file:
    print("Before Writing:")
    print(file.read())
    
    file.write("\nFile Handling")
    file.seek(0)
    print("\nAfter Writing:")
    print(file.read())