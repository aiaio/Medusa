from __future__ import print_function
import time
import re
import sys
import lxml.etree
import lxml.builder
import datetime

from xml.dom.minidom import parse, parseString

from urllib2 import urlopen, HTTPError
from optparse import OptionParser
#from bs4 import BeautifulSoup as bs
from optparse import OptionParser
from urlparse import urlparse
#mport requests

input_site = ""
inputType = ""


def main():
    global input_site
    global inputType
    input_bool = getFile()
    while (input_bool == False):
        input_site = raw_input('Enter website (ex: http://newsite.qa.aistg.com) : ')
                    #clean input or end program
        if input_site == 'quit':
            sys.exit()

                    #check valid site
        if check(input_site):
            break

        print ('Invalid host address.  Please re-enter or type quit to end.')

            #Get all links on site
    inputType = raw_input('(1)To search Images\n(2)To search Links\n: ')
    if inputType == '1':
        links = getLinks(input_site, 'IMG')
    elif inputType == '2':
        links = getLinks(input_site, 'LNK')

    print ('Number of links found: ' + str(len(links)))
            #lets format the output nicely


    output(links)

def output(links):
    returncodes = {}
    link_pos = 1
    num_links = len(links)
    t0 = time.clock()
    for link in links:
        print (link)
    for link in links:
        print ("checking %d of %d" %(link_pos,num_links))
        try:
            code = urlopen(link).getcode()
        except HTTPError as e :
            print('error %d from %s' %(e.code, link))
            code = e.code
        except:
            code= 0

        if code in returncodes:
            returncodes[code].append(link)
        else:
            returncodes[code] = [link]

        link_pos+=1

    print('took %d secs' % (time.clock() - t0))
        #returns themd httpstatus codes that were seen
    print(returncodes.keys())
    httpstatus = None
        #loop to allow the user to print the urls by status code
    while httpstatus != 'quit':
        httpstatus = raw_input('(1) Inspect Broken links\n(2) Enter a new Address\n(3) Run again\n(4) Quit and Write output to file\n: ')
        if httpstatus == '1':
            httpstatus = raw_input("Enter Status code to check: ")
            try:
                for lines in returncodes[int(httpstatus)]:
                    print (lines)
                raw_input('Press Enter to continue.....')
            except:
                print ("Status code not found")
                print(returncodes.keys())

        elif httpstatus == '2':
            main()
        elif httpstatus =='4':
            print ('Writing To XML Log File tempLinks.xml')
            writeFile(links, returncodes)
            sys.exit()
        elif httpstatus =='3':
            output(links)
        else:
            print('Invalid Input')
                #main done

#testes the url to make sure it is valid From Tim b
def check(test_str):
    pattern = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))'
    if not re.search(pattern, test_str):
        valid = False
        print ('Invalid url format : %r' % (test_str,))
    else:
        print ('Valid url format   : %r' % (test_str,))
        valid = True
    return valid

#Returns a list of links on a site
#abstracted in case we want to process HTML in a different way, later
def getLinks(url_string, type_of_link):
    return process(url_string, type_of_link)

#cleans links
def clean(pattern, url):
    urls = {}
    instances = 0
    for link in pattern:
        if link[0:2] == '//':
            print('URL does not specify host, prepending http:')
            link = 'http:'+link
        elif link[0] == '/':
            print('URL does not specify host, prepending '+urlparse(url).hostname)
            link = 'http://'+urlparse(url).hostname+link

    urls[link] = True
    instances += 1
    print('%d Found link %s' % (instances, link))
    return urls

#Process html into dictionary
def process(url, type_of_link):
    #url = host+page
    print('Opening %s...' % url)
    #scrapes the page source
    content = urlopen(url).read()

    print('Compiling RegExp...')
    if type_of_link == 'LNK':
        print("link processing RegEx")
        pattern = re.compile(r'<a .*?href=["|\'](?!#)(.+?)["\']');
    elif type_of_link == 'IMG':
        print("IMG processing for Regex")
        pattern = re.compile(r'<img .*?src=["|\'](?!#)(.+?)["\']');
    # we can avoid duplicates by using a hash - will save time later
    urls = {}
    instances = 0

    for link in pattern.findall(content):

        if link[0:2] == '//':
            print('URL does not specify host, prepending http:')
            link = 'http:'+link
        elif link[0] == '/':
            print('URL does not specify host, prepending '+urlparse(url).hostname)
            link = 'http://'+urlparse(url).hostname+link
        """
        elif link.find('\.com') == -1:
            print('URL does not specify host, prepending '+urlparse(url).hostname)
            link = 'http://'+urlparse(url).hostname+'/'+link
        """

        urls[link] = True
        instances += 1
        print('%d Found link %s' % (instances, link))


    print('Found %d links with %d unique URLs' % (instances, len(urls)))
#list of urls
    return urls.keys()

def getFile():
    print ("[Checking for file]\n")
    try:
        with open('tempLinks.xml'): pass
    except IOError:
        print ("[file not found, using command line for input]\n")
        return False

    choice = raw_input("\nLinks file found\nwould you like to check links in file?\n1:Yes\n2:No ")
    if choice == '1':
        parseFile()
        sys.exit()
    else:
        return False

def readFile():
    links = []
    with open('tempLinks.xml') as file_in:
        for line in file_in:
            links.append(line)

    urls = {}
    instances = 0
    for link in links:
        urls[link] = True
        instances += 1
        print('%d Found link %s' % (instances, link))

    print('Found %d links with %d unique URLs' % (instances, len(urls)))



def writeFile(links, returncodes):
    global inputType
    global input_site
    E = lxml.builder.ElementMaker()
    ROOT = E.root
    DOC = E.doc
    FIELD1 = E.Base
    FIELD2 = E.Code
    now = datetime.datetime.now()
    print (inputType)
    #parse the dom for input_site and inputType
    if inputType == '1':
      name='IMG'
      inputType = 'IMG'
    elif inputType == '2':
      name='LNK'
      inputType = "LNK"
    else:
      name=inputType

    output = ROOT(FIELD1(input_site, name=name))

    for key in returncodes.keys():
        for link in returncodes[int(key)]:
            output.append(FIELD2(link,name=str(key)))

    time_str = str(now.strftime("%Y-%m-%d-%H-%M"))
    timefilename = inputType+"-"
    timefilename = timefilename+str(urlparse(input_site).hostname)
    timefilename = timefilename.replace("\n", "")
    timefilename = timefilename.replace("www.", "")
    timefilename = timefilename.replace(".com", "")
    timefilename+=time_str
    timefilename = timefilename+'.xml'

    try:
        output_temp_file = open("tempLinks.xml", "w+")
        print (str(lxml.etree.tostring(output, pretty_print=True)), file=output_temp_file)
        #Log File Output
        output_log_file = open(timefilename, "w+")
        print (str(lxml.etree.tostring(output, pretty_print=True)), file=output_log_file)
    except:
        print("Unable to open file for writing")

def parseFile():
    global input_site
    global inputType
    lines = []
    cleaned_lines = []
    dom = parse("tempLinks.xml")
    for node in dom.getElementsByTagName('Base'):
      input_site = node.toxml()[1:-7]
    for node in dom.getElementsByTagName('Base'):
      print (node.toxml()[12:15])
      inputType = node.toxml()[12:15]

    for node in dom.getElementsByTagName('Code'):
        lines.append(node.toxml())

    for line in lines:
        #print line[17:-7]
        cleaned_lines.append(line[17:-7])
    cleaned_lines
    output(cleaned_lines)
    sys.ext()

main()




#This is useless but can server as a soup way to process HTML
"""
def tight(soup, type_of_link):
        print("Tight HTML Processing for " +type_of_link)
        links = {}
        if type_of_link == 'IMG':
                print ("Getting all <src img> links and testing link status")
                links = [x['src'] for x in content_soup.findAll('img')] #unclean links list
        if type_of_link == 'LINK':
                print ("Getting all <a href> links and testing link status")
                links = [x['href'] for x in content_soup.findAll('a')]
        cleaned = clean(links, urlparse(url_string).hostname)
        return cleaned
"""


#Previously Used way to check for valid URL.  Now we pass to urlopen and get code.
#So the internet checks for valid url instead of manual regex.



"""
#Boolean check for valid website
def check(url_string):
  if urlopen(url_string).getcode() == 200:
    return True
  else:
    return False
"""
