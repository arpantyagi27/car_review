from operator import length_hint


def palindrome(no, rno):
    sum=0
    sum=int(no)+int(rno)
    sum=str(sum)
    length=len((sum))
    rsum=""
    for i in range (length-1,-1,-1):
     rsum+=sum[i]
    if rsum==sum:
        print(rsum)
    else :
        palindrome(sum, rsum)
userinput=input("Enter a no: ")
reverseno=""
length=len(userinput)
for i in range (length-1,-1,-1):
    reverseno+=userinput[i]
palindrome(userinput, reverseno)