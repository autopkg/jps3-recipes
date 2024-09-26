# Topaz Video AI
## Additional Notes

- **dmg**
    - `Topaz Video AI.app` _--copy to-->_ `/Applications/`

```
Topaz Video AI.app/Contents/Resources
├── Topaz Video AI Frame Interpolation.plugin/
├── Topaz Video AI.ofx.bundle/
├── Topaz Video AI.plugin/
├── Topaz Video AIframeinterpolation.ofx.bundle/
├── ae_inst.sh
├── …
├── models/
│   ├── aaa-10.json
│   ├── aaa-9.json
│   ├── …
│   ├── thm-2.json
│   └── video-encoders.json
├── ofx_inst.sh
├── …
├── presets/
│   ├── 4x slow motion.json
│   ├── 8x super slow motion.json
│   ├── …
│   ├── Upscale to 4K.json
│   └── Upscale to FHD.json
└── …
```

| Name                                        | CFBundleExecutable                   | CFBundleIdentifier                                 | CFBundlePackageType |
|---------------------------------------------|--------------------------------------|----------------------------------------------------|---------------------|
| Topaz Video AI Frame Interpolation.plugin   | Topaz Video AI                       | `com.topazlabs.Topaz-Video-AI`                     | `eFKT`              |
| Topaz Video AI.ofx.bundle                   | Topaz Video AI Frame Interpolation   | `com.topazlabs.Topaz-Video-AI-Frame-Interpolation` | `eFKT`              |
| Topaz Video AI.plugin                       | Topaz Video AI.ofx                   | `com.topazlabs.Topaz-Video-AI`                     | `BNDL`              |
| Topaz Video AIframeinterpolation.ofx.bundle | Topaz Video AIframeinterpolation.ofx | `com.topazlabs.Topaz-Video-AI`                     | `BNDL`              |


**ofx_inst.sh** (OpenFX)
```shell
#!/bin/bash

mkdir -p "/Library/OFX/Plugins"
cp -Rp "/Applications/Topaz Video AI.app/Contents/Resources/Topaz Video AI.ofx.bundle" "/Library/OFX/Plugins/"
cp -Rp "/Applications/Topaz Video AI.app/Contents/Resources/Topaz Video AIframeinterpolation.ofx.bundle" "/Library/OFX/Plugins/"
```

- [ ] TODO _Note: It may be safe and effective to call this script from a munki pkginfo `postinstall_script` but needs testing._

**ae_inst.sh** (Adobe After Effects)
```shell
#!/bin/bash

for d in "/Applications/Adobe After Effects 202"[0-4]; do
    if [ -d "${d}/Plug-ins/Topaz Video AI.plugin" ]; then
        rm -rf "${d}/Plug-ins/Topaz Video AI.plugin"
        echo "Removed old plugin from ${d}"
    fi
    cp -Rp "/Applications/Topaz Video AI.app/Contents/Resources/Topaz Video AI.plugin" "${d}/Plug-ins/"

    if [ -d "${d}/Plug-ins/Topaz Video AI Frame Interpolation.plugin" ]; then
        rm -rf "${d}/Plug-ins/Topaz Video AI Frame Interpolation.plugin"
        echo "Removed old frame interpolation plugin from ${d}"
    fi
    cp -Rp "/Applications/Topaz Video AI.app/Contents/Resources/Topaz Video AI Frame Interpolation.plugin" "${d}/Plug-ins/"

    echo "Installed After Effects plugins for ${d}"
done
```

- [ ] TODO _Note: It may be safe and effective to call this script from a munki pkginfo `postinstall_script` but needs testing._
