class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """Append a value to the end of the list."""
        new_node = ListNode(value, prev=self._tail)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def insert(self, index, value):
        """Insert a new node with `value` at position `index`."""
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = ListNode(value)
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
        """Remove and return the last node's value."""
        if self._size == 0:
            return None

        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        if previous_node is None:
            # Only one node
            self._head = self._tail = None
        else:
            previous_node.next = None
            self._tail = previous_node

        value = node_to_remove.data
        del node_to_remove
        self._size -= 1
        return value

    def remove(self, index):
        """Remove the node at the specified index and return its value."""
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        previous_node = current_node.prev
        next_node = current_node.next

        # Update head and tail if necessary
        if previous_node is None:
            self._head = next_node
        else:
            previous_node.next = next_node

        if next_node is None:
            self._tail = previous_node
        else:
            next_node.prev = previous_node

        value = current_node.data
        del current_node
        self._size -= 1
        return value
