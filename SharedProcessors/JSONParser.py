#!/usr/bin/python
#
# Copyright 2016 Allister Banks/@arubdesu, pls tell me if I screwed it up
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
"""See docstring for JSONParser class"""

from __future__ import absolute_import

import json

from autopkglib import Processor, ProcessorError

try:
    from urllib.request import urlopen  # For Python 3
except ImportError:
    from urllib2 import urlopen  # For Python 2

__all__ = ["JSONParser"]


MASTER_FEED_URL = "https://objective-see.com/products.json"


class JSONParser(Processor):
    #pylint disable=line-too-long
    """Gets download links, based on products from the ObjectiveSee apps master feed
       Assumes handoff to URLDownloader as subsequent step.
       """

    input_variables = {
        "product": {
            "required": True,
            "description":
                "Which product from the objsee feed to fetch.",
        },
        "format": {
            "required": False,
            "description":
                "If multiple formats are provided, (e.g. pkg/dmg/zip)"
                "returns that URL, otherwise chooses zip.",
            "default": "zip",
        },
    }
    output_variables = {
        "url": {
            "description":
                "Returned download URL",
        },
        "version": {
            "description":
                "Returned version from JSON feed",
        },
    }

    description = __doc__

    def main(self):
        """gimme some main"""
        getit = self.env['product']
        full_feed = urlopen(MASTER_FEED_URL, timeout = 3).read()
        full_dict = json.loads(full_feed)
        we_want = full_dict.get(getit)
        if we_want:
            our_format = self.env.get('format', 'zip')
            self.env['url'] = we_want.get(our_format)
            self.env['version'] = we_want.get('version')
        else:
            raise ProcessorError("Product or format not found")


if __name__ == '__main__':
    PROCESSOR = JSONParser()
    PROCESSOR.execute_shell()
