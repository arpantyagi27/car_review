userinput=input("Enter a string : ")
ruserinput=""
length=len(userinput)
for i in range (length-1,-1,-1):
    ruserinput+=userinput[i]
print(ruserinput)
