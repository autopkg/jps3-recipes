#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET
from autopkglib import Processor, ProcessorError

__all__ = ["FfmpegUrlProvider"]

update_url = "http://www.osxexperts.net/ffmpeg/ffmpegexperts.html"

class FfmpegUrlProvider(Processor):
    description = "Provides download URL and version string information for latest ffmpeg binary installer."
    input_variables = {}
    output_variables = {
        "version": {
            "description": "Version of the ffmpeg installer download."
        },
        "url": {
            "description": "URL to the latest ffmpeg installer download."
        },
    }
    __doc__ = description
    
    def main(self):
        """docstring for main"""
        try:
            f = urllib2.urlopen(update_url)
            html = f.read()
            doc = ET.fromstring(html)
            self.env["url"] = None # TODO
            self.env["version"] = None # TODO
        except BaseException as e:
            raise ProcessorError("An error occurred attempting to identify the latest ffmpeg binary download: %s" % (e))


if __name__ == '__main__':
    processor = FfmpegUrlProvider()
    processor.execute_shell()

