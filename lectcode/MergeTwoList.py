# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode"""
        l=[]
        for i in set(l1+l2):
            l.append(i)
        return l
a=Solution()
a.mergeTwoLists([1,2,5,8,4,2,3,2],[44,2,89,9,4,2,3,1])