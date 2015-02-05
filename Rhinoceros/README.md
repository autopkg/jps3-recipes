Rhinoceros.munki
================

**Be certain to supply a valid email address to the `REGISTRANT_EMAIL_ADDRESS` variable or you will see errors from AutoPkg.**

**2015-02-05**
I have done one test with the licensing, which as a result, it seems feasible to create a Munki update package for the main Rhinoceros pkg. On a virgin test Mac (Rhinoceros would not run in a VMware Fusion instance for me, even with the "Accelerated 3D Graphics" option enabled), I downloaded and installed Rhinoceros.app, copied it to /Applications and launched it. At some point shortly thereafter I was prompted to register the software. Before that process completed, I was prompted for admin credentials. I found that two files were created:

```
/Applications/Rhinoceros.app/Contents/Frameworks/Mono64Rhino.framework/Versions/3.6.0/Resources/etc/mono/registry/last-btime
```
and
```
/Library/Application Support/McNeel/Rhinoceros/License Manager/Licenses/hhhhhhhh-nnnn-nnnn-hhhh-hhhhhhhhhhhh.lic
```

The first file is ASCII text and, for me at least, only contains the the string `-1`

The second file (`\*.lic`), which here I have replaced the hex and number with 'h' and 'n' pattern, I assume to be an encrypted file.

As a test, I placed both into a pkg and added to Munki as an update to the `Rhinoceros` pkginfo file. It worked fine on one test client in one of my labs, and Rhinoceros.app launched without any prompting for any admin credentials or licensing or registration information. This would *seem* to indicate that we can simply push out a second package with these two licensing files.

*Note: The download site, and the automated, follow-up emails you will receive, do mention that the application is nearly production ready and that the license will function for some period until they begin shipping the finished production version.*


**2015-02-04**
(Update): There may not be a way to "automagically" perform the registration before or after installation. It appears to be a fairly complex process requiring manual, GUI intervention to complete the licensing. At least for a first run. You could use fswatch or Composer (or similar) to identify the changed files after running on a test box, and create a separate package of those. (Note: I have not tested that yet). Downloading and import into Munki appears straightforward.


**2015-02-03**
The download recipe required a fairly major refactoring due to changes made to how the downloads from the publisher's web site were being done.

They now require the user to enter their email address before a license key and download URL are presented. This breaks the much easier and simpler 'URLDownloader' Processor, and required the creation of a custom one, named 'RhinocerosUrlProvider'.

What to do with the license key (as far as any automation within a recipe is concerned) has not yet been determined.


**(prior)**
The original com.github.hansen-m.download.Rhinoceros recipe can still be found at:
https://github.com/autopkg/hansen-m-recipes/tree/master/Rhinoceros


