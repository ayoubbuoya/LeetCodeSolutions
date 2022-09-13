#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        indxs = 0
        while current.next != None:
            indxs += 1
            current = current.next
        mid = indxs // 2
        if indxs % 2 != 0:
            mid += 1
        mid_node = head
        i = 0
        while mid_node.next != None and i < mid:
            mid_node = mid_node.next
            i += 1
        return mid_node
# @lc code=end
head = ListNode(1)
second = head.next = ListNode(2)
third = second.next = ListNode(3)

print(Solution().middleNode(head))
