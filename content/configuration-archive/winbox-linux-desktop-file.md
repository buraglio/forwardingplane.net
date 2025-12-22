---
title: Mikrotik Winbox linux .desktop file
date: 2024-12-21
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - linux
    - mikrotik
---


A minor annoyance, but the linux version of [Mikrotik winbox](https://mikrotik.com/download), while possibly the best network interface GUI around, has some quirks. If you want the icons to look correct, do the following (via Jerald Worthington)

This file assumes that the .zip from MikroTik is extracted to /opt/WinBox

If putting in another location, edit the Exec= and Icon= to match the correct locations

1. Place the WinBox.desktop file in /usr/share/applications
2. Create a symlink in /usr/local/bin to point to /opt/WinBox/WinBox (or wherever you extract the file to)

Then whenever you launch from the Application launcher it'll show the proper icon in the dock.