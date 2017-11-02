class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict={"{":"}","(":")","[":"]"}
        for char in s:
            if char in dict.keys():
                stack.append(char)
            elif char in dict.values():
                if stack==[] or char!=dict[stack.pop()]:
                    print "no"
                    return False
            else:
                print "no"
                return False
        return stack==[] #to judge the stack whether empty or not ,type(stack==[])=bool



a=Solution()
# a.isValid("{([{}})}")
# a.isValid("(){}[]")
a.isValid("({})()")
# a.isValid("(][(}(])(({]{{){){(]}}}){}))(){(}[{)})[[")