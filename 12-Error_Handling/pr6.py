age = int(input("Enter age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above")

    print("Valid age")

except Exception as e:
    print(e)