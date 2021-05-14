
def determinePalindrome(str):
    if(" " in str):
        print("not a valid input")
    x = 0
    for i in range (0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            x = 1
        
    if (x==0):
        return "String is a palindrome"
    else:
        return "Not a palindrome"


