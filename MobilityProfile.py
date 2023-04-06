#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

import LocationNode as LN
def create_profile(self, aList):
    """
    Purpose:
        Creates a mobility profile using the given aList 
    Pre-conditions:
        aList: A list of five strings, showing the sequential locations that the user had visited. 
        aList should only have five locations.
    Post-condition:
        A mobility profile is created
    Return: None
    """
    if len(aList) != 5:
        print("Error: aList must have exactly five locations.")
        return

    self.profile = LN.LocationNode(aList[0])
    current_node = self.profile

    for i in range(1, 5):
        next_node = LN.LocationNode(aList[i])
        current_node.set_next_location(next_node)
        current_node = next_node

def compare_profile(self, otherProfile):
    """
    Purpose:
        Compare two mobility profiles. Return True when the two mobility profile as a location matched.
    Pre-conditions:
        otherProfile: Another user's mobility profile for comparison.
        Both self and other profiles must not be None.
    Post-condition:
        None
    Return: True if there is a match, False for otherwise.
    """
    if self.profile is None or otherProfile.profile is None:
        print("Error: Both profiles must not be None.")
        return False

    current_node = self.profile
    other_node = otherProfile.profile

    while current_node is not None and other_node is not None:
        if current_node.get_current_location() == other_node.get_current_location():
            return True
        current_node = current_node.get_next_location()
        other_node = other_node.get_next_location()

    return False
