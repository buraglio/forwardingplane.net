---
title: 'Enable Telnet access on MacOS High Sierra'
date: Sat, 02 Mar 2019 16:11:38 +0000
draft: false
---

Lots of things changed under the hood in MacOS high sierra. One of those was to enable a sandbox like environment and to remove insecure communication protocols. This breaks things like console communication to the network modeling and virtualization platform [Eve-NG](https://www.eve-ng.net/). It's fairly trivial to re-enable it, however. This can be accomplished by doing the following steps.

Install [Homebrew](http://www.homebrew.sh). Open your favorite terminal application (I like to use [iTerm2](https://www.iterm2.com/) (also installable via homebrew), but Terminal works fine.)

```
1\. Reboot your Mac and hold the CMD + R keys   
2\. When presented with the recovery options, click Utilities at the top and choose Terminal   
3\. Type; csrutil disable   
4\. Reboot as normal   
6\. terminal and type;   
brew install telnet   
sudo ln -s /usr/local/bin/telnet /usr/bin/telnet   
7\. Again, Reboot your Mac and hold the CMD + R keys   
8\. When presented with the recovery options, click Utilities at the top and choose Terminal   
9\. Type; csrutil enable   
10\. Reboot as normal 
```

You're done. You can have telnet for your internal communication to Eve-NG consoles. **Don't use it to talk to production network gear, because it's not 1998.**