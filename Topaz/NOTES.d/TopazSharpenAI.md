# Topaz Sharpen AI
## Additional Notes

- **dmg**
  - `Topaz Sharpen AI.app` _--copy to-->_ `/Applications/`
  - Requires permissions fix (to mode 0777) for `./Contents/Resources/local/tgrc/`

```
Topaz Sharpen AI.app/Contents/Resources/
├── PS_Plugins/
│   └── TopazSharpenAI.plugin/
├── TopazSharpenAI.lrtemplate
├── …
├── linkplugins.applescript
├── local/
│   ├── …
│   └── tgrc/
│       ├── Sharpen_LensBlur.bin
│       ├── Sharpen_LensBlur_Noisy.bin
│       ├── …
│       ├── sms-v2-fp16-ml.tz
│       └── sms-v2-fp16-ov.tz
└── …
```