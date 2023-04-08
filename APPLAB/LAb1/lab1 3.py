lines=int(input("Enter no of lines: "))
for i in range (0,int(lines/2)+1):
    for i in range (0,i+1):
        print ("*" ,end=" ")
    print(end="\n")
for i in range (int(lines/2)-1,-1,-1):
    for i in range (0,i+1):
        print ("*" ,end=" ")
    print(end="\n")