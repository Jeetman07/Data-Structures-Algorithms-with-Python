class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise ValueError
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        Raises ValueError if node has two children.
        """
        if node is None:
            return

        # If node has two children → not allowed
        if node._left_child and node._right_child:
            raise ValueError("Cannot detach node with two children")

        parent = node._parent
        child = node._left_child if node._left_child else node._right_child

        # Case 1: Node is root
        if parent is None:
            self._root_node = child
            if child:
                child._parent = None

        else:
            # Replace parent's reference
            if parent._left_child == node:
                parent._left_child = child
            else:
                parent._right_child = child

            if child:
                child._parent = parent

        # Clean up detached node connections
        node._parent = None
        node._left_child = None
        node._right_child = None
