class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            print ""   
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                print strs[0][:i]
        else:
            print min(strs)
"gghd"=Solution()
"gghd".longestCommonPrefix("gghfad")

