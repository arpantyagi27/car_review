def user_input ():
    userinput=int(input("enter a positive no: "))
    if userinput>0:
        return userinput
    else:
        print("invaild input!!!")
        user_input()
number=user_input()
number_str=str(number)
while (number> 0):
    number -= sum([int(i) for i in list(number_str)])
    number_str = list(str(number))
print(number)