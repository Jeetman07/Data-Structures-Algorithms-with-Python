class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list
        """
        node = ListNode(value)
        if not self._head:
            self._head = node
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        """
        Remove the last element from the list and return its value.
        Returns None if the list is empty.
        """
        # Case 1: empty list
        if self._head is None:
            return None

        # Case 2: only one node
        if self._head.next is None:
            value = self._head.data
            del self._head
            self._head = None
            return value

        # Case 3: more than one node
        current = self._head
        while current.next.next is not None:
            current = current.next

        value = current.next.data
        del current.next
        current.next = None
        return value
