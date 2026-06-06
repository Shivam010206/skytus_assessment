text = input("enter a string:")
word = input("enter a word:")

if word in text:
    print(f"{word} is in the text.")
    
else:
    print(f" '{word}'  is not in the text.")