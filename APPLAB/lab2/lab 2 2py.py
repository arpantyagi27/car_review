s1 = input("string 1 is : ")
s2 = input("string 2 is : ")
if(s2 == s1[len(s1)-1]+s1[0:len(s1)-1]):
    print("Are two strings Rotationally equal? : True")
else:
    print("Are two strings Rotationally equal? : False")