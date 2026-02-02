class ListNode():
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode : {self.data}>'

class DoublyLinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
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

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
    
    def __iter__(self):
        self._iter_index = self._head
        return self

    def __getitem__(self, index):
        """
        Return value at index
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        
        # Return the value
        return current_node.data

    def __setitem__(self, index, value):
        """
        set value at index k with val
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Set the value
        current_node.data = value

    def contains(self, value):
        """
        Returns True if value if found in the list and False if not
        """
        for node_value in self:
            if value == node_value:
                return True
        return False

    def insert_left(self,val):
        '''
        This method is used to append given value to the left of the list i,e on its head
        head is the begining of the list
        '''
        new_node = ListNode(val)
        current_node = self._head
        if self._size ==0:
            self._head = self._tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            self._head = new_node
            self._head.next = current_node
            self._tail = self._tail

        self._size +=1

        return val
    
    def insert_End(self, val):
        '''
        This method is use to append the list i,e insert at the end of the list on its tail
        '''
        new_node = ListNode(val)
        current_node = self._tail
        if self._size ==0:
            self._tail = self._head = new_node
        else:
            old_tail = self._tail
            self._tail.next = new_node
            self._tail = new_node
            new_node.prev = old_tail
        self._size += 1
        return val

    def insert_Before_Node(self,index_val,val):
        '''
        This method inserts the given value into the given index value i,e actual value of the list
        shifting every remeaning nodes to the left of the node 
        '''
        if self._size == 0:
            raise(Exception("Cannot insert between null list"))
        
        node_Value_index = 0
        contains = False

        '''this is to check if the given value is within the list or not if not it throws error else it sets index number and sets 
            contains to ture'''
        for node_val in self:
            print(node_val)
            print(index_val)
            if node_val == index_val:
                contains = True
                break
            node_Value_index +=1
        new_node = ListNode(val)
        previous_node = None
        current_node = self._head
        next_node = None
        
        if contains:
            '''
            Handles both if size of the linded list is 1 or if the insertion is on the head of the list
            it is for double linked list
            '''
            if self._head == self._tail or self._head.data == index_val:
                self._head = new_node
                new_node.prev = None
                current_node.prev = self._head
                new_node.next = current_node

            else:
                for _ in range(node_Value_index):
                    previous_node = current_node
                    next_node = current_node.next
                    current_node = previous_node.next
                else:
                    previous_node.next = new_node
                    new_node.prev = previous_node
                    new_node.next = next_node
                    next_node.prev = new_node

        else:
            raise Exception("Given value not found inside the list")
        self._size += 1  

    def insert_After_Node(self,index_val,val):
        '''
        This method inserts the given value into the given index value i,e actual value of the list
        shifting every remeaning nodes to the left of the node 
        '''
        if self._size == 0:
            raise(Exception("Cannot insert between null list"))
        '''this is to check if the given value is within the list or not if not it throws error else it sets index number and sets 
            contains to ture'''
        node_Value_index = 0
        contains = False
        for node_val in self:
            if node_val == index_val:
                contains = True
                break
            node_Value_index +=1
        new_node = ListNode(val)
        previous_node = None
        current_node = self._head
        next_node = None

        if contains:
            if self._tail.data == index_val or self._head == self._tail:
                old_last_node = self._tail
                self._tail = new_node
                old_last_node.next = self._tail
                new_node.prev = old_last_node
                new_node.next = None
            else:
                for _ in range(node_Value_index):
                    previous_node = current_node
                    current_node = current_node.next
                    next_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = next_node
                next_node.prev = new_node
        else:
            raise Exception("Given value not found inside the list")
        self._size += 1    

    def remove_by_value(self,value):
        if self._size ==0:
            raise Exception("Cannot delete node from empty list")
        node_Value_index = 0
        contains = False
        for node_val in self:
            if node_val == value:
                contains = True
                break
            node_Value_index +=1
        previous_node = None
        next_node = None
        current_node = self._head
        if contains:
            if self._head == self._tail:
                self._head = None
                self._tail = None
            elif value == self._head.data:
                new_head = current_node.next
                new_head.prev = None
                self._head = new_head
            elif value == self._tail.data:
                new_tail = self._tail.prev
                new_tail.next = None
                self._tail = new_tail
            else:
                for _ in range(node_Value_index):
                    previous_node = current_node
                    current_node = current_node.next
                    next_node = current_node.next
                previous_node.next = next_node
                next_node.prev = previous_node
        else:
            raise Exception("Cannot find the given item on list")
        self._size -=1

    def remove_by_index(self, index_no):
        if self._size ==0:
            raise Exception("Cannot delete node from empty list")
        if index_no < 0 and index_no > self._size:
            raise Exception("Index out of bound")
        previous_node = None
        next_node = None
        current_node = self._head
        if self._head == self._tail:
            self = None
        elif index_no == 0:
            new_head = current_node.next
            new_head.prev = None
            self._head = new_head
        elif self._size == (index_no+1):
            new_tail = self._tail.prev
            new_tail.next = None
            self._tail = new_tail
        else:
            for _ in range(index_no):
                previous_node = current_node
                current_node = current_node.next
                next_node = current_node.next
            previous_node.next = next_node
            next_node.prev = previous_node
        self._size -=1

    def remove_by_value(self, value):
        if self._size == 0:
            raise Exception("Cannot delete node from empty list")

        current_node = self._head
        previous_node = None
        found = False

        while current_node:
            if current_node.data == value:
                found = True
                break
            previous_node = current_node
            current_node = current_node.next

        if not found:
            raise Exception("Cannot find the given item in the list")

        # Removing the node
        if previous_node is None:  # removing head
            self._head = current_node.next
            if self._head is None:  # list became empty
                self._tail = None
        else:
            previous_node.next = current_node.next
            if current_node == self._tail:  # removing tail
                self._tail = previous_node

        self._size -= 1

    def remove_by_index(self, index):
        if self._size == 0:
            raise Exception("Cannot delete node from empty list")
        if index < 0 or index >= self._size:
            raise Exception("Index out of bound")

        current_node = self._head
        previous_node = None

        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next

        # Remove the node
        if previous_node is None:  # removing head
            self._head = current_node.next
            if self._head is None:  # list became empty
                self._tail = None
        else:
            previous_node.next = current_node.next
            if current_node == self._tail:  # removing tail
                self._tail = previous_node

        self._size -= 1