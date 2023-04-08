userinput=input("enter the input: ")
alpha=int(0)
num=int(0)
for letter in userinput:
    if letter.isalpha():
        alpha+=1
    elif letter.isnumeric():
        num+=1
print(f"Letter : {alpha}")
print(f"Numbers : {num}")
