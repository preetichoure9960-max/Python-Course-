import json

student = {
    "roll_no": 101,
    "name": "Preeti",
    "branch": "Computer Engineering"
}

json_data = json.dumps(student)
#student = json.loads(json_data) ..if used then also ok
print(json_data)

print(student)
print(student["name"])

with open("student.json", "w") as file:#for making a seprate json doc of output
    json.dump(student, file)
    
import json

#with open("student.json", "r") as file:
    #data = json.load(file)

#print(data)
#print(data["name"])
...#if this used without that with open above syntax then same output
