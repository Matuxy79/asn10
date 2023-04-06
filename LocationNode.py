#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

import SuperNode as N
#added a new instance variable current_location to store the location information

#modified the set_next_location and get_next_location methods to call the inherited set_next and get_next methods

#updated the to_string method to correctly display the current location node in the format "*-]-->"

#corrected the error in the if statement that checks for an empty stack, by calling self.get_data().
class LocationNode(N.SuperNode):
    def __init__(self, value=None, next_node=None):
        """
        Purpose: creates an LocationNode with data
        Pre-condition: None
        Post-condition: A LocationNode with the given data is created
        Return: None
        """
        super().__init__(value, next_node)
        self.current_location = None

    def get_current_location(self):
        """
        Purpose:
            returns the current location stored in the node
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns current location stored in the node, or None if it is empty
        """
        return self.current_location

    def get_next_location(self):
        """
        Purpose:
            returns the next location node 
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the next location node , or None if it is empty
        """
        return self.get_next()

    def set_current_location(self, value):
        """
        Purpose:
            sets the value of the current location node
        Pre-conditions:
            None
        Post-condition:
            Current location node now contains the data value
        Return:
            None
        """
        self.current_location = value

    def set_next_location(self, next_location):
        """
        Purpose:
            sets the next location node
        Pre-conditions:
            None
        Post-condition:
            the next field now points to next location node, i.e., next_location
        Return:
            None
        """
        self.set_next(next_location)

    def to_string(self):
        """
        Purpose: Create a string representation of the container.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
        where 1 is the head of the container and 3 is the end of the container
        Pre-conditions: None
        Post_conditions: None
        Return: A string representation of the container.
        """
        # special case: empty stack
        if self.get_data() is None:
            result = 'EMPTY'
        else:
            walker = self
            value = walker.get_current_location()

            result = '[ ' + str(value) + ' |'
            while walker.get_next_location() is not None:
                walker = walker.get_next_location()
                value = walker.get_current_location()

                if walker == self:
                    result += ' *-]-->[ '+str(value)+' |'
                else:
                    result += '  ]-->[ '+str(value)+' |'

            result += ' / ]'

        return result
