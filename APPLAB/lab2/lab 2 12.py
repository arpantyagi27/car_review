s = input("Enter a string ")
def palindrome(s):
    if(s == s[::-1]):
        print("True")
    else:
        print("False")
palindrome(s)