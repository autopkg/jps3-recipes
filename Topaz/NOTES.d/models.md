# Models
## Additional Notes

- The behavior of each individual app can be slightly different, and even between minor and patch versions, in whether or not it prompts to download models, or goes ahead and downloads in the background. (This _may_ have to do with a preference or other setting file being set between testing runs I did not delete.)
- The downloads appear to silently stall in the background at times.
- Total download sizes likely to exceed 5 GB per app, for the current apps (not deprecated).
- App bundles generally contain a specific, world-writable (i.e. mode `0777`) `./Contents/Resources/models` folder which ships with a number of JSON files. The structure and content of these files _appears_ to be the basis for how the app constructs the URL to download the `*.tz` model files.
- You can find a filename “pattern” like so in each:

```shell
cat face-clc.json | jq '.. | objects | with_entries(select(.key=="nets")) | select(.!={})'
```

```json
{
  "nets": [
    "[N]-v[V]-fp32-[H]x[W]-ov-11.tz"
  ]
}
{
  "nets": [
    "[N]-v[V]-fp32-[H]x[W]-mlc.tz"
  ]
}
```

- For each backend (ex. `coreml`) 
    - `[N]` appears to be a reference to the value `.shortName` (ex. `gfclc`)
    - `[V]` appears to be a reference to the value `.version` (ex. `1`)
    - `[H]` and `[W]` appear to reference the value of 
