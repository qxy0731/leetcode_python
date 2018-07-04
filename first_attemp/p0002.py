# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = l3 = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            l3.next = ListNode((v1 + v2 + carry) % 10)
            carry = (v1 + v2 + carry) // 10
            l3 = l3.next
        return result.next
# trick
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     n1 = ''
    #     while l1:
    #         n1 = str(l1.val) + n1
    #         l1 = l1.next
    #     n2 = ''
    #     while l2:
    #         n2 = str(l2.val) + n2
    #         l2 = l2.next
    #     n3 = str(int(n1) + int(n2))
    #     result = l3 = ListNode(0)
    #     for i in range(1,len(n3) + 1):
    #         l3.next = ListNode(int(n3[-i]))
    #         l3 = l3.next
    #     return result.next
