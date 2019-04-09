import pyperclip
import unittest
from plock import Profile, Credential

class TestProfile(unittest.TestCase):
     '''
    Test class that defines test cases for the profile class behaviours.
    Args:
        unittest.TestCase: helps in creating test cases
    '''

    def setUp(self):
        '''
        Function to create a profile account before each test
        '''
        self.new_profile = Profile('mark', 'aguero', 'sergio10')

    def test__init__(self):
        '''
        Test to if check the initialization/creation of profile instances is properly done
        '''
        self.assertEqual(self.new_profile.first_name, 'mark')
        self.assertEqual(self.new_profile.last_name, 'aguero')
        self.assertEqual(self.new_profile.password, 'sergio10')

