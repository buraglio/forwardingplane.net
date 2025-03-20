---
title: Scripting URL normalization and resolution
date: 2025-02-28
author: Nick Buraglio
layout: post
categories:
    - python
    - linux
tags:
    - linux
    - nix4neteng
    - python
---

From time to time most network and / or security engineers will need to normalize the output of a set of URLs to either IP literals or a formatted list of DNS names. This can be particularly useful for feeding intelligence feeds or creating block/allow lists.

There are probably 10,000 other scripts to do this, but [this one](https://github.com/buraglio/urlresolver) is mine.

Potential use cases:

* Building custom pihole block / allow lists
* Building intelligence feeds
* Creating ACL lists
* Creating feeds for BGP filters
* Probably other stuff

Benefits / Features

* Works for both IPv4 and IPv6
* Simple implementation
* Easily extended to provide new output types

Via the github repo:

------
# Simple DNS Resolver Script for URLs
This script is marginally useful for creating files suitable for importing into tools that require one address or URL per line such as pihole

## Description
This Python script reads a list of URLs from an input file, extracts the domain names, and resolves their A (IPv4) and AAAA (IPv6) records. The results are printed to the console and saved to an output file.

## Prerequisites
- Python 3.x

## Installation
For simplicity, and because I am a terrible developer, no additional libraries are required as the script uses built-in Python capabilities / modules.

## Usage
Run the script with the following options:

```sh
python urlresolver.py [-f INPUT_FILE] [-o OUTPUT_FILE]
```

or 

```
chmod +x urlresolver.py
```

and then 

```
./urlresolver.py [-f INPUT_FILE] [-o OUTPUT_FILE]
```


### Options:
- `-f, --file`  : Specifies the input file containing URLs (default: `url.txt`).
- `-o, --output`: Specifies the output file to save resolved addresses (default: `resolved_addresses.txt`).
- `-n --normalize`: Specifies that the output should be a simple normalization of the URL - i.e. strip the http(s):// and trailing /$.
- `-r --resolve`: Specifies that the domain should be resolved and places as their literal IPv6 and/or legacy IPv4 addresses (default: -n).
- `-l --iptables`: Prints output in linux iptables format (requires -r)
- `-t --sros`: Prints output in Nokia SROS output (requires -r)
- `-j --junos`: Prints output as a JunOS prefix-list (requires -r)
- `-c --cisco`: Specifies the output as a Cisco IOS prefix-list (requires -r)
- `-x --iosxr`: Prints the output as an IOS-XR prefix-set (requires -r)
- `-z --filter-name`: Sets the name of the filter in -c, -x, -t, and -j
- `-h, --help`  : Displays the help message.

## Examples
```sh
python urlresolver.py -f someurls.txt -o someresults.txt
```
This will read domain names from `someurls.txt`, resolve their A and AAAA records, and save the results in `someresults.txt`.

```
urlresolver.py -r -j -f someurls.txt -o junos.txt -z someurls
```
This will read domain names from `someurls.txt`, resolve their A and AAAA records, and save the results in a junos prefix-list formatted list named `junos.txt` where the prefix-list name is `someurls`.


## Input File Format
The input file should contain one URL per line, e.g.,
```
https://example.com
http://sub.domain.com/
```

## Output File Format
The output file will contain resolved IP addresses, with the original URL commented above each entry, e.g.,
```
# https://example.com
192.0.2.1
3ffe:db8::1
# ----------------------------------------
```
Or, depending on the -n flag, it will return a list of commented, normalized URLs:
```
# https://7e14d.v.fwmrm.net
7e14d.v.fwmrm.net
# ----------------------------------------
# 
# ----------------------------------------
# https://a-fds.youborafds01.com
a-fds.youborafds01.com
# ----------------------------------------
# 
```


## Notes
- If a domain has no A or AAAA records, it will be noted in the console output but omitted from the output file.
- The script automatically removes protocol prefixes (e.g., `http://`, `https://`) and trailing slashes before resolving domains.
- If you'd rather run this as perl, simply `chmod +x urlresolver.pl` and run `./urlresolver.pl`. It should behave mostly the same with the same behavior, flags, and options.

## Caveats
The script can't handle stripping really, really long URLs, so anything egregiously long will need to be cleaned up manually.
