noofterms=int(input("Enter the no of term: "))
diff=int(input("Enter the difference between the nos: "))
sum=int(0)
for i in range (1,(noofterms)*diff+1,diff):
    sum+=i
    #print(sum)
print(sum)