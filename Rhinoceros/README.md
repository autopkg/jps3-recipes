Rhinoceros.munki
================

*2015-02-03*
The download recipe required a fairly major refactoring due to
changes made to how the downloads from the publisher's web site
were being done.

They now require the user to enter their email address before
a license key and download URL are presented. This breaks the
much easier and simpler 'URLDownloader' Processor, and required
the creation of a custom one, named 'RhinocerosUrlProvider'.

What to do with the license key (as far as any automation within
a recipe is concerned) has not yet been determined.


*(prior)*
The original com.github.hansen-m.download.Rhinoceros recipe can
still be found at:
https://github.com/autopkg/hansen-m-recipes/tree/master/Rhinoceros


