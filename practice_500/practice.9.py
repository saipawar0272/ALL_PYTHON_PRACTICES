import json

student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)