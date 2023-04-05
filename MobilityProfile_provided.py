import LocationNode as LN

class MobilityProfile(object):
    def __init__(self, aList=None):
        """
        Purpose: creates a mobility profile. If no aList is given, profile is set to None
        Pre-condition:
            aList: A list of five strings, showing the sequential locations that the user had visited.
        Post-condition: A mobility profile is created
        Return: None
        """

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


