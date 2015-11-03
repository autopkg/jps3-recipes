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

# Last Checked: Monday; November 2, 2015
# `latest.xml` appears to be for current stable releases
# `latest.json` appears to be for current beta releases
import json
import xml.etree.ElementTree as ET


__all__ = ["CuraUrlProvider"]

CURA_URL_STUB_DEFAULT = 'http://software.ultimaker.com'
CURA_RELEASE_TYPE_DEFAULT = 'stable'
CURA_EXT = 'dmg'


class CuraUrlProvider(Processor):
    description = """
    Downloads the developer's update feed (XML or JSON) and returns the 
    URL to download their installer file.
    """
    input_variables = {
        "release_type": {
            "required": False,
            "default": CURA_RELEASE_TYPE_DEFAULT,
            "description": "Value can be `stable` (default) or `beta`.",
        },
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

    def parse_json_feed_make_filepath(self, json_data):
        """
        Parses the JSON feed for latest (assumedly) beta version, and attempts to 
        construct and return a valid URL path for download.
        """
        getdatum = lambda s: latest['cura']['Darwin'][s]
        try:
            latest = json.loads(json_data)
            release_major = int(getdatum('major'))
            release_minor = "{:02d}".format(int(getdatum('minor')))
            release_revision = "{:02d}".format(int(getdatum('revision')))
            filepath = "{maj}.{min}/Cura-{maj}.{min}.{rev}-{sys}.{ext}".format(
                maj=release_major, min=release_minor, rev=release_revision,
                sys=platform.system(), ext=CURA_EXT)
            assert filepath is not None
        except Exception as e:
            raise ProcessorError(
                "Error parsing JSON data from feed. ('{}')".format(e))

        return filepath

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
        """Retrieves version feed file, which differs based on `release_type`."""

        if self.env["release_type"].lower() == 'beta':
            feed_url = '{stub}/latest.{ext}'.format(stub=stub_url, ext='json')
        else:
            feed_url = '{stub}/latest.{ext}'.format(stub=stub_url, ext='xml')

        try:
            request = urllib2.Request(url=feed_url)
            url_handle = urllib2.urlopen(request)
            feed_data = url_handle.read()
        except:
            raise ProcessorError(
                "Could not open or read update feed url: {u}".format(u=url))

        mime_type = url_handle.headers.type

        if mime_type == 'application/json':
            filepath = self.parse_json_feed_make_filepath(feed_data)
        elif mime_type == 'application/xml':
            filepath = self.parse_xml_feed_make_filepath(feed_data)
        else:
            raise ProcessorError(
                "No handler for feed Content-Type of '{t}'".format(t=mime_type))

        return urllib2.urlparse.urljoin(stub_url, filepath)

    def main(self):
        self.env["url"] = self.get_latest_feed_file()
        self.output(
            "Found download Cura download URL: {}".format(self.env["url"]))


if __name__ == "__main__":
    processor = CuraUrlProvider()
    processor.execute_shell
