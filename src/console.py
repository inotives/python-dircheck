'''
Created on Sep 3, 2013

@author: t_tonit
'''
from htmlbrokenlinkcheck import BrokenLinkCheck as chklink 
import os, sys

if __name__ == '__main__':
    
    choice = None
    while choice != '0':
        print 'Collection of script for Auto Checking files\n',
        print '(1) Empty link Checker\n',
        print '(2) Object ARX header folder diff checking\n',
        print '(0) Exit',
        print ('Choose the Choice:'),
        choice = raw_input()
        if choice == '1':
            print 'Welcome to Link Checker Script - Written by Toni'
            print '-----------------------------------------------------'
            print 'Please key in the directory to be check(e.q. c:/files/folder1):'
            
            dir2bcheck = raw_input() # 'C:/ravi/files'
            chklink().BrokenLinkChecker(str(dir2bcheck))
        
        if choice == '2':
            pass
        
        if choice == '0':
            sys.exit()
        
        else:
            print ('<-- Wrong input, please choose again!! --> ')