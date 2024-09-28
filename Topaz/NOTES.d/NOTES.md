# Notes

## Current App Downloads

Examples of where download URLs redirect to:

### Gigapixel

- `https://topazlabs.com/d/gigapixel/latest/mac/full`
  - `HTTP 301` → `https://downloads.topazlabs.com/deploy/TopazGigapixelAI/7.4.3/TopazGigapixelAI-7.4.3.pkg`
- **pkg**
  - 

### Photo

- `https://topazlabs.com/d/photo/latest/mac/full`
  - `HTTP 301` → `https://downloads.topazlabs.com/deploy/TopazPhotoAI/3.2.1/TopazPhotoAI-3.2.1.pkg`
- **pkg**

### Video

- `https://topazlabs.com/d/tvai/latest/mac/full`
  - `HTTP 301` → `https://downloads.topazlabs.com/deploy/TopazVideoAI/5.3.2/TopazVideoAI-5.3.2.dmg`
- **dmg**
- _See also: [TopazVideoAI.md](./TopazVideoAI.md)_


## Deprecated Apps
_Note: Only those Topaz apps which faculty have requested have recipes, there are others._

### DeNoise

- `https://downloads.topazlabs.com/deploy/TopazDeNoiseAI/latest/TopazDeNoiseAI-Full-Installer.dmg`
  - `last-modified: Wed, 22 Feb 2023 18:14:40 GMT`
- **dmg**
- _See also: [TopazDeNoiseAI.md](./TopazDeNoiseAI.md)_

### Sharpen

- `https://downloads.topazlabs.com/deploy/TopazSharpenAI/latest/TopazSharpenAI-Full-Installer.dmg`
  - `last-modified: Thu, 24 Mar 2022 19:37:10 GMT`
- **dmg**
- _See also: [TopazSharpenAI.md](./TopazSharpenAI.md)_

- - - 

## Plugins for Other Apps

_See also: [plugins.md](./plugins.md)



- - - 

## Templates

### Adobe Lightroom & Lightroom Classic

- `*.lrtemplate`
  - Files may contain placeholders (ex. `{{APPNAME}}`) which need to be `sed`’d out
  - Can _**only**_ work if placed in _**each user’s**_ library folder
    - This appears to only be performed by a post install script by apps using `pkg` installers, and _only_ for the current GUI session’s user.
    - `$HOME/Library/Application Support/Adobe/Lightroom/…`
    - Will require custom-authord Outset per-user scripts to perform checks
      - and must be tied to AutoPkg + Munki and take cleanup into account

- - - 

## Models

- _See also: [models.md](./models.md)_

- - - 

## APIs

- _See also: [APIs-Etc.md](./APIs-Etc.md)_
