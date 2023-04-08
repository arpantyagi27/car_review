password = input("Enter a password ")
count_low = 0
count_upper = 0
count_digit = 0
sc = ['$','#','@','_']
sc_count = 0
if(len(password)<6 or len(password)>16):
    print("Invalid size")
    quit()
else:
      for i in range(0,len(password)):
        if(password[i].isalpha()==True):
            if password[i].isupper()==True :
                count_upper +=1
            elif password[i].islower()==True :
                count_low +=1
        elif(password[i].isdigit()==True):
            count_digit +=1
        elif password[i] in sc:
            sc_count +=1

if(count_low>=1 and count_upper>=1 and count_digit>=1 and sc_count>=1):
    print("Valid Password")
else:
    print("Invalid Password")