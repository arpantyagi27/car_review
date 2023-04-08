s = input("Enter a string ")
txt = s
length=len(s)
for i in range(length):
    if s[i].isalpha()==False:
        txt=txt.replace(txt[i],"")
print(txt)