# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cabeza_falsa = ListNode(0)
        actual = cabeza_falsa 

        acarreo = 0

        while l1 or l2 or acarreo:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            suma_total = val1 + val2 + acarreo
            acarreo = suma_total // 10
            digito = suma_total % 10 


            actual.next = ListNode(digito)
            actual = actual.next 

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return cabeza_falsa.next 
         