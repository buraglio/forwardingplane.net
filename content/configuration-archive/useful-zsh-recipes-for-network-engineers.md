---
title: Useful .zshrc formulas for network engineers
date: 2025-02-27
author: Nick Buraglio
layout: page
categories:
    - configuration
tags:
    - linux
    - zsh
---

Useful .zshrc formulas for network engineers


`mac` will take a MAC address input and provide multiple formats for use on differing systems

```
mac() {
    if [[ -z "$1" ]]; then
        echo "Usage: format_mac <MAC>"
        return 1
    fi

    # Remove all non-hex characters
    mac=$(echo "$1" | tr -d ':-.')

    if [[ ${#mac} -ne 12 ]]; then
        echo "Invalid MAC address format."
        return 1
    fi

    # Standard colon-separated format (AA:BB:CC:DD:EE:FF)
    mac_colon=$(echo "$mac" | sed 's/\(..\)/\1:/g; s/:$//')

    # Cisco format (AAAA.BBBB.CCCC)
    mac_cisco=$(echo "$mac" | sed 's/\(..\)\(..\)/\1\2./g; s/\.$//')

    # Microsoft dash-separated format (AA-BB-CC-DD-EE-FF)
    mac_dash=$(echo "$mac" | sed 's/\(..\)/\1-/g; s/-$//')

    # CatOS format (AAAAAA-BBBBBB)
    mac_catos=$(echo "$mac" | sed 's/\(......\)/\1-/; s/-$//')

    echo "Standard  : $mac_colon"
    echo "Cisco IOS : $mac_cisco"
    echo "Microsoft : $mac_dash"
    echo "CatOS     : $mac_catos"
}
```

Print all network info on given interfaces

```
#netinfo - shows network information for your system
allnets ()
{
echo "--------------- Network Information ---------------"
/sbin/ifconfig | awk /'inet addr/ {print $2}'
/sbin/ifconfig | awk /'Bcast/ {print $3}'
/sbin/ifconfig | awk /'inet addr/ {print $4}'
/sbin/ifconfig | awk /'HWaddr/ {print $4,$5}'
/sbin/ifconfig | awk /inet6\ /'{print $2}'
echo "---------------Global Addressing--------------------"
#myip=`lynx -dump -hiddenlinks=ignore -nolist http://checkip.dyndns.org:8245/ | sed '/^$/d; s/^[ ]*//g; s/[ ]*$//g' `
myip=`curl -s https://ip4only.me/api/ | cut -f2 -d,`
myip6=`curl -s https://ip6only.me/api/ | cut -f2 -d,`
echo "My global IPv4 address is ${myip}"
echo "My global IPv6 address is ${myip6}"
echo "---------------------------------------------------"
}

netinfo ()
{
echo "---------------Global Addressing--------------------"
myip=`curl -s https://ip4only.me/api/ | cut -f2 -d,`
myip6=`curl -s https://ip6only.me/api/ | cut -f2 -d,`
echo "My global IPv4 address is ${myip}"
echo "My global IPv6 address is ${myip6}"
echo "---------------------------------------------------"
}
```

`netinfo` prints the preferred interfaces IPv4 and IPv6 addresses based on a query to a public API. Requires internet access. This 
will display the external IPv4 NAT address, which may be useful for troubleshooting access rules on far end systems or intermediary ACLs.  

`allnets` will print all network addres information on all interfaces, including IPv6 link local addresses.

Also available as a gist [here](https://gist.github.com/buraglio/b2a16315c0601ea5d2dd2e4e93e46cf6)
