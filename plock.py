import random
import string
import pyperclip

# 
global profiles_list

class Profile:
    '''
    Class to create and save profile information
    '''
    # Class Variables
    # global profiles_list
    profiles_list = []

    def __init__(self, first_name, last_name, password):
        '''
        Method to define each profile object properties.
        '''

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_profile(self):
        Function to save a newly created user instance
        '''
        Profile.profiles_list.append(self)
