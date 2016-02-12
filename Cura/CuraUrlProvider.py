#!/usr/bin/env python
#
# Copyright 2015 Jason Stanford
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
# Originally based on code Copyright 2013 Timothy Sutton
#    AutoPkg/autopkglib/SparkleUpdateInfoProvider.py
#

import urllib2
import platform
from distutils.version import LooseVersion
from autopkglib import Processor, ProcessorError

import xml.etree.ElementTree as ET


__all__ = ["CuraUrlProvider"]

CURA_URL_STUB_DEFAULT = 'https://software.ultimaker.com'
CURA_EXT = 'dmg'


class CuraUrlProvider(Processor):
    description = """
    Downloads the developer's update feed (XML or JSON) and returns the 
    URL to download their installer file.
    """
    input_variables = {
        "update_url_stub": {
            "required": False,
            "default": CURA_URL_STUB_DEFAULT,
            "description": "Base url (stub) for update feed files.",
        },
    }
    output_variables = {
        "url": {
            "description": "feed_url for downloading.",
        },
    }
    __doc__ = description

    def parse_xml_feed_make_filepath(self, xml_data):
        """
        Parses the XML feed for the latest (assumedly) stable version, and 
        attempts to construct and return a valid URL path for download.
        """
        try:
            root = ET.fromstring(xml_data)
            for item in root.iterfind('release'):
                if item.get('os').lower() == 'darwin':
                    filename = item.find('filename').text
                    filepath = "current/{fn}".format(fn=filename)
            assert filepath is not None
        except Exception as e:
            raise ProcessorError(
                "Error parsing XML data from feed. ('{}')".format(e))
        return filepath

    def get_latest_feed_file(self, stub_url=CURA_URL_STUB_DEFAULT):
        """Retrieves version feed file."""
        feed_url = '{stub}/latest.{ext}'.format(stub=stub_url, ext='xml')
        try:
            request = urllib2.Request(url=feed_url)
            url_handle = urllib2.urlopen(request)
            feed_data = url_handle.read()
        except:
            raise ProcessorError(
                "Could not open or read update feed url: {u}".format(u=url))
        filepath = self.parse_xml_feed_make_filepath(feed_data)
        return urllib2.urlparse.urljoin(stub_url, filepath)

    def main(self):
        self.env["url"] = self.get_latest_feed_file(self.env["update_url_stub"])
        self.output(
            "Found download Cura download URL: {}".format(self.env["url"]))


if __name__ == "__main__":
    processor = CuraUrlProvider()
    processor.execute_shell
