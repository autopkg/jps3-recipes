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

__all__ = ["CuraUrlProvider"]

xml_namespaces = {"atom": "http://www.w3.org/2005/Atom"}

class CuraUrlProvider(Processor):
    description = "docstring for CuraUrlProvider"
    input_variables = {
        "updates_url": {
            "required": True,
            "description": "The URL to the XML update feed.",
        },
    }
    output_variables = {
        "url": {
            "description": "URL for downloading.",
        },
        "version": {
            "description": "Version of the Cura download.",
        },
        "mime_type": {
            "description": "MIME Type of download file.",
        },
    }
    __doc__ = description
    
    def get_feed_items(self, url):
        """Retrieves XML updated feed data from URL.
        Example snippet:
        <cura>
        ...
        	<release os="Darwin" major="14" minor="3" revision="0">
        		<filename>Cura-14.03-MacOS.dmg</filename>
        	</release>
        ...
        </cura>
        """
        request = urllib2.Request(url=url)

        try:
            url_handle = urllib2.urlopen(request)
        except:
            raise ProcessorError("Could not open URL %s" % request.get_full_url())

        data = url_handle.read()

        try:
            xmldata = ElementTree.fromstring(data)
        except:
            raise ProcessorError("Error parsing XML from appcast feed.")

        items = xmldata.findall("release[@os='Darwin']")
        
        versions = []
        for item_elem in items:
            item = {}
            release_major = item_elem.attrib['major']
            release_revision = item_elem.attrib['revision']
            release_minor = item_elem.attrib['minor']
            item["version"] = "%s.%s%s" % (release_major, release_revision, release_minor)
            filepath = "current/%s" % item_elem.find('filename').text
            item["url"] = urllib2.urlparse.urljoin(url, filepath)

            if item["url"] is None:
                raise ProcessorError("Could not extract download URL in information from entry from feed!")
            if item["version"] is None:
                raise ProcessorError("Could not extract version information from entry in feed!")
            versions.append(item)

        return versions



    def main(self):
        def compare_version(a,b):
            return cmp(LooseVersion(a), LooseVersion(b))

        items = self.get_feed_items(self.env.get("updates_url"))
        sorted_items = sorted( items, key=itemgetter("version"), cmp=compare_version)
        latest = sorted_items[-1]
        self.env["version"] = latest["version"]
        self.output("Version retrieved from update feed: %s" % latest["version"])
        self.env["url"] = latest["url"]
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    processor = CuraUrlProvider()
    processor.execute_shell
