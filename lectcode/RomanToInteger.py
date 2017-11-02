class Solution(object):
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z = z - roman[s[i]]
            else:
                z = z + roman[s[i]]
        return z + roman[s[-1]]
r=Solution()
r.romanToInt("IV")