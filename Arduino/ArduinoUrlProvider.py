#!/usr/bin/env python

# Copyright 2014 Jason P. Stanford
# Adapted original work for use with different googlecode project.
# Work still largely that of original author, with minor changes.

#
# Original Copyright 2013 Greg Neagle
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

import re
import urllib2

from autopkglib import Processor, ProcessorError


__all__ = ["ArduinoUrlProvider"]


RELEASE_BASE_URL = "http://code.google.com/p/arduino/downloads/list"

re_dmg_link = re.compile(r'href="(?P<url>//arduino.googlecode.com/files/arduino-[.0-9]*-macosx.zip)"')


class ArduinoUrlProvider(Processor):
    """Provides a download URL for Arduino IDE."""
    input_variables = {
        "base_url": {
            "required": False,
            "description": "Default is %s" % RELEASE_BASE_URL,
        },
    }
    output_variables = {
        "url": {
            "description": "URL to arduino zip file download.",
        },
    }
    description = __doc__

    def get_arduino_dmg_url(self, base_url):
        # Read HTML index.
        try:
            f = urllib2.urlopen(base_url)
            html = f.read()
            f.close()
        except BaseException as err:
            raise ProcessorError("Can't download %s: %s" % (base_url, err))
        
        m = re_dmg_link.search(html)
        
        if not m:
            raise ProcessorError(
                "Couldn't find arduino download URL in %s" % base_url)
        
        link = urllib2.quote(m.group("url"), safe=":/%")
        if link.startswith("//"):
            link = "http:" + link
        return link
        

    def main(self):
        """Find and return a download URL"""
        base_url = self.env.get("base_url", RELEASE_BASE_URL)
        self.env["url"] = self.get_arduino_dmg_url(base_url)
        self.output("Found URL %s" % self.env["url"])


if __name__ == "__main__":
    processor = ArduinoUrlProvider()
    processor.execute_shell()
