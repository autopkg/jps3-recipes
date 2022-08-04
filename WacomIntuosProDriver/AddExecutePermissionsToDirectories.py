#!/usr/local/autopkg/python

from __future__ import absolute_import

import os
import stat

from autopkglib import Processor, ProcessorError

__all__ = ["AddExecutePermissionsToDirectories"]


class AddExecutePermissionsToDirectories(Processor):

    description = """
        Attempts to correct sloppy installer packaging which include directories
        lacking any execute permissions (ex. Wacom drivers sometimes).
    """
    input_variables = {
        "root_path": {
            "required": True,
            "description": "root path to check."
        },
    }
    output_variables = {}
    __doc__ = description

    S_IX_PERMS = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH

    def has_all_perms(self, path, perms):
        return bool(os.lstat(path).st_mode & perms)

    def fix_permissions(self, path, perms):
        try:
            os.lchmod(path, os.stat(path).st_mode | perms)
        except:
            raise ProcessorError(
                "Error changing mode for: '{p}'".format(p=path))

    def main(self):
        changed_dirs = []
        for path, dirs, files in os.walk(self.env['root_path']):
            for d in dirs:
                sub_path = os.path.join(path, d)
                if not self.has_all_perms(sub_path, self.S_IX_PERMS):
                    self.fix_permissions(sub_path, self.S_IX_PERMS)
                    changed_dirs.append(sub_path)
        self.output("Fixed permissions for: {}".format(changed_dirs))



if __name__ == '__main__':
    processor = PathFinderURLProvider()
    processor.execute_shell()
