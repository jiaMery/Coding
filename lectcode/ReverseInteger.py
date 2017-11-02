class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            newx=''
            x=str(x)
            itetate=range(len(x))
            itetate.reverse()
            for i in itetate:
                newx=newx+x[i]
            x=int(newx) 
            if x>(2**31-1):
                return 0
            else:
                return x
        else:
            newx=''
            x=str(abs(x))
            itetate=range(len(x))
            itetate.reverse()
            for i in itetate:
                newx=newx+x[i]
            x=-int(newx)
            if x<(-2**31):
                return 0
            else:
                return x
   
