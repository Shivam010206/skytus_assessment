def simple_interest(p, r, t):
    return (p * r * t) / 100


principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

print("Simple Interest =", simple_interest(principal, rate, time))