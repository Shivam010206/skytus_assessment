def is_armstrong(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    return total == num


num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")