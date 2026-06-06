numbers = [10, 20, 30]

index = int(input("Enter index: "))

try:
    print(numbers[index])

except IndexError:
    print("Index out of range")