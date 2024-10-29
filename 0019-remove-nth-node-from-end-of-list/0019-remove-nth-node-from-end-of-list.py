# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if not head:
            return None


        current = head
        count = 0
        while current: # count number of nodes in list
            count += 1
            current = current.next

        print(f"Linked List Length: {count}")

        if count == 1:
            return None

        current = head
        current_index = 0
        prev = None
        while current: 

            if count - n == 0:
                head = current.next
                break
            
            elif current_index == count - n - 1: # 0 | 2 - 2

                current.next = current.next.next
                break

            
            current = current.next

            current_index += 1

        return head

            