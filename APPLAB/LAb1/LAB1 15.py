nos=int(input("No of inputs"))
nums=[]
for i in range (0, nos):
    userinput=int(input("Enter no: "))
    nums.append(userinput)
length=len(nums)
if length== len(set(nums)):
    print("Every no is different")
else:
    print("Every no is not different")