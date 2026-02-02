class Queue:
    def __init__(self):
        self._head = None   # newest element
        self._tail = None   # oldest element
        self._size = 0

    def enqueue(self, data):
        new_node = ListNode(data)

        if self._size == 0:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        value = self._tail.data

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None

        self._size -= 1
        return value

    def __repr__(self):
        values = []
        current = self._head
        while current:
            values.append(str(current.data))
            current = current.next

        plural = '' if self._size == 1 else 's'
        return f"<Queue ({self._size} element{plural}): [{', '.join(values)}]>"
