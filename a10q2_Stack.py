#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

from a10q2_Container import Container

"""The Stack class now inherits all the attributes and methods from the Container class. I have only changed the constructor in the Stack class to call the constructor of the Container class and removed the redundant attributes and methods that are already defined in the Container class. The push(), pop(), and peek() methods are the same."""

class Stack(Container):
    def __init__(self):
        Container.__init__(self)

    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        new_node = self.Node(value, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Purpose
            Removes and returns a data value from the stack.
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None
        """
        assert not self.is_empty(), 'popped an empty stack'

        prev_first_node = self._top
        result = prev_first_node.get_data()
        self._top = prev_first_node.get_next()
        self._size -= 1
        return result

    def peek(self):
        """
        Purpose
            returns the value from the top of given stack
            without removing it
            Note: the stack cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top of the stack
        """
        assert not self.is_empty(), 'peeked into an empty stack'

        first_node = self._top
        result = first_node.get_data()
        return result

