Rhinoceros.munki
================

**Be certain to supply a valid email address to the `REGISTRANT_EMAIL_ADDRESS` variable or you will see errors from AutoPkg.**

**2015-02-04**
(Update): There may not be a way to "automagically" perform the registration before or after installation. It appears to be a fairly complex process requiring manual, GUI intervention to complete the licensing. At least for a first run. You could use fswatch or Composer (or similar) to identify the changed files after running on a test box, and create a separate package of those. (Note: I have not tested that yet). Downloading and import into Munki appears straightforward.

**2015-02-03**
The download recipe required a fairly major refactoring due to changes made to how the downloads from the publisher's web site were being done.

They now require the user to enter their email address before a license key and download URL are presented. This breaks the much easier and simpler 'URLDownloader' Processor, and required the creation of a custom one, named 'RhinocerosUrlProvider'.

What to do with the license key (as far as any automation within a recipe is concerned) has not yet been determined.


**(prior)**
The original com.github.hansen-m.download.Rhinoceros recipe can still be found at:
https://github.com/autopkg/hansen-m-recipes/tree/master/Rhinoceros


