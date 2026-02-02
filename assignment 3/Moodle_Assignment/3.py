class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
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
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list
        """
        new_node = ListNode(value)
        if not self._head:
            # Empty list
            self._head = self._tail = new_node
        else:
            # Non-empty list
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list
        """
        if not self._size:
            return None
        
        # Only one node
        if self._size == 1:
            value = self._head.data
            del self._head
            self._head = self._tail = None
            self._size -= 1
            return value

        # More than one node
        current = self._head
        while current.next != self._tail:
            current = current.next

        value = self._tail.data
        del self._tail
        current.next = None
        self._tail = current
        self._size -= 1
        return value

    def insert(self, index, value):
        """
        Insert a new node with value at the specified index
        """
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        previous_node = None
        next_node = self._head
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        new_node = ListNode(value, next_node)

        if previous_node is None:
            # Insert at head
            self._head = new_node
        else:
            previous_node.next = new_node

        if previous_node == self._tail:
            # Insert at tail
            self._tail = new_node

        self._size += 1

    def remove(self, index):
        """
        Remove the node at the specified index and return its value
        """
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        # Remove head
        if index == 0:
            removed_node = self._head
            self._head = self._head.next
            if self._size == 1:
                self._tail = None
            value = removed_node.data
            del removed_node
            self._size -= 1
            return value

        # Remove middle or tail
        previous_node = self._head
        for _ in range(index - 1):
            previous_node = previous_node.next

        removed_node = previous_node.next
        value = removed_node.data
        previous_node.next = removed_node.next

        if removed_node == self._tail:
            self._tail = previous_node

        del removed_node
        self._size -= 1
        return value
