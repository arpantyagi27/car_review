user_input=input("Enter the input")
user_input=user_input.lower()
print(user_input)
letters={}
for le in user_input:
    if letters.get(le)=="None":
        letters[le]=int(1)
    else:
        letters[le]=int(letters[le]+1)
for k in letters:
    print (k,": ",letters[k])
