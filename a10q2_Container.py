#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

import Node as N

class Container(object):

    def __init__(self):
        """
        Purpose
            creates an empty container
        """
        self.__size = 0      # how many elements in the container
        self.__front = None  # the node chain starts here
        self.__back = None   # the node chain ends here


    def size(self):
        """
        Purpose
            returns the number of data values in the container
        Return:
            The number of data values in the container
        """
        return self.__size


    def is_empty(self):
        """
        Purpose
            checks if the container has no data in it
        Return:
            True if the container has no data, or false otherwise
        """
        return self.__size == 0


    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the container
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the container
        Return:
            (none)
        """
        new_node = N.node(value, None)

        if self.is_empty():
            self.__front = new_node
            self.__back = new_node
        else:
            prev_last_node = self.__back
            prev_last_node.set_next(new_node)
            self.__back = new_node

        self.__size += 1


    def dequeue(self):
        """
        Purpose
            removes and returns a data value from the container
            Note: the container cannot be empty!
        Post-condition:
            the first value is removed from the container
        Return:
            the first value in the container, or None
        """
        assert not self.is_empty(), 'dequeued an empty container'

        prev_first_node = self.__front
        result = prev_first_node.get_data()
        self.__front = prev_first_node.get_next()
        self.__size -= 1
        if self.__size == 0:
            self.__back = None
        return result


    def peek(self):
        """
        Purpose
            returns the value from the front of the container
            without removing it
            Note: the container cannot be empty!
        Post-condition:
            None
        Return:
            the value at the front of the container
        """
        assert not self.is_empty(), 'peeked into an empty container'

        first_node = self.__front
        result = first_node.get_data()
        return result


    def push(self, value):
        """
        Purpose
            adds the given data value to the container
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the container
        Return:
            (none)
        """
        new_node = N.node(value, self.__front)
        self.__front = new_node
        self.__size += 1


    def pop(self):
        """
        Purpose
            removes and returns a data value from the container.
            Note: the container cannot be empty!
        Post-condition:
            the first value is removed from the container
        Return:
            the first value in the container, or None
        """
        assert not self.is_empty(), 'popped an empty container'

        prev_first_node = self.__front
        result = prev_first_node.get_data()
        self.__front = prev_first_node.get_next()
        self.__size -= 1
        return result
