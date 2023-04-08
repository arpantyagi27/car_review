l = [2,5,(12,13),98,(12,13),2]
count = 0
for i in l:
    if(type(i) is not tuple):
        count=count+1
print(count)