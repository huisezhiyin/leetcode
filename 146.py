class DLinkNode(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.first = DLinkNode()
        self.last = DLinkNode()
        self.first.next = self.last
        self.last.prev = self.first

    def move_node_to_tail(self, node: DLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.last.prev
        node.next = self.last
        node.prev.next = node
        self.last.prev = node

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node = self.cache[key]
            self.move_node_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node_now = self.cache[key]
            node_now.value = value
            self.move_node_to_tail(node_now)
        else:
            if len(self.cache.keys()) == self.capacity:
                head = self.first.next
                self.first.next = head.next
                head.next.prev = self.first
                self.cache.pop(head.key)
            node_now = DLinkNode(key, value)
            self.cache[key] = node_now

            self.last.prev.next = node_now
            node_now.prev = self.last.prev

            node_now.next = self.last
            self.last.prev = node_now


if __name__ == '__main__':
    l = LRUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    l.put(3, 3)
    print(l.cache)
