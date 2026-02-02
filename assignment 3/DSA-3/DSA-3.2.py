class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        values = ", ".join(str(v) for v in self)
        plural = "" if self._size == 1 else "s"
        return f"<SinglyLinkedList ({self._size} element{plural}): [{values}]>"

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        current = self._head
        for _ in range(index):
            current = current.next
        current.data = value

    def insert_left(self, value):
        new_node = ListNode(value)

        if self._size == 0:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def insert_end(self, value):
        new_node = ListNode(value)

        if self._size == 0:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def insert_before_index(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.insert_left(value)
            return

        new_node = ListNode(value)
        current = self._head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
            self._tail = new_node

        self._size += 1

    def insert_after_index(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        new_node = ListNode(value)
        current = self._head

        for _ in range(index):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
            self._tail = new_node

        self._size += 1

    def remove_by_value(self, value):
        current = self._head
        previous = None

        while current:
            if current.data == value:
                if previous is None:
                    self._head = current.next
                    if self._head is None:
                        self._tail = None
                else:
                    previous.next = current.next
                    if current == self._tail:
                        self._tail = previous

                self._size -= 1
                return

            previous = current
            current = current.next

        raise ValueError("Value not found")

    def remove_by_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        current = self._head
        previous = None

        for _ in range(index):
            previous = current
            current = current.next

        if previous is None:
            self._head = current.next
            if self._head is None:
                self._tail = None
        else:
            previous.next = current.next
            if current == self._tail:
                self._tail = previous

        self._size -= 1
