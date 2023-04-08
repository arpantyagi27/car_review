

norow=int(input("No of rows: "))
nocolumn =int(input("No of Columns: "))
row=[]

n=0
for i in range (0,norow+1):
    #print(i)
    column=[]
    for j in range (0,nocolumn+1):
        no=i*j
        #print(j)
        column.append((no))
    row.append(column)
for i in range (0,norow):
    for j in range (0,nocolumn):
        print( row[i][j] ,end =" ")
    print ("\n")