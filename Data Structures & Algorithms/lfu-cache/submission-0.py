from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def pop_tail(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.nodes = {}  # key -> node
        self.freqs = defaultdict(DoublyLinkedList)  # freq -> DLL

    def update_freq(self, node):
        freq = node.freq

        self.freqs[freq].remove(node)

        if freq == self.min_freq and self.freqs[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freqs[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.update_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.update_freq(node)
            return

        if self.size == self.capacity:
            lfu_node = self.freqs[self.min_freq].pop_tail()
            del self.nodes[lfu_node.key]
            self.size -= 1

        node = Node(key, value)

        self.nodes[key] = node
        self.freqs[1].add(node)

        self.min_freq = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)