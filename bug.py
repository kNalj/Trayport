# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:20:53 2021

@author: ldrmic
"""

class Bug:
    def __init__(self, location):
        """
        Constructr for a bug class. Read in a bug from a given file location.
        
        :param location: DESCRIPTION
        :type location: TYPE
        :return: 
        :rtype: NoneType

        """

        self.bug_file_location = location
        self.bug = self.read_bug()
        
        return
        
    def read_bug(self):
        """
        The method assumes that the bug is located in a first line and first 
        column of the file passed to the constructor
        
        :return: Array of strings containing each line where bug is spanning
        :rtype: array[str]

        """
        bug_strings = []
        with open(self.bug_file_location) as f:
            for line in f:
                bug_strings.append(line.strip("\n"))
            
        return bug_strings

    def bug_start(self):
        """
        Find and return the character which starts the bug string to be able to
        find possible bug locations in a file by looking for this char.
        
        :return: First character of the full bug string
        :rtype: str

        """
        if len(self.bug) > 0:
            return self.bug[0][0]
        else:
            raise IndexError("The bug seems to be non existent")

    def bug_size(self):
        """
        A method that finds and returns the size of each line across which the
        bug is spanning.
        
        :return: Array of integers where each value is a length of a line on 
                 which the bug is spanning. If a bug is across 4 lines, it 
                 would return 4 integers with length of the bug in each of 
                 those lines
        :rtype: array[int]

        """
        
        sizes = [len(line) for line in self.bug]
        return sizes