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

class Credential:
   '''
   Class to create  account credentials, generate passwords and save their information
   '''
   # Class Variables
   credentials_list = []
   profile_credentials_list = []
   @classmethod
   def check_profile(cls, first_name, password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_profile = ''
        for profile in Profile.profiles_list:
            if (profile.first_name == first_name and profile.password == password):
                current_profile = profile.first_name
        return current_profile
