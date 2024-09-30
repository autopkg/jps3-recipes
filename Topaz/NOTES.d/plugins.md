# Plugins
## Additional Notes

| plugins                                     | CFBundlePackageType  | CFBundleName               | CFBundleIdentifier                                 |
|:--------------------------------------------|:--------------------:|:---------------------------|:---------------------------------------------------|
| Topaz Video AI Frame Interpolation.plugin   |        `eFKT`        | -                          | `com.topazlabs.Topaz-Video-AI-Frame-Interpolation` |
| Topaz Video AIframeinterpolation.ofx.bundle |        `BNDL`        | -                          | `com.topazlabs.Topaz-Video-AI`                     |
| Topaz Video AI.ofx.bundle                   |        `BNDL`        | -                          | `com.topazlabs.Topaz-Video-AI`                     |
| Topaz Video AI.plugin                       |        `eFKT`        | -                          | `com.topazlabs.Topaz-Video-AI`                     |
| TopazDeNoiseAI.plugin                       |        `8BFM`        | TopazDeNoiseAI             | -                                                  |
| TopazPhotoAI.plugin                         |        `8BFM`        | Topaz Photo AI             | `com.topazlabs.TopazPhotoAI`                       |
| TopazPhotoAI.coplugin                       |        `BNDL`        | Topaz Photo AI Plugin      | `com.topazlabs.TopazPhotoAI`                       |
| TopazPhotoAIAutomate.plugin                 |        `8BFM`        | Topaz Photo AIAutomate     | `com.topazlabs.TopazPhotoAIAutomate`               |
| TopazPhotoAIApply.plugin                    |        `8BFM`        | Topaz Photo AIApply        | `com.topazlabs.TopazPhotoAIApply`                  |
| TopazPhotoAIGather.plugin                   |        `8BFM`        | Topaz Photo AIGather       | `com.topazlabs.TopazPhotoAIGather`                 |
| TopazGigapixelAI.coplugin                   |        `BNDL`        | Topaz Gigapixel AI Plugin  | `com.topazlabs.TopazGigapixelAI`                   |
| TopazGigapixelAIGather.plugin               |        `8BFM`        | Topaz Gigapixel AIGather   | `com.topazlabs.TopazGigapixelAIGather`             |
| TopazGigapixelAIAutomate.plugin             |        `8BFM`        | Topaz Gigapixel AIAutomate | `com.topazlabs.TopazGigapixelAIAutomate`           |
| TopazGigapixelAIApply.plugin                |        `8BFM`        | Topaz Gigapixel AIApply    | `com.topazlabs.TopazGigapixelAIApply`              |
| TopazSharpenAI.plugin                       |        `8BFM`        | TopazSharpenAI             | -                                                  |
                                                            

- `8BFM` + `*.plugin` is for Adobe Photoshop
  - example destinations:
    - `/Applications/Adobe Photoshop 2024/Plug-ins`
    - `/Library/Application Support/Adobe/Plug-ins/CC`
- `eFKT` + `*.plugin` is for Adobe After Effects
  - example destinations:
    - `/Applications/Adobe After Effects 2024/Plug-ins`
    - `/Library/Application Support/Adobe/Plug-ins/CC`
- `BNDL` + `*.coplugin` is a plugin for [Capture One](https://www.captureone.com/en)
- `BNDL` + `*.ofx.bundle` is an [OpenFX](https://en.wikipedia.org/wiki/OpenFX_(API)) plugin (typically DaVinci Resolve)

- table data scraped for:
  - Topaz Gigapixel AI 7.4.3
  - Topaz Photo AI 3.2.2
  - Topaz Video AI 5.3.2
  - Topaz DeNoise AI 3.7.2
  - Topaz Sharpen AI 4.1.0

- - - 

TODO: ### Adobe Lightroom & Lightroom Classic

- `*.lrdevplugin/*`


- - - 

**topaz-plugins.zsh**

```zsh
#!/bin/zsh

function get_plist_value () {
  plutil -extract "$1" raw "$2" | grep -ve "Could not extract value, error"
}

function get_plugins_info_plist_paths () {
  if [[ -d "$1" ]]; then
    IFS=$'\0' read -A plugins <<<$(
      find "$1"                                        \
        -name "Info.plist"                             \
        '('                                            \
            -path "*/Resources/*.plugin/Contents/*"    \
            -or                                        \
            -path "*/Resources/*.coplugin/Contents/*"  \
            -or \
            -path "*/Resources/*.ofx.bundle/Contents/*" \
        ')'                                            \
        -print0
      )
    print -r -- ${(qq)plugins}
  fi
}

plist_keys=(
  "CFBundlePackageType"
  "CFBundleName"
  "CFBundleIdentifier"
  #"CFBundleExecutable"
)

#print "app_name\tplugin\t${(j:\t:)plist_keys}"
print "plugin\t${(j:\t:)plist_keys}"

mdfind -0 -onlyin /Applications \
  '
    kMDItemKind=="Application"
    && kMDItemCFBundleIdentifier=="com.topazlabs.*"
  ' \
| while read -d '' -r TOPAZ_APP
  do
    app_plist="${TOPAZ_APP}/Contents/Info.plist"
    app_name="$(get_plist_value "CFBundleExecutable" "$app_plist")"
        # https://unix.stackexchange.com/a/535135
        plugins_paths=( "${(@Q)${(z)$(get_plugins_info_plist_paths "$TOPAZ_APP")}}" )
        for plugin in $plugins_paths
        do
          #printf '%s\t' "$app_name"
          printf '%s\t' "$(basename "${plugin%/Contents/Info.plist}")"
          for key in $plist_keys
          do
            value=$(get_plist_value "$key" "$plugin")
            printf '%s\t' "${value:--}"
          done
          printf '\n'
        done
  done

```
