try:
    num = int(input("Enter a number: "))

except Exception as e:
    file = open("error_log.txt", "a")

    file.write(str(e) + "\n")

    file.close()

    print("Error saved to file")