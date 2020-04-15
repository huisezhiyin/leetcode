# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head
        while p:
            next_origin = p.next.next
            p.next.next = next_origin.next if next_origin else None
            p.next.random = p.random.next if p.random else None
            p = next_origin
        return head.next
if __name__ == '__main__':
    s = Solution()
    s.copyRandomList()