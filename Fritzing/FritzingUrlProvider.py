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


from __future__ import absolute_import
import urllib2
from xml.etree import ElementTree

from autopkglib import Processor, ProcessorError
from distutils.version import LooseVersion
from operator import itemgetter

__all__ = ["FritzingUrlProvider"]

xml_namespaces = {"atom": "http://www.w3.org/2005/Atom"}

class FritzingUrlProvider(Processor):
    description = "docstring for FritzingUrlProvider"
    input_variables = {
        "updates_url": {
            "required": True,
            "description": "The URL to the ATOM/XML update feed.",
        },
    }
    output_variables = {
        "url": {
            "description": "URL for downloading.",
        },
        "version": {
            "description": "Version of the Fritzing download.",
        },
        "mime_type": {
            "description": "MIME Type of download file.",
        },
    }
    __doc__ = description
    
    def get_feed_items(self, url):
        """Retrieves ATOM/XML updated feed data from URL.
        Like the SparkleUpdateInfoProvider, this also returns an array
        of dicts, one per update <entry> structured like:
        version: 0.8.7b
        url: http://fritzing.org/download/api/1.0/update/311
        description_data: HTML description for update (optional)
        description_url: URL given by entry/link[@rel='alternate']/@href
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
        
        items = xmldata.findall('atom:entry', xml_namespaces)
        
        versions = []
        for item_elem in items:
            item = {}
            link_enclosure = item_elem.find("atom:link[@rel='enclosure']", xml_namespaces)
            if link_enclosure is not None:
                item["url"] = link_enclosure.get('href')
                item["mime_type"] = link_enclosure.get('type')
            title = item_elem.find("atom:title", xml_namespaces)
            if title is not None:
                item["version"] = title.text

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
        self.env["mime_type"] = latest["mime_type"]
        self.output("MIME-Type retrieved from update feed: %s" % latest["mime_type"])


if __name__ == "__main__":
    processor = FritzingUrlProvider()
    processor.execute_shell
