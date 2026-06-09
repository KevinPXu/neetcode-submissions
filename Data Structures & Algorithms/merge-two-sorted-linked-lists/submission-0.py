# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = list1
        l2_curr = list2
        if not list1:
            return list2
        
        if not list2: 
            return list1
            
        if list1.val <= list2.val:
            newList = list1
            l1_curr = list1.next
        else: 
            newList = list2
            l2_curr = list2.next

        new_curr = newList
        while l1_curr and l2_curr:
            if (l1_curr.val <= l2_curr.val):
                new_curr.next = l1_curr
                l1_curr = l1_curr.next
                new_curr = new_curr.next
            else: 
                new_curr.next = l2_curr
                l2_curr = l2_curr.next
                new_curr = new_curr.next
        
        if l1_curr:
            new_curr.next = l1_curr

        if l2_curr:
            new_curr.next = l2_curr

        return newList