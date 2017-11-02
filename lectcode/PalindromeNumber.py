class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x>(-2**31))&(x<(2**31-1)):
            x=str(x)
            i=0
            while((len(x)-1-i)>=i):
                if x[i]==x[(len(x)-1-i)]:
                    i=i+1
                else:
                    return False
            return True
        else:
            return False

r=Solution()
r.isPalindrome(-5546464664)
