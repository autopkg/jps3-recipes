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

__all__ = ["MeshmixerUrlProvider"]

class MeshmixerUrlProvider(Processor):
    description = "docstring for MeshmixerUrlProvider"
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
        "minimum_os_version": {
            "description": "Minimum version of OS X required to run the application.",
        },
    }
    __doc__ = description
    
    def get_feed_items(self, url):
        """Retrieves XML updated feed data from URL.
        Example:
		<autodesk namespace="acg">
		  <application name="meshmixer">
		    <version current="9005" build_number="10.4.60" />
		    <installer type="application">
		      <file name="Autodesk Meshmixer Windows (x86) Setup" os="Windows" platform="x86" min_os_version="5.1" link="http://labs-download.autodesk.com/us/labs/trials/worldwide/meshmixer/Autodesk_Meshmixer_v2p4_Win32.exe" />
		      <file name="Autodesk Meshmixer Windows (x64) Setup" os="Windows" platform="x64" min_os_version="5.1" link="http://labs-download.autodesk.com/us/labs/trials/worldwide/meshmixer/Autodesk_Meshmixer_v2p4_Win64.exe" />
		      <file name="Autodesk Meshmixer OSX Installer Package" os="OSX" platform="x86_64" min_os_version="10.7" link="http://labs-download.autodesk.com/us/labs/trials/worldwide/meshmixer/Autodesk_Meshmixer_v2p4_MacOS.pkg" />
		    </installer>
		    <installer type="sdk">
		    </installer>
		  </application>
		</autodesk>

        Notes: (1) The 'min_os_version' attribute is *only* defined here, not in the pkg nor 
                   any payload or in Meshmixer.app bundle (ie. no LSMinimumSystemVersion key 
                   either)
               (2) The version[@build_number] is not necessarily accurate to what's in 
                   Meshmixer.app Info.plist (at this time version[@build_number] reports
                   "10.4.60" yet Meshmixer.app's CFBundleShortVersionString is "10.4.62"
                   and from package downloaded from URL in @link from this XML file.
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
       
        file_item = xmldata.find('application/installer/file[@os="OSX"]')
        version = xmldata.find('application/version').get('build_number')

        try:
            assert file_item.get('link')
        except AssertionException as e:
            raise ProcessorError("Error identifying download URL for installer.")

        try:
            assert version
        except AssertionException as e:
            raise ProcessorError("Error identifying version for installer download.")

        item = {}
        item['url'] = file_item.get('link')
        item['minimum_os_version'] = file_item.get('min_os_version')
       
        return item


    def main(self):
        item = self.get_feed_items(self.env.get("updates_url"))
        for i in item:
            self.env[i] = item[i]


if __name__ == "__main__":
    processor = MeshmixerUrlProvider()
    processor.execute_shell
