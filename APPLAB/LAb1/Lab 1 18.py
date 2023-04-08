def user_input ():
    userinput=int(input("enter mobile no: "))
    if userinput<10000000000:
        return userinput
    else:
        print("invaild input!!!")
        user_input()
mob=str(user_input())
all_nums = set([0,1,2,3,4,5,6,7,8,9])
mob = set([int(i) for i in mob])
missing_nos= mob.symmetric_difference(all_nums)
missing_nos= sorted(missing_nos)
print(missing_nos)