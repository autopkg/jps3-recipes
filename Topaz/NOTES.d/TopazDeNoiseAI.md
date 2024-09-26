# Topaz DeNoise AI
## Additional Notes

- **dmg**
  - `Topaz DeNoise AI.app` _--copy to-->_ `/Applications/`
  - Requires permissions fix (to mode 0777) for `./Contents/Resources/local/tgrc/`

```
Topaz DeNoise AI.app/Contents/Resources/
├── PS_Plugins/
│   └── TopazDeNoiseAI.plugin/
├── TopazDeNoiseAI.lrtemplate
├── …
├── linkplugins.applescript
├── local/
│   ├── …
│   └── tgrc/
│       ├── Denoise.bin
│       ├── Denoise_Hifid.bin
│       ├── …
│       ├── nMsL.bin
│       └── nMsL_b.bin
└── …
```