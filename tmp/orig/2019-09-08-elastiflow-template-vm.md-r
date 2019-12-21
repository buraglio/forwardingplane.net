Flow data is a critical piece of understanding how your network works what what it is actively doing. It also provides a great baseline and capacity planning tool. However, some of the more feature rich NetFlow and/or sFlow collectors can be quite daunting in their cost and/or complexity to install. [ElastiFlow](https://github.com/robcowart/elastiflow) is a great alternative for flow analytics and is built on the well traveled and robust [ElasticStack](https://www.elastic.co/start?ultron=[EL]-[B]-[AMER]-US+CA-Exact&blade=adwords-s&Device=c&thor=elastic%20stack&gclid=EAIaIQobChMIuKC5xefB5AIVCYnICh0wEg5lEAAYASAAEgIp_fD_BwE), meaning, its back end is well documented, well supported, and scales exceptionally well. For those that would like to play around with this but don&#8217;t want to take the time to install it (see below for the instruction set I used), I have provided a simple VM to toy around with. <figure class="wp-block-image">

<img src="http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-1024x704.png" alt="" class="wp-image-1710" srcset="http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-1024x704.png 1024w, http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-300x206.png 300w, http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM-768x528.png 768w, http://www.forwardingplane.net/wp-content/uploads/2019/09/Screen-Shot-2019-09-07-at-11.00.35-PM.png 1487w" sizes="(max-width: 1024px) 100vw, 1024px" /> </figure> 

Included here is a vanilla Ubuntu 18 LTS VM with a basic [Elastiflow](https://github.com/robcowart/elastiflow) install. This includes all of the components of an ElasticStack plus the front end pieces of the ElastiFlow project. Most of the install is based on [this](https://www.catapultsystems.com/blogs/install-elastiflow-on-ubuntu-18-04-part-1/) how-to. 

Included in the image is also a base install of NGINX and certbot so that you can reverse proxy the access and have a valid SSL certificate. There are a plethora of guides on how to accomplish that task on the internet. 

This was build and validated on Proxmox 6.0.6 but should be able to run on VMWare as well with a bit of qemu-img conversion. As expected, ElastiFlow (and ElasticStack) are fairly resource hungry. 16G of Memory and a handful of CPU cores is the bare minimum to run this with any real efficiency. Additionally, Ubuntu 18 has changed how the networking is setup &#8211; it is all located in /etc/netplan/ now.     


Login Information:

<pre class="wp-block-preformatted">User Name: root
Password: elastiflow
Privileged user: elastiflow
Password: elastiflow<br /></pre>

Default IP addresses:

<pre class="wp-block-preformatted">10.255.255.5/27
2001:db8:ffff:2::5/64</pre>

Download the image [here](https://drive.google.com/open?id=1ga_Pj2j6h1ce9rcT7jQjncpVjLIC4X4t). 

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-1709" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-1709" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-1709" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-1709" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2019/09/elastiflow-template-vm/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>