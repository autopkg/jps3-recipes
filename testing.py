#!/usr/bin/python

import urllib2
from xml.etree import ElementTree as ET
import pprint
import re

download__url = 'http://www.rhino3d.com/download/rhino-for-mac/5.0/wip'
download__post_data = 'email=x%40y.z&direction_next=Next+%3E&current_page=license_info'

class ProcessorError(Exception):
    pass

def main():

    pp = pprint.PrettyPrinter(indent=4).pprint
    get_namespace = lambda  : { "x": re.findall('\{([^\}]*)\}',htmldoc.getroot().tag)[0] }
    check_text    = lambda s: re.findall('license.*(key)?.*install', x, re.IGNORECASE)

    try:
        request = urllib2.Request(url=download__url, data=download__post_data)
        url_handle = urllib2.urlopen(request)
    except:
        raise ProcessorError("Could not open URL %s" % request.get_full_url())

    try:
        htmldoc = ET.parse(url_handle)
        docroot = htmldoc.getroot()
        namespace = get_namespace() # Ex. {"x": "http://www.w3.org/1999/xhtml"}
    except:
        raise ProcessorError("Error parsing HTML download request page.")
    
    try:
        download_link = docroot.find("x:body//x:a[@class='btn download_link']", namespace).get('href')
        pp(download_link)
    except Exception as e:
        raise e
    
    try:
        p = ( e for e in docroot.find("x:body//x:p", namespace) if check_text() )
        
    except Exception as e:
        raise e
    
    #self.env["url"] = latest["url"]
    #self.output("Found URL %s" % self.env["url"])
    #self.env["license_key"] 

if __name__ == '__main__':
    main()
