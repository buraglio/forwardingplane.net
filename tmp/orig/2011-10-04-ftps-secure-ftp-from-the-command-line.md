I have recently enabled [Duo Security](http://www.duosecurity.com/) for many of my personal services, and I can&#8217;t recommend them enough. Personal [two factor authentication](http://en.wikipedia.org/wiki/Two-factor_authentication) is very useful and really powerful. It works on my iPhone and I have yet to run into any real issues&#8230;.except for one. I can&#8217;t use automation to scp or sftp anything anymore and keep my two factor auth working in a way I&#8217;m comfortable with.

Enter [ftps](http://en.wikipedia.org/wiki/Ftps). FTP is a terrible, yet immensely useful protocol. I chose to use [vsftp](https://security.appspot.com/vsftpd.html) under debian Linux with Implicit TLS/SSL, meaning there is no negotiation of protocol as with explicit ftps (or ftpes). It&#8217;s secure, or none.

Configuring this is pretty easy, but it does require some editing of the /etc/vsftpd.conf file. I added some stuff to make it do ftpes as such:

_ssl_enable=YES  
  
allow\_anon\_ssl=NO  
  
force\_local\_data_ssl=YES  
  
force\_local\_logins_ssl=YES  
  
rsa\_cert\_file=/etc/ssl/certs/vsftpd.pem  
  
_ 

This and a few other tweaks that aren&#8217;t relevant here, make ftpes work on my machine.

Now, clients are another story. Most of the modern GUI based clients work. I know [filezilla](http://filezilla-project.org/) works, and it&#8217;s free. The problem I have, is that I need to do this programmatically, via a script.

A bit of digging didn&#8217;t yield much, however, I did come across [lftp](http://lftp.yar.ru/). lftp is an extremely powerful command line ftp client that has a LOT of features, one of which is ftpes support. Now, the one problem with lftp is that it is extremely full featured. Like, overly featured. So much so, that it can be a bit daunting to make it do what you want, which in my case was pretty simple.

I wrote a simple script to make it do what I wanted, which was just to upload a file and move it around.

_  
  
#!/bin/sh  
  
_ _/usr/bin/lftp -u user,password remote.host.com_ _<eof cd="" www="" lcd="" mnt="" nas\_vol\_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i=""></eof>_

<div style="display: inline !important; ">
  <i><<eof<eof<eof<eof< div=""></eof<eof<eof<eof<></i><i><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i=""></p> 
  
  <div>
    cd data
  </div>
  
  <div>
    lcd /mnt/NAS/files/updates
  </div>
  
  <div>
    put updates.txt
  </div>
  
  <div>
    mv updates.txt data.txt
  </div>
  
  <div>
    quit 0
  </div>
  
  <div>
    EOF
  </div>
  
  <div>
  </div>
  
  <p>
    </eof></i>
  </p>
  
  <div>
    <eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i="">This works fine, and since I&#8217;m using ftpes, it does all of the negotiation for me.</p> 
    
    <p>
      </eof>
    </p>
    
    <div>
    </div>
    
    <div>
      <i><eof cd="" www="" lcd="" mnt="" nas_vol_4="" files="" update="" put="" txt="" mv="" quit="" 0="" eof="" i=""><br /> <br /></eof></i>
    </div>
  </div></div> 
  
  <div>
    [[ This is a content summary only. Visit my website for full links, other content, and more! ]]
  </div>
  
  <div class="sharedaddy sd-sharing-enabled">
    <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
      <h3 class="sd-title">
        Share this:
      </h3>
      
      <div class="sd-content">
        <ul>
          <li class="share-twitter">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-28" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
          </li>
          <li class="share-email">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
          </li>
          <li class="share-print">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/" target="_blank" title="Click to print"><span>Print</span></a>
          </li>
          <li class="share-linkedin">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-28" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
          </li>
          <li class="share-facebook">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-28" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
          </li>
          <li class="share-reddit">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
          </li>
          <li class="share-tumblr">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
          </li>
          <li class="share-pinterest">
            <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-28" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
          </li>
          <li class="share-pocket">
            <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/10/ftps-secure-ftp-from-the-command-line/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
          </li>
          <li class="share-end">
          </li>
        </ul>
      </div>
    </div>
  </div>
