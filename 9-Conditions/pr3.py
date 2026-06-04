signal = input("enter a signal (red, yellow, green):").lower()

if signal == "red" :
    print("stop")
elif signal == "yellow":
    print("ready")
elif signal == "green":
    print("go")
else:
    print("invalid signal")
    
