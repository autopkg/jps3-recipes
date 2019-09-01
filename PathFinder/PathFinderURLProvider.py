#!/usr/bin/env python

from __future__ import absolute_import
import xml.etree.ElementTree as ET
from autopkglib import Processor, ProcessorError

try:
    from urllib.request import urlopen  # For Python 3
except ImportError:
    from urllib2 import urlopen  # For Python 2

__all__ = ["PathFinderURLProvider"]


class PathFinderURLProvider(Processor):

    description = "Provides URL for the latest version of PathFinder."
    input_variables = {}
    output_variables = {
        "version": {
            "description": "Version of the PathFinder download.",
        },
        "url": {
            "description": "URL to the latest PathFinder release download.",
        },
    }
    __doc__ = description



    def main(self):
        """Identify and return the download URL for the latest version of PathFinder"""
        update_url = "%s/%s" % (self.env['UPDATE_XML_HOST'], self.env['UPDATE_XML_PATH'])
        try:
            f = urlopen(update_url)
        except BaseException as e:
            raise ProcessorError("Unable to download %s: %s" % (update_url, e))

        try:
            xml = f.read()
            doc = ET.fromstring(xml)
        except BaseException as e:
            raise ProcessorError("Error attempting to parse XML data from update feed at: %s (Error: %s)" % (update_url, e) )
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
#     <build>1672</build>
#     <version>7.1.1</version>
#     <minOS>10.7</minOS>
#     <url>http://get.cocoatech.com/PF7.zip</url>
#     <notes><![CDATA[
#         <center><img src="http://sparkle.cocoatech.com/upgrade_header.png" width="560" height="94"></center>
#         <font face="lucida grande" size=2>
#         <center><h2>Path Finder 7.1.1 is now available!</h2></center>
#         <p><b>News, changes and improvements:</b></p>
#         <ul>
#             <li>Improved file copying between different disks/volumes.</li>
#             <li>Fixed keyboard selection in the column view.</li>
#             <li>Fixed scrolling of the first item in the list view in Yosemite.</li>
#             <li>Fixed memory leak when previewing PDF documents in Yosemite.</li>
#             <li>Fixed drawing of the Sidebar in shelf modules in Yosemite.</li>
#             <li>Other minor fixes and performance and stability improvements.</li>
#         </ul>
#         </font>
#     ]]>
#     </notes>
# </item>
