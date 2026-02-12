class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        """
        Represents a single node in a Binary Search Tree (BST)
        """
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        """
        Prints the node and its children for debugging purposes.
        """
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        """
        Initializes an empty Binary Search Tree
        """
        self._root_node = None

    def __repr__(self):
        """
        Displays the whole tree
        """
        return f'<Tree: {self._root_node}>'

    # ----------------------------
    # Inserting a new value
    # ----------------------------
    def insert(self, data):
        """
        Inserts a new value into the BST
        """
        current = self._root_node
        parent = None

        # Find where to insert the new node
        while current:
            parent = current
            if data <= current.data:
                current = current._left_child
            else:
                current = current._right_child

        # Create the new node
        new_node = Node(data, parent_node=parent)

        # If tree is empty, new node becomes root
        if parent is None:
            self._root_node = new_node
        # Otherwise, attach new node as left or right child
        elif data < parent.data:
            parent._left_child = new_node
        else:
            parent._right_child = new_node

    # ----------------------------
    # Finding a value in the tree
    # ----------------------------
    def _find(self, data):
        """
        Finds a node containing the given data
        Returns the node if found, else None
        """
        current = self._root_node
        while current:
            if data == current.data:
                return current
            elif data < current.data:
                current = current._left_child
            else:
                current = current._right_child
        return None

    # ----------------------------
    # Deleting a value from the tree
    # ----------------------------
    def delete_node(self, data):
        """
        Deletes a node containing 'data' from the BST.
        Handles all three cases:
        1. Node is a leaf
        2. Node has one child
        3. Node has two children
        """
        # Step 1: Find the node to delete
        node = self._find(data)
        if node is None:
            return  # Value not found, nothing to delete

        # ------------------------
        # Case 1: Node has no left child
        # ------------------------
        if node._left_child is None:
            child = node._right_child  # could be None

            if node._parent is None:
                # Node is root
                self._root_node = child
                if child:
                    child._parent = None
            else:
                # Update parent's pointer
                if node._parent._left_child == node:
                    node._parent._left_child = child
                else:
                    node._parent._right_child = child

                if child:
                    child._parent = node._parent

        # ------------------------
        # Case 2: Node has no right child
        # ------------------------
        elif node._right_child is None:
            child = node._left_child

            if node._parent is None:
                # Node is root
                self._root_node = child
                if child:
                    child._parent = None
            else:
                # Update parent's pointer
                if node._parent._left_child == node:
                    node._parent._left_child = child
                else:
                    node._parent._right_child = child

                if child:
                    child._parent = node._parent

        # ------------------------
        # Case 3: Node has two children
        # ------------------------
        else:
            # Step 3a: Find successor (smallest node in right subtree)
            successor = node._right_child
            while successor._left_child:
                successor = successor._left_child

            # Step 3b: If successor is not the direct child
            if successor._parent != node:
                # Move successor's right child up
                if successor._right_child:
                    successor._right_child._parent = successor._parent
                successor._parent._left_child = successor._right_child

                # Connect successor's right child to node's right child
                successor._right_child = node._right_child
                node._right_child._parent = successor

            # Step 3c: Replace node with successor
            if node._parent is None:
                # Node is root
                self._root_node = successor
            else:
                if node._parent._left_child == node:
                    node._parent._left_child = successor
                else:
                    node._parent._right_child = successor

            successor._parent = node._parent

            # Connect successor's left child
            successor._left_child = node._left_child
            node._left_child._parent = successor

        # Step 4: Clean up the removed node
        node._parent = None
        node._left_child = None
        node._right_child = None
