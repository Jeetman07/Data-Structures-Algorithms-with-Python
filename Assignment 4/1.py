class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        return self._top.data if self._top else None

    def push(self, data):
        self._top = Node(data, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            return None

        value = self._top.data
        self._top = self._top.next
        self._size -= 1
        return value

    def __repr__(self):
        values = []
        current = self._top
        while current:
            values.append(str(current.data))
            current = current.next

        content = ", ".join(values)
        element_word = "element" if self._size == 1 else "elements"
        return f"<Stack ({self._size} {element_word}): [{content}]>"
