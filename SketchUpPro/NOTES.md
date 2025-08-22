# SketchUp

## What’s What?

1. Name change from “SketchUp Pro” to “SketchUp”
1. [Managing Network Lab License](https://help.sketchup.com/en/admin/managing-network-license)
1. [«Win» Offline Silent Installation of Network Lab License](https://help.sketchup.com/en/sketchup/performing-silent-install-sketchup)
1. Create new, updated license activation pkg
	- pre-populate `activation_info.txt` (actually json) and place in `/Library/Application Support/SketchUp ${MAJOR_VERSION:-2025}`
	- **must** include new, additional folder `/Library/Application Support/Reprise` (mode:`0777` required)
1. Take screenshots


## Considerations

1. Link to release notes?


## TODOs

- … _keep_ old and update …
	- [ ] Remove `CodeSignatureVerifier` processor step for `Style Builder.app` which is dropped in 2025, but _presumably_ for earlier versions if the main two apps verify can we assume Style Builder would have? _There is no way to indicate an if-then-else or optional processor step it seems._
- … **or** scrap old …
	- [ ] Add `DeprecationWarning` to `SketchUpPro.download.recipe`
	- [ ] Add `DeprecationWarning` to `SketchUpPro.munki.recipe`
	- [ ] Create new `SketchUpPro2025.download.recipe`
	- [ ] Create new `SketchUpPro2025.munki.recipe`


## Misc Notes

- old verifications (same for the three `*.app` bundles:
	- `anchor apple generic and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL)`
- verifications for 2023-2025 regardless of app:
	- `$designated anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
- Had used extant recipes (DMS) for SketchUpPro 2023 and SketchUp 2024 (kept the Munki pkgname `SketchUpPro` for conenience)


```xml
	<key>Description</key>
	<string>Downloads the latest version of SketchUp Pro by looking for the first match on the download page, then imports into your Munki repo. 
		
Note 1: At the time of this commit, the only valid values for RELEASE_YEAR are 2023, 2024, and 2025 (default).

Note 2: “2023” is named “SketchUp Pro” and contains 3-qty apps (SketchUp, Layout, Style Builder). “2024” is named “SketchUp” and contains 3-qty apps (SketchUp, Layout, and Style Builder). “2025” is named “SketchUp” and contains 2-qty apps (SketchUp and Layout)


</string>
<!-- …snip… -->
<key>description</key>
<string>Effortlessly turn creative ideas into buildable 3D models with intuitive, professional-grade design software trusted by architects, builders, and designers worldwide. Additional information can be found at https://sketchup.trimble.com/en
</string>
<key>display_name</key>
<string>SketchUp</string>
```

https://download.sketchup.com/SketchUp-2025-0-659-288.dmg
https://download.sketchup.com/SketchUp-2024-0-598-243.dmg
https://download.sketchup.com/SketchUpPro-2023-1-341-117.dmg


- - - 

## SketchUp 2025

	/Volumes/SketchUp 2025/SketchUp 2025/:
	total 104
	-rw-r--r--@ 1 testuser  staff     0B May 29 09:28 Icon?
	drwxrwxrwx  3 testuser  staff   102B May 27 18:02 LayOut.app
	drwxrwxrwx  3 testuser  staff   102B May 27 18:02 SketchUp.app

- **two** apps
- minimum supported version of macOS 11.7
- there is only _one_ file with correct permissions, all others are **world writable**
- `(?P&lt;url&gt;(?:https?:\/\/)?(?:download\.)?sketchup\.com\/.*(?:\/)?(?P&lt;filename&gt;SketchUp-(?:2025)-[^\.]+\.dmg))`
- Bundle Identifiers:
	- `com.sketchup.LayOut.2025`
	- `com.sketchup.SketchUp.2025`
- Code signatures:	
	- `designated => identifier "com.sketchup.LayOut.2025" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
	- `designated => identifier "com.sketchup.SketchUp.2025" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
- [Release Notes](https://help.sketchup.com/en/release-notes/sketchup-desktop-20250)


## SkethUp 2024

	/Volumes/SketchUp 2024/SketchUp 2024/:
	total 104
	-rw-r--r--@ 1 testuser  staff     0B Sep 24  2024 Icon?
	drwxrwxrwx  3 testuser  staff   102B Sep 24  2024 LayOut.app
	drwxrwxrwx  3 testuser  staff   102B Sep 24  2024 SketchUp.app
	drwxrwxrwx  3 testuser  staff   102B Sep 24  2024 Style Builder.app

- **three** apps
- minimum supported version of macOS 11.7
- there is only _one_ file with correct permissions, all others are **world writable**
- Bundle Identifiers:
	- `com.sketchup.LayOut.2024`
	- `com.sketchup.SketchUp.2024`
	- `com.sketchup.StyleBuilder.2024`
- Code signatures:
	- `designated => identifier "com.sketchup.LayOut.2024" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
	- `designated => identifier "com.sketchup.SketchUp.2024" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
	- `designated => identifier "com.sketchup.StyleBuilder.2024" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
- [Release Notes](https://help.sketchup.com/en/release-notes/sketchup-desktop-20240)


## SketchUpPro 2023

	/Volumes/SketchUp 2023/SketchUp 2023/:
	total 104
	-rw-r--r--@ 1 testuser  staff     0B Sep 29  2023 Icon?
	drwxrwxrwx  3 testuser  staff   102B Sep 29  2023 LayOut.app
	drwxrwxrwx  3 testuser  staff   102B Sep 29  2023 SketchUp.app
	drwxrwxrwx  3 testuser  staff   102B Sep 29  2023 Style Builder.app

- **three** apps
- minimum supported version of macOS 10.15
- there is only _one_ file with correct permissions, all others are **world writable**
- Bundle Identifiers:
	- `com.sketchup.LayOut.2023`
	- `com.sketchup.SketchUp.2023`
	- `com.sketchup.StyleBuilder.2023`
- Code Signatures:
	- `designated => identifier "com.sketchup.LayOut.2023" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
	- `designated => identifier "com.sketchup.SketchUp.2023" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
	- `designated => identifier "com.sketchup.StyleBuilder.2023" and anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = J8PVMCY7KL`
- [Release Notes](https://help.sketchup.com/en/release-notes/sketchup-desktop-20231)

- - - 
