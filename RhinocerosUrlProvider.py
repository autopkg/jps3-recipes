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
# Originally based on code Copyright 2013 Timothy Sutton:
#    AutoPkg/autopkglib/SparkleUpdateInfoProvider.py
#

import urllib
import urllib2
from xml.etree import ElementTree
import re

from autopkglib import Processor, ProcessorError
from distutils.version import LooseVersion
from operator import itemgetter

__all__ = ["RhinocerosUrlProvider"]

class RhinocerosUrlProvider(Processor):
    description = "Attempts to divine download URL for the Rhinoceros *.dmg file, as well as the license key."
    input_variables = {
        "download_form_url": {
            "required": True,
            "description": "The URL to the HTML download request page.",
        },
        "registrant_email": {
            "required": True,
            "description": "Per requirements to download you must provide your email address."
        }
    }
    output_variables = {
        "url": {
            "description": "URL for downloading.",
        },
        "license_key": {
            "description": "Text string of license key as displayed on download page.",
        },
    }
    __doc__ = description

    def make_http_post_data_string():
        # These values determined by capturing the HTTP POST request while using
        # a GUI browser (Google Chrome in this case, 'Inspect Element' is so handy!)
        values = {
            "email": self.env["registrant_email"],
            "direction_next": "Next >",
            "current_page": "license_info",
        }
        return urllib.urlencode(values)

    def main(self):
        """POSTs a request for the download page of Rhinoceros. The POST must provide a 'valid' email address (x@y.z). The resulting HTML contains both the license key text, as well as the URL for the *.dmg file.
        """

        # for parsing out xmlns string
        rgx_namespace = re.compile('\{([^\}]*)\}')
        # for parsing check of reasonably valid @href
        rgx_download  = re.compile(r'^http.*\.dmg$')
        # for parsing check of reasonably valid license key
        rgx_license   = re.compile('^(?:[A-Z0-9]{4}-){4,}(?:[A-Z0-9]{4})$')

        # A little safety net in case the source HTML changes at some point, and
        # their DOCTYPE or xmlns changes.
        get_namespace = lambda  : { "x": re.findall(rgx_namespace, htmldoc.getroot().tag)[0] }

        try:
            request = urllib2.Request( url=download_url, data=make_http_post_data_string() )
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
            assert re.findall(rgx_download, download_link, flags=re.IGNORECASE)
            self.output( "Found installer download URL: {}".format(download_link) )
        except:
            raise ProcessorError("Unable to parse or identify installer download URL.")

        try:
            # TODO: toughen the xpath as the "@class='...'" is probably somewhat 
            # fragile (as per site developer whims)
            license_code = docroot.find("x:body//x:a[@class='btn download_link']/..//x:nobr",namespace).text
            assert re.findall(rgx_license, license_code, flags=re.IGNORECASE)
            self.output( "Found license key on download page: {}".format(license_key) )
        except:
            raise ProcessorError("Unable to parse or identify the license key from download page.")

        self.env["url"] = download_link
        self.env["license_key"] = license_key        

if __name__ == "__main__":
    processor = RhinocerosUrlProvider()
    processor.execute_shell
