---
id: 688
title: VMWare ESXi CLI reference
date: 2013-06-30T08:08:11-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=688
themeblvd_pagetitle:
  - 'true'
themeblvd_title:
  - VMWare ESX CLI reference
themeblvd_keywords:
  - VMware, termina, shell, ssh, CLI
themeblvd_description:
  - Command reference for using VMware from the CLI
themeblvd_noindex:
  - 'true'
dsq_thread_id:
  - "3627407189"
---
All of these commands require ssh to be enabled on the VMware host and were tested on 5.1.

Power off a VM

<pre class="wp-block-preformatted">vim-cmd vmsvc/power.getstate</pre>

List power state of VM:

<pre class="wp-block-preformatted">vim-cmd vmsvc/power.of</pre>

Power on VM

<pre class="wp-block-preformatted">vim-cmd vmsvc/power.on</pre>

List all VMs:

<pre class="wp-block-preformatted">vim-cmd vmsvc/getallvms</pre>

Other important commands under vmsvc:

<pre class="wp-block-preformatted">acquiremksticket get.snapshotinfo<br />acquireticket get.spaceNeededForConsolidation<br />connect get.summary<br />convert.toTemplate get.tasklist<br />convert.toVm getallvms<br />createdummyvm gethostconstraints<br />destroy login<br />device.connection logout<br />device.connusbdev message<br />device.disconnusbdev power.getstate<br />device.diskadd power.hibernate<br />device.diskaddexisting power.off<br />device.diskremove power.on<br />device.getdevices power.reboot<br />device.toolsSyncSet power.reset<br />device.vmiadd power.shutdown<br />device.vmiremove power.suspend<br />devices.createnic power.suspendResume<br />disconnect queryftcompat<br />get.capability reload<br />get.config setscreenres<br />get.config.cpuidmask snapshot.create<br />get.configoption snapshot.dumpoption<br />get.datastores snapshot.get<br />get.disabledmethods snapshot.remove<br />get.environment snapshot.removeall<br />get.filelayout snapshot.revert<br />get.filelayoutex snapshot.setoption<br />get.guest tools.cancelinstall<br />get.guestheartbeatStatus tools.install<br />get.managedentitystatus tools.upgrade<br />get.networks unregister<br />get.runtime upgrade</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-688" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-688" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-688" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-688" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/vmware-esxi-cli-reference/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>