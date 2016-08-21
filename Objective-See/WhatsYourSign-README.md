# Notes on WhatsYourSign.app and WhatsYourSignExt.appex

## Example scenario for scripting an installation

_Note: I am unfamiliar with Apple's API for App Extensions, but it appears that there is no means to "universally" activate a FinderSync app extension (plugin) for all users on a system. (This is probably a Good Thing™ from a security standpoint, I suppose). Possibly some sort of LaunchAgent to perform the activation might perform appropriately._


1. Copy `WhatsYourSign.app` to a managed, central location, such as `/Applications/Objective-See/` for example.
1. Copy `/path/to/WhatsYourSign.app/Contents/Resources/WhatsYourSign.appex` to a managed, central location, such as `/Library/Application Support/Objective-See/`
1. Use a LaunchAgent to enable the use of the `WhatsYourSign.appex` FinderSync app extension for each console (Aqua) user that logs in.

_Note: The `pluginkit -e use …` command adds or edits an entry to `/var/folders/XX/«30-char-random?-string»/0/com.apple.pluginkit/Annotations`. Therefore only by deleting the `Annotations` file is this database reset._

_Note: Other Objective-See products will install themselves into `/Applications` and involves a fair amount of extra careful scripting to move to something like `/Applications/Objective-See`. So perhaps it is "best" to just put into `/Applications` after all?_


# Miscellanea

- I used Hopper Disassembler v3 to figure out how the `WhatsYourSign.app` container app installed and use its Finder contextual menu item, and stumbled across the `/usr/bin/pluginkit` command. I was unaware of this entirely until I came across it.
- One can also use `/usr/bin/pluginkit` to list app extensions (which include Notification Center widgets, Dropbox's FinderSync status overlays, etc) and determine whether they are `use`d (`'+'`), `ignore`d (`'-'`) or `default` (`' '`) status. 
- `pluginkit -m` will list all known app extensions. (Adding `-A` and/or `-D` addd additional information.)
- Example: use or ignore (i.e. disable) the Notification Center stocks widget from the command line. `pluginkit -e use -i com.apple.ncplugin.stocks`. Deactivating, at least this example in particular seems a bit wonky, I suspect it has to do with how ever Notification Center refreshes itself (once an ncplugin activates, it seems to take awhile for it to go away unless explicity deleted interactively by user). However, to "disable" via cli: `pluginkit -e ignore -i com.apple.ncplugin.stocks` (or `-e default`).