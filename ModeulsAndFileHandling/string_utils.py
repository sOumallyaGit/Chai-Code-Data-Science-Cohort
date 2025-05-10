## Reversal of a string

def reversal(str):
    return str[::-1]

## Palindrome check

def palindrome(str):
    if str == str[::-1]:
        return "The String is a palindrome"
    else :
        return "Not a palindrome"
    
## length Check

def length_check(str):
    return len(str)

## Concatenation of str

def concate(str1,str2):
    return str1+str2