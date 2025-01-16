"""
Problem 707: Design Linked List 
https://leetcode.com/problems/design-linked-list/description/
"""

class Node: 
    def __init__(self,val):
        self.val = val 
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, index: int) -> int:
        curr = self.left.next 
        while curr and index > 0: 
            curr = curr.next 
            index -= 1
        
        if curr != None and curr != self.right and index == 0: 
            return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.left.next 
        node.prev = self.left 
        self.left.next = node 
        node.next.prev = node 

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.right
        node.prev = self.right.prev 
        self.right.prev = node
        node.prev.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next 
        while curr and index > 0: 
            curr = curr.next
            index -= 1
        if curr and index == 0: 
            node = Node(val)
            node.next = curr
            node.prev = curr.prev
            curr.prev = node 
            node.prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next 
        while curr and index > 0: 
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0: 
            curr.prev.next = curr.next 
            curr.next.prev = curr.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)