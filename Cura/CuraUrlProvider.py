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
# Based on code Copyright 2013 Timothy Sutton 
#    AutoPkg/autopkglib/SparkleUpdateInfoProvider.py
#


import urllib2
import platform
import json

from autopkglib import Processor, ProcessorError
from distutils.version import LooseVersion

__all__ = ["CuraUrlProvider"]

CURA_URL = 'http://software.ultimaker.com/latest.json'
CURA_EXT = 'dmg'

class CuraUrlProvider(Processor):
    description = "docstring for CuraUrlProvider"
    input_variables = {}
    output_variables = {
        "url": {
            "description": "CURA_URL for downloading.",
        },
    }
    __doc__ = description
    
    def get_latest_json(self, url):
        """Retrieves 'latest.json' file"""
        request = urllib2.Request(url=url)

        try:
            url_handle = urllib2.urlopen(request)
        except:
            raise ProcessorError("Could not open CURA_URL %s" % request.get_full_url())

        data = url_handle.read()

        try:
            latest = json.loads(data)
        except:
            raise ProcessorError("Error parsing JSON data from {}.".format(url))

        zeropad = lambda i: "{:02d}".format(i)
        getdatum = lambda s: latest['cura']['Darwin'][s]

        release_major = getdatum('major')
        release_minor = zeropad(getdatum('minor'))
        release_revision = zeropad(getdatum('revision'))
        filepath = "{maj}.{min}/Cura-{maj}.{min}.{rev}-{sys}.{ext}".format(
                        maj=release_major, min=release_minor, rev=release_revision, sys=platform.system(), ext=CURA_EXT)
        try:
            self.env["url"] = urllib2.urlparse.urljoin(url, filepath)
        except:
            raise ProcessorError("An error occured when attempting to construct the download URL from the latest.json update data.")

        return


    def main(self):
        self.get_latest_json(CURA_URL)
        self.output("Found download Cura download URL: {}".format(self.env["url"]))


if __name__ == "__main__":
    processor = CuraUrlProvider()
    processor.execute_shell
