#!/bin/zsh
#
# clean up downloaded models to avoid munki warning
#

app_title="Topaz {{APPNAME}} AI"  # ex "Topaz Gigapixel AI"
app_resources="/Applications/${app_title}.app/Contents/Resources"

find "${app_resources}/models" ! -user 0 -name "*.tz" -delete

exit 0

