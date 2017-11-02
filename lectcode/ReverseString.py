def reverseString(s):
    newString=""
    for i in range(len(s)):
        newString=newString+s[len(s)-1-i]
    print newString
    return newString
reverseString("abcdefgh")