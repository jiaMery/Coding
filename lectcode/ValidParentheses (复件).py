class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (len(s)%2)==0:
            j=len(s)-1
            for i in range((len(s)/2)):
                if s[i]=="{":
                    if s[j]=="}":
                          j=j-1
                    elif s[i+1]=="}":
                        i=i+1
                        j=j-1
                    else:
                        return False
                else:
                    if s[i] == "}":
                        if s[j] == "{":
                            j = j - 1
                        else:
                            return False
                    else:
                        if s[i] == "(":
                            if s[j] == ")":
                                j = j - 1
                            else:
                                return False
                        else:
                            if s[i] == ")":
                                if s[j] == "(":
                                    j = j - 1
                                else:
                                    return False
                            else:
                                if s[i] == "[":
                                    if s[j] == "]":
                                        j = j - 1
                                    else:
                                        return False
                                else:
                                    if s[i] == "]":
                                        if s[j] == "[":
                                            j = j - 1
                                        else:
                                            return False
                                    else:
                                        return False
            return True
        else:
            print "not"



f=Solution()
f.isValid("{([{}})}")
f.isValid("(){}[]")