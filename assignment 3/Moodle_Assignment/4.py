class DNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'<DNode: {self.data}>'


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current = self._head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{", ".join(values)}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """Append a value to the end of the list."""
        new_node = DNode(value)
        if not self._head:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._size += 1

    def insert(self, index, value):
        """Insert a new node with `value` at position `index`."""
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = DNode(value)

        if index == 0:
            # Insert at head
            new_node.next = self._head
            if self._head:
                self._head.prev = new_node
            self._head = new_node
            if self._size == 0:
                self._tail = new_node
        elif index == self._size:
            # Insert at tail
            self.append(value)
            return
        else:
            # Insert in middle
            current = self._head
            for _ in range(index):
                current = current.next
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node

        self._size += 1

    def pop(self):
        """Remove the last element and return its value."""
        if self._size == 0:
            return None

        removed = self._tail
        value = removed.data

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = removed.prev
            self._tail.next = None

        del removed
        self._size -= 1
        return value

    def remove(self, index):
        """Remove the node at the specified index and return its value."""
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        if index == 0:
            removed = self._head
            self._head = self._head.next
            if self._head:
                self._head.prev = None
            if self._size == 1:
                self._tail = None
        elif index == self._size - 1:
            return self.pop()
        else:
            removed = self._head
            
