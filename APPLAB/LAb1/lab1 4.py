#get a string from the user 
letter=input("Give input ")
lenght=len(letter)
reversed=""
for i in range (lenght-1,-1,-1):
    reversed+=letter[i]
print(reversed)