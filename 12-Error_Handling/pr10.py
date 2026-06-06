email = input("Enter email: ")

try:
    if "@" not in email or "." not in email:
        raise Exception("Invalid Email Format")

    print("Valid Email")

except Exception as e:
    print(e)