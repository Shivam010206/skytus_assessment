balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Enter a valid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)