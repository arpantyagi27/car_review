   # Write a Python program to find those numbers which are divisible by
    #8 and multiple of 5, between 1000 and 2000 (both included)
nos=[]
for no in range (1000,2001):
    if(no%5==0 and no %8==0):
        nos.append(no)
print(nos)
