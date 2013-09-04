'''
Created on Sep 3, 2013

@author: t_tonit
'''

import os, sys
from bs4 import BeautifulSoup

class BrokenLinkCheck():
    '''This class is to check any <a> tag in html page which is empty'''
    
    def BrokenLinkChecker(self,directory):
        dirContents = ()
        try:
            dirContents = list(os.listdir(directory)) #list all the files in the directory 
        except (IOError):
            print 'Error: Can\'t find the directory'
        except:
            print 'Error: Not a correct path name'
            
        haveBrokenLink = False
        datain = False
        count = 0
        totalpg = 0
        pgcount = 0
        path_to_script = os.path.dirname(os.path.abspath(__file__)) #locate the path of the script
        output_file = os.path.join(path_to_script, "BrokenLinksCheckResult.txt")#write to local folder of the sccipt
        outputfilehandle = open(output_file,"w+") #creating a file handle to write
        
        for pages in dirContents:
            soup = BeautifulSoup(open( directory + '/' + pages))  #put each of the html pages into soup array  
            totalpg+=1
            print str(totalpg) 
            #find all the <a> tag in the html pages loaded into the soup
            for link in soup.find_all('a'):
                #if the href attribute consist of "" blank, put into the txt files as broken links 
                if (str(link.get('href')) == ""):
                    try:
                        brokenLinksText = str(link.text)
                        brokenLinksText.encode('utf-8',errors='replace')
                        brokenLinksText.encode('ascii',errors='xmlcharrefreplace')
                        outputfilehandle.write ( brokenLinksText + '\n' )
                    except UnicodeEncodeError, Argument: 
                        print 'error occur:', Argument
                    
                    haveBrokenLink = True;
                    count+=1 #counter for broken link in each pages
            #mark the pages as broken link existed pages 
            if (haveBrokenLink):
                haveBrokenLink = False
                outputfilehandle.write ('Topic ID: '+ pages + ' ----> Total Suspected Broken Links = ' + str(count) + '\n\n')
                pgcount+=1 #broken links counter
                count = 0
                print '-Broken Links!-' + pages
            datain = True
        if(datain):
            print 'Completed! - Total Scanned Pages: ' + str(totalpg) + ', Broken Link Pages: ' + str(pgcount)
            datain=False
        outputfilehandle.write ( 
        '\n----------------------------------------------------------\n' +     
        'Total Scanned Pages: ' + str(totalpg) + '\n' +
        'Total Error Pages: ' + str(pgcount) + '\n' +
        '----------------------------------------------------------'
        )        
        