---
title: Python IPv6 Subnet Planner
date: 2025-03-14
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

IPv6 address planning can be a trial-and-error endeavor. There are useful tools for subnetting, but I couldn;t find anything that would just take a prefix, subnet length, and provide a simple list of the prefixes. (Now, [this](https://github.com/vladak/ipv6gen) does exist, and I just simply missed it). I wrote some [really simple python](https://github.com/buraglio/ipv6-subnet-planner) that does a few things:

* Accepts an IPv6 prefix and a new prefix length to generate subnet allocations.

* Allows output to be saved to a file.

* Warns if the prefixes requested are not on a nibble boundary.

* Outputs to json if requested. Why? I have no idea but it was shockingly easy to do.

From the github repo: 

```
The IPv6 Subnet Planner is nothing more than a simple Python script designed to help network engineers, IT administrators, or zealous hobbyists to plan and allocate IPv6 subnets. It really just takes an IPv6 prefix as input and generates subnets of a user-specified prefix length. This can be useful for visualizing the subnets and for importing them into other things for more effective use.
```

[Git Repo](https://github.com/buraglio/ipv6-subnet-planner)
