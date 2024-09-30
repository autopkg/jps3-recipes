#!/bin/zsh
#
# (munki) postinstall_script
#
#  - supports current, non-deprecated pkg-based installers
#      (ex. Gigapixel, Photo)
#
#  - installer pkg script ('install-psplugin') assumes it
#      is being executed within context of user at gui
#      console; when installed via munki some aspects "fail"
#      silently
#
#

app_title="Topaz {{APPNAME}} AI"
app_resources="/Applications/${app_title}.app/Contents/Resources"

# adobe photoshop plugins are bundles with .plugin extension
adobe_ps_plugins_srcs=(
 "${app_resources}"/*.plugin(N)
)

# adobe photoshop plugin destination
adobe_ps_plugins_dsts=(
 "/Applications/Adobe Photoshop 202"[0-9]"/Plug-ins"(N)
 "/Library/Application Support/Adobe/Plug-ins/CC"(N)
)

# copy *.plugin bundles to destinations
for dst in $adobe_ps_plugins_dsts; do
 if [[ -d "$dst" ]]; then
   for src in $adobe_ps_plugins_srcs; do
     printf 'Copying "%s" to "%s" ... ' "$src" "$dst"
     cp -Rp "${src}" "${dst}/" && print "done." || print "error?"
   done
 fi
done

# ensure correct permissions for models
chmod -R -v -v 0777 \
  "${app_resources}/models/"

exit 0

