IP addressing and subnetting is a common interview subject. I assert that memorizing these things is useful for learning the concepts but ultimately futile in that it is time consuming and inefficient use of engineering time when tools can be utilized to accomplish the same goals in less time with fewer errors. Honestly, I gave up doing this kind of work manually around 10 years ago and have never regretted it, and in actuality, I&#8217;d probably struggle to do it at this point because it&#8217;s a repetitive process better suited by code.  
In the old days, subnetting IPv4 manually was a badge of honor (and one that I always hated), but I learned it because I needed to know it for cert tests and daily work. However, once I started doing IPv6 around 2001, it became clear that doing this kind of thing by hand was consuming more time than it needed to.  
Enter UNIX tools.

HEX

Hex isn&#8217;t really a tool as much as it&#8217;s a hack for your shell.  Remember the [post on dotfiles](http://www.forwardingplane.net/2014/04/nix4neteng-1-managing-dotfiles-pwn-the-unspoken-pain-of-unix-administration/ "NIX4NetEng #1 Managing dotfiles; pwn the unspoken pain of UNIX administration")? This is something that can go right into your .bashrc and allows for the quick and easy translation of decimal to hexidecimal, which is very useful for IPv6 dual stacking because [in my opinion] the appropriate addressing scheme is to match the last octet based on hex and not numerically. So, to do that one needs to be able to easily convert the last octet quickly and easily.  Adding this to your .bashrc will accomplish this:

<pre>alias hex='printf "%x\n"'</pre>

Now, if you have an address of 10.143.27.199, you take the .199 you can utilize the shell alias to convert it to the hex equivalent.  For example:  
If you&#8217;re using static addresses or dhcpv6 with static addressing, you can match the last octet properly.

<pre>(~) desktop $ hex 199
c7</pre>

If you&#8217;re using static addresses or dhcpv6 with static addressing, you can match the last octet properly.

<pre>10.143.27.199/27
2001:DB8:1b::c7/120
</pre>

There are more than this, but these are the tools I use almost daily.

I generally use <a href="http://www.routemeister.net/projects/sipcalc/" target="_blank">sipcalc</a> at this point since it does what I used to use <a href="http://jodies.de/ipcalc" target="_blank">ipcalc</a> for and more.  For gathering and verifying information, this is a fantastic tool.

<pre>(~) desktop $ sipcalc 2001:DB8:1b::c7/120
-[ipv6 : 2001:DB8:1b::c7/120] - 0</pre>

<pre>[IPV6 INFO]
Expanded Address - 2001:0db8:001b:0000:0000:0000:0000:00c7
Compressed address - 2001:db8:1b::c7
Subnet prefix (masked) - 2001:db8:1b:0:0:0:0:0/120
Address ID (masked) - 0:0:0:0:0:0:0:c7/120
Prefix address - ffff:ffff:ffff:ffff:ffff:ffff:ffff:ff00
Prefix length - 120
Address type - Aggregatable Global Unicast Addresses
Network range - 2001:0db8:001b:0000:0000:0000:0000:0000 -
 2001:0db8:001b:0000:0000:0000:0000:00ff -</pre>

And for IPv4:

<pre>(~) desktop $ sipcalc 10.143.27.199/27
-[ipv4 : 10.143.27.199/27] - 0</pre>

<pre>[CIDR]
Host address - 10.143.27.199
Host address (decimal) - 177150919
Host address (hex) - A8F1BC7
Network address - 10.143.27.192
Network mask - 255.255.255.224
Network mask (bits) - 27
Network mask (hex) - FFFFFFE0
Broadcast address - 10.143.27.223
Cisco wildcard - 0.0.0.31
Addresses in network - 32
Network range - 10.143.27.192 - 10.143.27.223
Usable range - 10.143.27.193 - 10.143.27.222</pre>

&nbsp;

Notable mention:  
Web tools are also useful and are becoming more prolific than the UNIX tools, but I will assume that you&#8217;re probably already loged into a UNIX system like a jump box or bastion host anyway and the tools are faster and thinner in that environment. That said, here are some useful web tools:

<a href="http://jodies.de/ipcalc" target="_blank">ipcalc</a> has the web interface to their tool.

<a href="http://www.gestioip.net/cgi-bin/subnet_calculator.cgi" target="_blank">This site </a>has a v4 and v6 calculator that works well and looks a lot like the output of sipcalc.

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1039" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1039" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1039" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1039" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2014/07/nix4neteng-3-ip-addressing-and-subnet-tools/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>