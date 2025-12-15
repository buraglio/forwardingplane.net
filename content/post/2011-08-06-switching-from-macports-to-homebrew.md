---
id: 31
title: 'Switching from MacPorts to Homebrew'
date: '2011-08-06T17:22:00-05:00'
author: buraglio
layout: post
guid: 'http://new.forwardingplane.net/2011/08/switching-from-macports-to-homebrew/'
permalink: /2011/08/06/switching-from-macports-to-homebrew/
themeblvd_noindex:
    - 'true'
Views:
    - '122'
categories:
    - How-To
    - UNIX
---

I've recently decided that even though I love the BSD style [MacPorts](http://www.macports.org) system, it can be too clunky to maintain and doesn't handle dependancies as well as I'd like (much like the actual BSD ports collection). So, in doing a little looking I found that [Fink](http://www.finkproject.org/) is still out of date, but [Homebrew](http://mxcl.github.com/homebrew/) is very simple and also really elegant comparatively speaking.

Since homebrew doesn't wrk well with other packge systems installed, and I already

I'd like to know what I had installed since this system has been in use for 2+ years, so I do a list and send it to a txt file:

*touch ~/Documents/installed.macports.txt*
*sudo port list installed > Documents/installed.macports.txt*

*sudo cat .macports/history >> ~/Documents/installed.macports.txt*


Then I remove the installed packages:

*sudo port -f uninstall installed*

Per the instructions found on the [MacPorts page](http://guide.macports.org/chunked/installing.macports.uninstalling.html), remove all of the directories as such:


*sudo rm -rf \*
* /opt/local \*
* /Applications/DarwinPorts \*
* /Applications/MacPorts \*
* /Library/LaunchDaemons/org.macports.* \*
* /Library/Receipts/DarwinPorts*.pkg \*
* /Library/Receipts/MacPorts*.pkg \*
* /Library/StartupItems/DarwinPortsStartup \*
* /Library/Tcl/darwinports1.0 \*
* /Library/Tcl/macports1.0 \*
* ~/.macports*


If this is an upgraded machine (say, from 10.6 to 10.7), you'll need to also reinstall the Xcode Developer Tools via the app store before installing homebrew.

After waiting forever to get XCode downloaded, and since it's been installed via the App Store under Lion (10.7), I need to run the “Install Xcode” app that is placed in /Applications.

Now I can [Install homebrew](https://github.com/mxcl/homebrew/wiki/Installation) via the handy cli command:

*sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"*
*
*
You'll then see something like this:


*==> This script will install:*
*/usr/local/bin/brew*
*/usr/local/Library/Formula/...*
*/usr/local/Library/Homebrew/...*
*==> The following directories will be made group writable:*
*/usr/local/share/man*
*/usr/local/lib/pkgconfig*
*/usr/local/share/man/man8*
*/usr/local/share/doc*
*/usr/local/bin*
*/usr/local/include*
*/usr/local/lib*
*/usr/local/share*
*==> The following directories will have their group set to staff:*
*/usr/local/share/man*
*/usr/local/lib/pkgconfig*
*/usr/local/share/man/man8*
*/usr/local/share/doc*
*/usr/local/bin*
*/usr/local/include*
*/usr/local/lib*
*/usr/local/share*
*
*
*Press enter to continue*

*
*
If you want to continue, hit enter.* * In my case, I saw this:
*
*

==> /usr/bin/sudo /bin/chmod o+w /usr/local
==> /usr/bin/sudo /bin/chmod g+w /usr/local/share/man /usr/local/lib/pkgconfig /usr/local/share/man/man8 /usr/local/share/doc /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share
==> /usr/bin/sudo /usr/bin/chgrp staff /usr/local/share/man /usr/local/lib/pkgconfig /usr/local/share/man/man8 /usr/local/share/doc /usr/local/bin /usr/local/include /usr/local/lib /usr/local/share
==> Downloading and Installing Homebrew...
==> /usr/bin/sudo /bin/chmod o-w /usr/local
Warning: Now install Xcode: http://developer.apple.com/technologies/xcode.html
Warning: The following *evil* dylibs exist in /usr/local/lib
They may break builds or worse. You should consider deleting them:
/usr/local/lib/libfuse.2.dylib
/usr/local/lib/libfuse_ino64.2.dylib
==> Installation successful!
Now type: brew help

I chose to leave those libraries and deal with the fallout as I saw it.


Now I need to install the base repository manager that brew uses:

*sudo brew install git*

Then I can update the brew repository:

*sudo brew update*
*
*
That's basically it. Now I can install apps via HomeBrew using the simple command:

*sudo brew install *

I chose to install nmap as a test:

*sudo brew install nmap*
*
*
You're done. Enjoy your HomeBrew =)


