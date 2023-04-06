#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

import Node as N
from a10q2_Container import Container

"""In the __init__ method, I called the superclass Container's __init__ method using super(), and then initialize the __back attribute to None. We also access the __size and __front attributes of the superclass using the _Container__size and _Container__front names, respectively.

The rest of the methods are mostly unchanged from the original, except for the slight modifications to use the superclass attributes and methods."""

class Queue(Container):

    def __init__(self):
        """
        Purpose
            creates an empty queue
        """
        super().__init__()
        self.__back = None   # the node chain ends here


    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the queue
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the queue
        Return:
            (none)
        """
        new_node = N.node(value, None)

        if self.is_empty():
            self._Container__front = new_node
            self.__back = new_node
        else:
            prev_last_node = self.__back
            prev_last_node.set_next(new_node)
            self.__back = new_node

        self._Container__size += 1



    def dequeue(self):
        """
        Purpose
            removes and returns a data value from the queue
            Note: the queue cannot be empty!
        Post-condition:
            the first value is removed from the queue
        Return:
            the first value in the queue, or None
        """
        assert not self.is_empty(), 'dequeued an empty queue'

        prev_first_node = self._Container__front
        result = prev_first_node.get_data()
        self._Container__front = prev_first_node.get_next()
        self._Container__size -= 1
        if self._Container__size == 0:
            self.__back = None
        return result


    def peek(self):
        """
        Purpose
            returns the value from the front of queue
            without removing it
            Note: the queue cannot be empty!
        Post-condition:
            None
        Return:
            the value at the front of the queue
        """
        assert not self.is_empty(), 'peeked into an empty queue'

        first_node = self._Container__front
        result = first_node.get_data()
        return result
