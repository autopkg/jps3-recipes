# APIs / Scratch
## Additional Notes

- Docs
    - [Topaz Web API](https://api.topaz-labs.net/)
        - [Swagger(?)](https://api.topaz-labs.net/docs)
            - `https://api.topaz-labs.net/openapi.json`
            - `https://github.com/TopazLabs/topaz-web-api/blob/main/README.md#topaz-web-api` _(not public? no longer extant? :shrug:)_
        - `https://api.topaz-labs.net/redoc`


- - - 

# Scratch

`https://api.topaz-labs.net/v2/app_state/unauthed?«query_params»`

`trurl --json …snip…` output

```json
[
  {
    "url": "https://api.topaz-labs.net/v2/app_state/unauthed?app_build_type=RELEASE&app_cname=GIGAPIXEL&app_version=7.4.1&arch=arm64&cpu_supports_avx=true&email_mac=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&license_expiration_datetime=YYYY-MM-DDTHH%3aMM%3aSS&os_type=osx&os_version=15.0&user_email=someemail%40company.tld",
    "parts": {
      "scheme": "https",
      "host": "api.topaz-labs.net",
      "path": "/v2/app_state/unauthed",
      "query": "app_build_type=RELEASE&app_cname=GIGAPIXEL&app_version=7.4.1&arch=arm64&cpu_supports_avx=true&email_mac=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&license_expiration_datetime=YYYY-MM-DDTHH:MM:SS&os_type=osx&os_version=15.0&user_email=someemail@company.tld"
    },
    "params": [
      {
        "key": "app_build_type",
        "value": "RELEASE"
      },
      {
        "key": "app_cname",
        "value": "GIGAPIXEL"
      },
      {
        "key": "app_version",
        "value": "7.4.1"
      },
      {
        "key": "arch",
        "value": "arm64"
      },
      {
        "key": "cpu_supports_avx",
        "value": "true"
      },
      {
        "key": "email_mac",
        "value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      },
      {
        "key": "license_expiration_datetime",
        "value": "YYYY-MM-DDTHH:MM:SS"
      },
      {
        "key": "os_type",
        "value": "osx"
      },
      {
        "key": "os_version",
        "value": "15.0"
      },
      {
        "key": "user_email",
        "value": "someemail@company.tld"
      }
    ]
  }
]
```

_Note:_ `email_mac` is the HMAC-SHA256 of `user_email` as input using a secret key (which is hard-coded into one of the frameworks in app bundle)


```shell
#!/bin/zsh

# 
# «s3kr37»  it is also hard-coded into the same binaries and can
#           'grepped' with a little effort. Without it curl query
#           below always returns an error.
# 
function get_hmac () {
	echo -n $1                                    \
	| openssl dgst -r                             \
                   -sha256                        \
                   -hmac "${HMAC_KEY:-«s3kr37»}"  \
	| cut -d ' ' -f1
}

# 
# x-api-key was noticed during initial discovery using ssl/tlx proxy;
#           it is also hard-coded into one of the binaries and can
#           'grepped' with a little effort. Without it "forbidden"
#           will always be returned.
# 
curl            \
    --silent    \
    --location  \
    --url       "https://api.topaz-labs.net/v2/app_state/unauthed"      \
    --header    "x-api-key: ${x_api_key}"                               \
    --url-query "app_build_type=RELEASE"                                \
    --url-query "app_cname=${app_cname:-GIGAPIXEL}"                     \
    --url-query "app_version=${app_ver:-7.0.0}"                         \
    --url-query "arch=$(uname -m)"                                      \
    --url-query "cpu_supports_avx=true"                                 \
    --url-query "email_mac=$(get_hmac "$user_email")"                   \
    --url-query "license_expiration_datetime=$(date -v "+1y" +"%FT%T")" \
    --url-query "os_type=osx"                                           \
    --url-query "os_version=$(sw_vers -productVersion)"                 \
    --url-query "user_email=${user_email:-foo@bar.nul}"                 \
| jq .
```

```json
  {
    "status": "OK",
    "app_update": {
      "app_update_status": "UPDATE_AVAILABLE",
      "app_update_versions": [
        {
          "app_version": "7.4.3",
          "baseline_version": "",
          "release_datetime": "2024-09-17T22:19:13",
          "release_highlights": "<ul>\n<li>EULA has been updated</li>\n<li>Flip order of Fit/Fill in Gigaprint, make Fill default</li>\n<li>Co  mparison selection editing now disabled when using Recovery Speed</li>\n<li>Allow image selection in Recovery mode</li>\n<li>Add model name   to print assistant</li>\n<li>Disable face recovery toggle when no faces detected</li>\n<li>Update scale rather than dimensions when resoluti  on changes</li>\n<li>Allow selecting PPCM as resolution unit when dimensions unit is pixels</li>\n<li>Always make scrollbars visible</li>\n<  li>Improve accuracy of processing state in model indicator</li>\n<li>Minor UI changes</li>\n<li>View behind processed Recovery previews when   original requested</li>\n<li>Fix showing \"Viewing original\" while processing Recovery preview</li>\n<li>Fix file view changing size after   switching from recovery model</li>\n<li>Fix monochrome images having color introduced after processing</li>\n<li>Fix max upscale warning au  to-closing on being shown</li>\n<li>Fix spacebar not viewing original image after changing orientation in Gigaprint</li>\n<li>Fix large scal  e values erroneously appearing as invalid</li>\n<li>Fix preview not updating when using Face Recovery v2 with no faces selected</li>\n<li>Fi  x tiny scrollbar appearing on file list</li>\n<li>Fix processing stalling occasionally after exiting Gigaprint</li>\n</ul>",
          "release_notes_url": "https://community.topazlabs.com/t/gigapixel-v7-4-3/78196",
          "required_models": [],
          "is_owned": true,
          "is_compatible": true,
          "incompatibility_message": "",
          "inapp_installer_type": "INSTALLBUILDER_INAPP_ONLINE",
          "inapp_installer_url": "https://downloads.topazlabs.com/deploy/TopazGigapixelAI/7.4.3/TopazGigapixelAI-7.4.3.pkg",
          "inapp_installer_sha256": "b89008f15d602a281304ef8f4916ab76554baa65d1db461f6c96f14353d80f28",
          "inapp_installer_file_size_bytes": 323990671,
          "installbuilder_full_url": "https://downloads.topazlabs.com/deploy/TopazGigapixelAI/7.4.3/TopazGigapixelAI-7.4.3.pkg",
          "installbuilder_full_sha256": "b89008f15d602a281304ef8f4916ab76554baa65d1db461f6c96f14353d80f28"
        },
        {
            …snip…
```

- - - 

[yq](https://mikefarah.gitbook.io/yq) _(like jq but for yaml)_

```shell
#appnames=( "Gigapixel" "Photo" "Video" )
appnames=( "Gigapixel" "Photo" )
for APPNAME in $appnames
do
  export APPNAME
  target="Topaz/Topaz${APPNAME}AI.munki.recipe.yaml"
  # add '--inplace' arg to yq to change input yaml file
  if [[ -s "$target" ]]; then
    yq '
        .Input.pkginfo.postinstall_script |=
          (
            load_str("Topaz/NOTES.d/template--munki-preuninstall_script.zsh")
            | sub("{{APPNAME}}", env(APPNAME))
          )
        |
        .Input.pkginfo.preuninstall_script |=
          (
            load_str("Topaz/NOTES.d/template--munki-preuninstall_script.zsh")
            | sub("{{APPNAME}}", env(APPNAME))
          )
        |
        .Input.pkginfo.postuninstall_script |=
          (
            load_str("Topaz/NOTES.d/template--munki-postuninstall_script.zsh")
            | sub("{{APPNAME}}", env(APPNAME))
          )
      ' \
      "${target}"
  fi
  unset APPNAME
done
```

- - - 

_Comments/notes removed from TopazGigapixelAI.munki.recipe.yaml_
```
#
# TODOs:
#
#   Note: Munki warning log "Removing non-empty bundle" (*.tz models)
#
#   postinstall_script:
#   ╷
#   │ ╭─● Create Symlink Plugins
#   ├─┤
#   │ │ (sources)
#   │ ├─┬🡢 /Applications/Topaz Gigapixel AI.app/Contents/Resources/
#   │ │ │
#   │ │ ├──🡢 ./TopazGigapixelAI.plugin
#   │ │ ├──🡢 ./TopazGigapixelAIApply.plugin
#   │ │ ├──🡢 ./TopazGigapixelAIAuthomate.plugin
#   │ │ ╰──🡢 ./TopazGigapixelAIGather.plugin
#   │ │
#   │ │ (destinations)
#   │ ╰─┬🡢 /Applications/Adobe Photoshop 2024/Plug-ins/
#   │   ╰🡢 /Library/Application Support/Adobe/Plug-ins/CC/
#   │
#   │   [note: src plugins in ./Content/Resources/]
#   │
#   ├─● Adobe Lightroom template(s)
#   │
#   ├─● Capture One plugin: TopazGigapixelAI.coplugin
#   │
#   ╰─● ... ?
#
#
#   ???  OTHER PACKAGES                       ???
#   ???  https://github.com/macadmins/outset  ???
#
#   _Note: There **is** no TopazGigapixelAI.plugin, so WTF Topaz?_
#
#   handle TopazGigapixelAI.plugin for Affinity Photo, Affinity Photo 2
#      "${HOME}/Library/Application Support/Affinity Photo/Plugins"
#      "${HOME}/Library/Application Support/Affinity Photo 2/Plugins"
#
#   handle Lightroom template files
#   Lightroom Templates
#   /Applications/Topaz Gigapixel AI.app/Contents/Resources
#        ./lrtemplates/
#              ./export.lrtemplate
#              ./external editor.lrtemplate
#   $HOME/Library/Application Support/Adobe/Lightroom/
#   [WARNING] *.rtemplate _may_ have {{PLACEHOLDER}} req. `sed` edit
#   ├🡢 ./Export Presets/${EXPORT_PRESET}.lrtemplate
#   ├🡢 ./External Editor Presets/${EXTERNAL_EDITOR_PRESET}.lrtemplate
#   Note: change filename to something more meaningful?
#
#   handle TopazGigapixelAI.plugin for ON1 Photo RAW
#      "${HOME}/Library/Application Support/ON1/..."
#
#   handle *.coplugin for Capture One
#      "${HOME}/Library/Application Support/Capture One/..."
#
#
```

_Comments/notes removed from TopazPhotoAI.munki.recipe.yaml_
```
#
# TODOs:
#
#   preuninstall_script:
#   ├─● Delete (symlinks to) plugins
#   ├─● Note: Munki warning log "Removing non-empty bundle" (*.tz models)
#   ├─● Remove CC plugins (may be symlinks)
#   ├─● Remove /etc/paths.d/50/com.topazlabs.photo
#   ╰─● ... ?
#
#   postinstall_script:
#    ├─● Adobe CC plugins:
#    │ ├🡢 TopazPhotoAI.plugin
#    │ ├🡢 TopazPhotoAIApply.plugin
#    │ ├🡢 TopazPhotoAIAuthomate.plugin
#    │ ╰🡢 TopazPhotoAIGather.plugin
#    ├─● Adobe Lightroom plugin: photo.lrdevplugin
#    ├─● Adobe Lightroom template(s)
#    ╰─● Capture One plugin: TopazPhotoAI.coplugin
#
```

_Comments/notes removed from TopazVideoAI.munki.recipe.yaml_
```
#   ╷
#   │ ╭─● embedded plugin installer scripts
#   ├─┤
#   │ ├─┬🡢 /Applications/Topaz Video AI.app/Contents/Resources/
#   │ │ │
#   │ │ ├──🡢 ./ae_inst.sh
#   │ │ ╰──🡢 ./ofx_inst.sh
#   │ ╰─●
#   ╰───●
#
# TODO: preuninstall_script:
#       ╰─● if unnecessary then uncomment 'unattended_uninstall: true'
#
# unattended_uninstall: true
#
```