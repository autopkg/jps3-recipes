#!/usr/bin/env python
#
# Copyright 2014 Jason Stanford
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Based on code Copyright 2013 Timothy Sutton 
#    AutoPkg/autopkglib/SparkleUpdateInfoProvider.py
#


import urllib2
from xml.etree import ElementTree

from autopkglib import Processor, ProcessorError
from distutils.version import LooseVersion
from operator import itemgetter

__all__ = ["RhinocerosUrlProvider"]

namespaces = { "x": "http://www.w3.org/1999/xhtml" } # the current ns in web page

class RhinocerosUrlProvider(Processor):
    description = "Attempts to divine download URL for the Rhinoceros *.dmg file, as well as the license key."
    input_variables = {
        "updates_url": {
            "required": True,
            "description": "The URL to the HTML download request page.",
        },
    }
    output_variables = {
        "url": {
            "description": "URL for downloading.",
        },
        "license_key": {
            "description": "Text string of license key as displayed on download page.",
        },
        "mime_type": {
            "description": "MIME Type of download file.",
        },
    }
    __doc__ = description
    
    def main(self):
        """POSTs a request for the download page of Rhinoceros. The POST must provide a 'valid' email address (x@y.z). The resulting HTML contains both the license key text, as well as the URL for the *.dmg file.
        """
        # A little safety net in case the source HTML changes at some point.
        # (Insert gripes about how frustrating ElementTree is here.)
        get_namespace = lambda: re.findall('\{([^\}]*)\}',htmldoc.getroot().tag)[0]

        try:
            request = urllib2.Request(url=url, data=post_data)
            url_handle = urllib2.urlopen(request)
        except:
            raise ProcessorError("Could not open URL %s" % request.get_full_url())

        try:
            htmldoc = ElementTree().parse(url_handle)
            docroot = htmldoc.getroot()
        except:
            raise ProcessorError("Error parsing HTML download request page.")
            

        #items = htmldoc.findall("release[@os='Darwin']")
        # TODO: logic to find the tags/data of interest
        
        #versions = []
        #for item_elem in items:
        #    item = {}
        #    release_major = item_elem.attrib['major']
        #    release_revision = item_elem.attrib['revision']
        #    release_minor = item_elem.attrib['minor']
        #    item["version"] = "%s.%s%s" % (release_major, release_revision, release_minor)
        #    filepath = "current/%s" % item_elem.find('filename').text
        #    item["url"] = urllib2.urlparse.urljoin(url, filepath)
 
        #    if item["url"] is None:
        #        raise ProcessorError("Could not extract download URL in information from entry from feed!")
        #    if item["version"] is None:
        #        raise ProcessorError("Could not extract version information from entry in feed!")
        #    versions.append(item)
        
        self.env["url"] = latest["url"]
        self.output("Found URL %s" % self.env["url"])
        self.env["license_key"] 


if __name__ == "__main__":
    processor = RhinocerosUrlProvider()
    processor.execute_shell
