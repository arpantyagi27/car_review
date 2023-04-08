import string
import random
n = int(input("Enter length of your string "))
res = ''.join([random.choice( string.ascii_uppercase + string.digits) for i in range(n)])
print("Random String: ",res)