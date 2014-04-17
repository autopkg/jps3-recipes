#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET
from autopkglib import Processor, ProcessorError

__all__ = ["PathFinderURLProvider"]


class PathFinderURLProvider(Processor):

    description = "Provides URL for the latest version of PathFinder 6"
    input_variables = {}
    output_variables = {
        "version": {
            "description": "Version of the PathFinder download.",
        },
        "url": {
            "description": "URL to the latest PathFinder 6 release download.",
        },
    }
    __doc__ = description



    def main(self):
        """Identify and return the download URL for the latest version of PathFinder 6"""
        update_url = "%s/%s" % (self.env['UPDATE_XML_HOST'], self.env['UPDATE_XML_PATH'])
        try:
            f = urllib2.urlopen(update_url) 
            xml = f.read()
            doc = ET.fromstring(xml)
        except BaseException as e:
            raise ProcessorError("Unable to download %s: %s" (update_url, e))
        else:
            self.env["url"] = doc.find('url').text
            self.output("Found URL for update download: %s" % self.env["url"])
            self.env["version"] = doc.find('version').text
            self.output("Found version for update download: %s" % self.env["version"])
            


if __name__ == '__main__':
    processor = PathFinderURLProvider()
    processor.execute_shell()


# Example returned data:
# <?xml version="1.0" encoding="utf-8"?>
# <item>
#     <build>1561</build>
#     <version>6.5.3</version>
#     <minOS>10.7</minOS>
#     <url>http://get.cocoatech.com/PF6_LION.zip</url>
#     <notes><![CDATA[
#         <h3>Path Finder 6.5.3 is now available!</h3>
#         <p>Changes:</p>
#         <p><b>1.</b> Fixes to some instability issues introduced in 6.5.2</p>
#         ]]>
#     </notes>
# </item>
