#!/bin/zsh
#
# munki postuninstall_script
#
#  supports current, non-deprecated pkg-based installers
#    (ex. Gigapixel, Photo)
#
#  installer pkg script ('install-psplugin') copies and
#    adds items elsewhere in filesystem not reflected
#    in pkg bom so must be cleaned up here
#
#  Note: After inclusion, and before use of this script
#    in a specific recipe, be sure to replace {{APPNAME}}
#    appropriately.
#

app_title="Topaz {{APPNAME}} AI"      # ex "Topaz Gigapixel AI"
apptitle=${app_title// /}             # ex "TopazGigapixelAI"
appname=${(L)${:-{{APPNAME}}}//[{}]/} # ex "gigapixel"

# additional PATH items
rm -f /etc/paths.d/50-com.topazlabs.${appname}

# adobe photoshop plugin destination
adobe_ps_plugins_dsts=(
 "/Applications/Adobe Photoshop 202"[0-9]"/Plug-ins"(N)
 "/Library/Application Support/Adobe/Plug-ins/CC"(N)
)

for dst in $adobe_ps_plugins_dsts; do
  rm -fr "${dst}/${apptitle}"*.plugin
done

exit 0

