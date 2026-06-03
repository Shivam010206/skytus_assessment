age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("You are allowed")
else:
    print("You are not allowed")

if age < 18 or age > 60:
    print("Special condition matched")