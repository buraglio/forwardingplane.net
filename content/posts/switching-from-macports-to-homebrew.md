---
title: 'Switching from MacPorts to Homebrew'
date: Sat, 06 Aug 2011 17:22:00 +0000
draft: false
tags: [How-To, UNIX]
---

I've recently decided that even though I love the BSD style [MacPorts](http://www.macports.org) system, it can be too clunky to maintain and doesn't handle dependancies as well as I'd like (much like the actual BSD ports collection). So, in doing a little looking I found that [Fink](http://www.finkproject.org/) is still out of date, but [Homebrew](http://mxcl.github.com/homebrew/) is very simple and also really elegant comparatively speaking.

Since homebrew doesn't wrk well with other packge systems installed, and I already

I'd like to know what I had installed since this system has been in use for 2+ years, so I do a list and send it to a txt file:

_touch ~/Documents/installed.macports.txt_

_sudo port list installed > Documents/installed.macports.txt_

_sudo cat .macports/history >> ~/Documents/installed.macports.txt_

Then I remove the installed packages:

_sudo port -f uninstall installed_

Per the instructions found on the [MacPorts page](http://guide.macports.org/chunked/installing.macports.uninstalling.html), remove all of the directories as such:

_sudo rm -rf \\_

_/opt/local \\_

_/Applications/DarwinPorts \\_

_/Applications/MacPorts \\_

_/Library/LaunchDaemons/org.macports.\* \\_

_/Library/Receipts/DarwinPorts\*.pkg \\_

_/Library/Receipts/MacPorts\*.pkg \\_

_/Library/StartupItems/DarwinPortsStartup \\_

_/Library/Tcl/darwinports1.0 \\_

_/Library/Tcl/macports1.0 \\_

_~/.macports_

If this is an upgraded machine (say, from 10.6 to 10.7), you'll need to also reinstall the Xcode Developer Tools via the app store before installing homebrew.

After waiting forever to get XCode downloaded, and since it's been installed via the App Store under Lion (10.7), I need to run the “Install Xcode” app that is placed in /Applications.

Now I can [Install homebrew](https://github.com/mxcl/homebrew/wiki/Installation) via the handy cli command:

_sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"_

You'll then see something like this:

_\==> This script will install:_

_/usr/local/bin/brew_

_/usr/local/Library/Formula/..._

_/usr/local/Library/Homebrew/..._

_\==> The following directories will be made group writable:_

_/usr/local/share/man_

_/usr/local/lib/pkgconfig_

_/usr/local/share/man/man8_

_/usr/local/share/doc_

_/usr/local/bin_

_/usr/local/include_

_/usr/local/lib_

_/usr/local/share_

_\==> The following directories will have their group set to staff:_

_/usr/local/share/man_

_/usr/local/lib/pkgconfig_

_/usr/local/share/man/man8_

_/usr/local/share/doc_

_/usr/local/bin_

_/usr/local/include_

_/usr/local/lib_

_/usr/local/share_

_Press enter to continue_

If you want to continue, hit enter.  In my case, I saw this:

\==> /usr/bin/sudo /bin/chmod o+w /usr/local

\==> /usr/bin/sudo /bin/chmod g+w /usr/local/share/man /usr/local/lib/pkgconfig /usr/local/share/man/man8 /usr/local/share/doc /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share

\==> /usr/bin/sudo /usr/bin/chgrp staff /usr/local/share/man /usr/local/lib/pkgconfig /usr/local/share/man/man8 /usr/local/share/doc /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share

\==> Downloading and Installing Homebrew...

\==> /usr/bin/sudo /bin/chmod o-w /usr/local

Warning: Now install Xcode: http://developer.apple.com/technologies/xcode.html

Warning: The following \*evil\* dylibs exist in /usr/local/lib

They may break builds or worse. You should consider deleting them:

/usr/local/lib/libfuse.2.dylib

/usr/local/lib/libfuse\_ino64.2.dylib

\==> Installation successful!

Now type: brew help

I chose to leave those libraries and deal with the fallout as I saw it.

Now I need to install the base repository manager that brew uses:

_sudo brew install git_

Then I can update the brew repository:

_sudo brew update_

That's basically it. Now I can install apps via HomeBrew using the simple command:

_sudo brew install_

I chose to install nmap as a test:

_sudo brew install nmap_

You're done. Enjoy your HomeBrew =)

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]