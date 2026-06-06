student = {
    "name": "Shivam",
    "city": "Valsad",
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print(reversed_dict)