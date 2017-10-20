##Palindrome
## Oct. 20

def reverse(s):
    # this function reverse the input as a string
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def palindrome(s):
    # this function tests if the string is a palindrome
    return reverse(s) == s
