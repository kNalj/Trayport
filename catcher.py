# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:23:55 2021

@author: ldrmic
"""

from bug import Bug

class Catcher:
    def __init__(self):
        """
        Constructor for the catcher class
        
        :return: DESCRIPTION
        :rtype: TYPE

        """
        
        bugs = None
    
    def catch(self, file_location, bug)->int:
        """
        A method that goes through a file "f" and finds all occurances of "bug"
        
        :param file_location: File to find bugs in
        :type file_location: str
        :param bug: Type of bug to look for
        :type bug: Bug
        :return: Number of bugs of type Bug, found in file specified by f
        :rtype: int

        """
        caught = 0  # This will be returned as the number of bugs found
        
        possible_bug_locations = []
        row = 0
        column = 0
        
        lines = []
        with open(file_location, "r") as f:
            for line in f:
                column = 0
                for char in line:
                    if char == "|":
                        possible_bug_locations.append((row, column))
                    column += 1
                row += 1

                lines.append(line.strip("\n"))
        
        is_bug = True
        for location in possible_bug_locations:
            row, column = location
            if row < len(lines) - 2:  # To avoid "Index out of range"
                for line, length in enumerate(bug.bug_size()):
                    if lines[row + line][column:column + length] != bug.bug[line]:
                        is_bug = False
            else:
                break
                
            if is_bug:
                caught += 1
            is_bug = True
        
        return caught