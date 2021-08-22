# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:22:30 2021

@author: ldrmic
"""
from bug import Bug
from catcher import Catcher


def main():
    
    location = "bug.txt"    
    bug = Bug(location)
    
    location = "landscape.txt"    
    catcher = Catcher()
    print(catcher.catch(location, bug))
 
if __name__ == "__main__":
    main()