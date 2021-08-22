# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:20:53 2021

@author: ldrmic
"""

class Bug:
    def __init__(self, location):
        """
        
        :param file: DESCRIPTION
        :type file: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """

        self.bug_file_location = location
        self.bug = self.read_bug(self.bug_file_location)
        
        
    def read_bug(self, file):
        """
        The method assumes that the bug is located in a first line and first 
        column of the file that is passed for reading
        
        :param file: DESCRIPTION
        :type file: TYPE
        :return: DESCRIPTION
        :rtype: TYPE

        """
        bug_strings = []
        with open(self.bug_file_location) as f:
            for line in f:
                bug_strings.append(line.strip("\n"))
            
        return bug_strings

    def bug_start(self):
        """
        
        :return: DESCRIPTION
        :rtype: TYPE

        """
        if len(self.bug) > 0:
            return self.bug[0][0]
        else:
            raise IndexError("The bug seems to be non existent")

    def bug_size(self):
        """
        
        :return: DESCRIPTION
        :rtype: TYPE

        """
        
        sizes = [len(line) for line in self.bug]
        return sizes