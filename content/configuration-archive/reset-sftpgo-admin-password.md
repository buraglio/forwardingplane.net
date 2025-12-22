---
title: Reset admin password for sftpgo docker container
date: 2025-12-22
author: Nick Buraglio
layout: page
categories:
    - configuration
    - docker
    - linux
tags:
    - linux
    - sftpgo
---

I have recently run into some odd behavior using the docker application sftpgo on my unraid NAS. I use this to do motion capture backup of my external security cameras, and it was a bit of a pain to figure out. Essentially, the admin account password seems to have reset itself, and I was in need of a way to set it back to what I had documented. In order to do so, open a connsole for the container and typew the command 
`sftpgo resetpwd --admin admin` Where `admin` is whatever you have set the adminstrative account to. 
This will allow for the reset to a new password and can be repeated from the console if necessary until I can figure out *why* this symptom occured.