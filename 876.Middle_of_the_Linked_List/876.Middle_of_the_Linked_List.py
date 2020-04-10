import math
import copy

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0

        tempHead = copy.deepcopy(head)
        while(tempHead.next != None):
            count += 1
            tempHead = tempHead.next

        if(int(count) % 2 != 0):
            count += 1
        count = math.ceil(count/2)

        for i in range(int(count)):
            head = head.next

        return head
