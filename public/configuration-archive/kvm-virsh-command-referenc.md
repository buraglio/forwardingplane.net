---
id: 472
title: KVM virsh command reference
date: 2013-03-01T14:28:32-06:00
author: Nick Buraglio
layout: page
guid: http://www.forwardingplane.net/?page_id=472
themeblvd_pagetitle:
  - 'true'
themeblvd_noindex:
  - 'true'
themeblvd_title:
  - virsh --help output
themeblvd_keywords:
  - KVM, Virtualization, VMware, UNIX, CentOS, Linux
themeblvd_description:
  - 'Quick command reference for the KVM virsh command. '
dsq_thread_id:
  - "3627599523"
---
From the help command, here is a reference sheet for the virsh command:

<pre>virsh [options]... [&lt;command_string&gt;]
virsh [options]... &lt;command>&lt;/command> [args...]

  options:
    -c | --connect=URI      hypervisor connection URI
    -r | --readonly         connect readonly
    -d | --debug=NUM        debug level [0-4]
    -h | --help             this help
    -q | --quiet            quiet mode
    -t | --timing           print timing information
    -l | --log=FILE         output logging to file
    -v                      short version
    -V                      long version
         --version[=TYPE]   version, TYPE is short or long (default short)
    -e | --escape     set escape sequence for console

  commands (non interactive mode):

 Domain Management (help keyword 'domain')
    attach-device                  attach device from an XML file
    attach-disk                    attach disk device
    attach-interface               attach network interface
    autostart                      autostart a domain
    blkdeviotune                   Set or query a block device I/O tuning parameters.
    blkiotune                      Get or set blkio parameters
    blockcopy                      Start a block copy operation.
    blockjob                       Manage active block operations
    blockpull                      Populate a disk from its backing image.
    blockresize                    Resize block device of domain.
    change-media                   Change media of CD or floppy drive
    console                        connect to the guest console
    cpu-baseline                   compute baseline CPU
    cpu-compare                    compare host CPU with a CPU described by an XML file
    cpu-stats                      show domain cpu statistics
    create                         create a domain from an XML file
    define                         define (but don't start) a domain from an XML file
    desc                           show or set domain's description or title
    destroy                        destroy (stop) a domain
    detach-device                  detach device from an XML file
    detach-disk                    detach disk device
    detach-interface               detach network interface
    domid                          convert a domain name or UUID to domain id
    domif-setlink                  set link state of a virtual interface
    domiftune                      get/set parameters of a virtual interface
    domjobabort                    abort active domain job
    domjobinfo                     domain job information
    domname                        convert a domain id or UUID to domain name
    dompmsuspend                   suspend a domain for a given time duration
    domuuid                        convert a domain name or id to domain UUID
    domxml-from-native             Convert native config to domain XML
    domxml-to-native               Convert domain XML to native config
    dump                           dump the core of a domain to a file for analysis
    dumpxml                        domain information in XML
    edit                           edit XML configuration for a domain
    inject-nmi                     Inject NMI to the guest
    send-key                       Send keycodes to the guest
    managedsave                    managed save of a domain state
    managedsave-remove             Remove managed save of a domain
    maxvcpus                       connection vcpu maximum
    memtune                        Get or set memory parameters
    migrate                        migrate domain to another host
    migrate-setmaxdowntime         set maximum tolerable downtime
    migrate-setspeed               Set the maximum migration bandwidth
    migrate-getspeed               Get the maximum migration bandwidth
    numatune                       Get or set numa parameters
    reboot                         reboot a domain
    reset                          reset a domain
    restore                        restore a domain from a saved state in a file
    resume                         resume a domain
    save                           save a domain state to a file
    save-image-define              redefine the XML for a domain's saved state file
    save-image-dumpxml             saved state domain information in XML
    save-image-edit                edit XML for a domain's saved state file
    schedinfo                      show/set scheduler parameters
    screenshot                     take a screenshot of a current domain console and store it into a file
    setmaxmem                      change maximum memory limit
    setmem                         change memory allocation
    setvcpus                       change number of virtual CPUs
    shutdown                       gracefully shutdown a domain
    start                          start a (previously defined) inactive domain
    suspend                        suspend a domain
    ttyconsole                     tty console
    undefine                       undefine a domain
    update-device                  update device from an XML file
    vcpucount                      domain vcpu counts
    vcpuinfo                       detailed domain vcpu information
    vcpupin                        control or query domain vcpu affinity
    vncdisplay                     vnc display

 Domain Monitoring (help keyword 'monitor')
    domblkerror                    Show errors on block devices
    domblkinfo                     domain block device size information
    domblklist                     list all domain blocks
    domblkstat                     get device block stats for a domain
    domcontrol                     domain control interface state
    domif-getlink                  get link state of a virtual interface
    domiflist                      list all domain virtual interfaces
    domifstat                      get network interface stats for a domain
    dominfo                        domain information
    dommemstat                     get memory statistics for a domain
    domstate                       domain state
    list                           list domains

 Host and Hypervisor (help keyword 'host')
    capabilities                   capabilities
    connect                        (re)connect to hypervisor
    freecell                       NUMA free memory
    hostname                       print the hypervisor hostname
    nodecpustats                   Prints cpu stats of the node.
    nodeinfo                       node information
    nodememstats                   Prints memory stats of the node.
    nodesuspend                    suspend the host node for a given time duration
    qemu-attach                    QEMU Attach
    qemu-monitor-command           QEMU Monitor Command
    sysinfo                        print the hypervisor sysinfo
    uri                            print the hypervisor canonical URI
    version                        show version

 Interface (help keyword 'interface')
    iface-begin                    create a snapshot of current interfaces settings, which can be later committed (iface-commit) or restored (iface-rollback)
    iface-bridge                   create a bridge device and attach an existing network device to it
    iface-commit                   commit changes made since iface-begin and free restore point
    iface-define                   define (but don't start) a physical host interface from an XML file
    iface-destroy                  destroy a physical host interface (disable it / "if-down")
    iface-dumpxml                  interface information in XML
    iface-edit                     edit XML configuration for a physical host interface
    iface-list                     list physical host interfaces
    iface-mac                      convert an interface name to interface MAC address
    iface-name                     convert an interface MAC address to interface name
    iface-rollback                 rollback to previous saved configuration created via iface-begin
    iface-start                    start a physical host interface (enable it / "if-up")
    iface-unbridge                 undefine a bridge device after detaching its slave device
    iface-undefine                 undefine a physical host interface (remove it from configuration)

 Network Filter (help keyword 'filter')
    nwfilter-define                define or update a network filter from an XML file
    nwfilter-dumpxml               network filter information in XML
    nwfilter-edit                  edit XML configuration for a network filter
    nwfilter-list                  list network filters
    nwfilter-undefine              undefine a network filter

 Networking (help keyword 'network')
    net-autostart                  autostart a network
    net-create                     create a network from an XML file
    net-define                     define (but don't start) a network from an XML file
    net-destroy                    destroy (stop) a network
    net-dumpxml                    network information in XML
    net-edit                       edit XML configuration for a network
    net-info                       network information
    net-list                       list networks
    net-name                       convert a network UUID to network name
    net-start                      start a (previously defined) inactive network
    net-undefine                   undefine an inactive network
    net-uuid                       convert a network name to network UUID

 Node Device (help keyword 'nodedev')
    nodedev-create                 create a device defined by an XML file on the node
    nodedev-destroy                destroy (stop) a device on the node
    nodedev-detach                 detach node device from its device driver
    nodedev-dumpxml                node device details in XML
    nodedev-list                   enumerate devices on this host
    nodedev-reattach               reattach node device to its device driver
    nodedev-reset                  reset node device

 Secret (help keyword 'secret')
    secret-define                  define or modify a secret from an XML file
    secret-dumpxml                 secret attributes in XML
    secret-get-value               Output a secret value
    secret-list                    list secrets
    secret-set-value               set a secret value
    secret-undefine                undefine a secret

 Snapshot (help keyword 'snapshot')
    snapshot-create                Create a snapshot from XML
    snapshot-create-as             Create a snapshot from a set of args
    snapshot-current               Get or set the current snapshot
    snapshot-delete                Delete a domain snapshot
    snapshot-dumpxml               Dump XML for a domain snapshot
    snapshot-edit                  edit XML for a snapshot
    snapshot-list                  List snapshots for a domain
    snapshot-parent                Get the name of the parent of a snapshot
    snapshot-revert                Revert a domain to a snapshot

 Storage Pool (help keyword 'pool')
    find-storage-pool-sources-as   find potential storage pool sources
    find-storage-pool-sources      discover potential storage pool sources
    pool-autostart                 autostart a pool
    pool-build                     build a pool
    pool-create-as                 create a pool from a set of args
    pool-create                    create a pool from an XML file
    pool-define-as                 define a pool from a set of args
    pool-define                    define (but don't start) a pool from an XML file
    pool-delete                    delete a pool
    pool-destroy                   destroy (stop) a pool
    pool-dumpxml                   pool information in XML
    pool-edit                      edit XML configuration for a storage pool
    pool-info                      storage pool information
    pool-list                      list pools
    pool-name                      convert a pool UUID to pool name
    pool-refresh                   refresh a pool
    pool-start                     start a (previously defined) inactive pool
    pool-undefine                  undefine an inactive pool
    pool-uuid                      convert a pool name to pool UUID

 Storage Volume (help keyword 'volume')
    vol-clone                      clone a volume.
    vol-create-as                  create a volume from a set of args
    vol-create                     create a vol from an XML file
    vol-create-from                create a vol, using another volume as input
    vol-delete                     delete a vol
    vol-download                   Download a volume to a file
    vol-dumpxml                    vol information in XML
    vol-info                       storage vol information
    vol-key                        returns the volume key for a given volume name or path
    vol-list                       list vols
    vol-name                       returns the volume name for a given volume key or path
    vol-path                       returns the volume path for a given volume name or key
    vol-pool                       returns the storage pool for a given volume key or path
    vol-resize                     resize a vol
    vol-upload                     upload a file into a volume
    vol-wipe                       wipe a vol

 Virsh itself (help keyword 'virsh')
    cd                             change the current directory
    echo                           echo arguments
    exit                           quit this interactive terminal
    help                           print help
    pwd                            print the current directory
    quit                           quit this interactive terminal

  (specify help  for details about the commands in the group)

  (specify help &lt;command>&lt;/command> for details about the command)</pre>

<div class="sharedaddy sd-sharing-enabled">
  <div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing">
    <h3 class="sd-title">
      Share this:
    </h3>
    
    <div class="sd-content">
      <ul>
        <li class="share-twitter">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-472" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
        </li>
        <li class="share-email">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
        </li>
        <li class="share-print">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/" target="_blank" title="Click to print"><span>Print</span></a>
        </li>
        <li class="share-linkedin">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-472" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
        </li>
        <li class="share-facebook">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-472" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
        </li>
        <li class="share-reddit">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
        </li>
        <li class="share-tumblr">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
        </li>
        <li class="share-pinterest">
          <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-472" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
        </li>
        <li class="share-pocket">
          <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/configuration-archive/kvm-virsh-command-referenc/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
        </li>
        <li class="share-end">
        </li>
      </ul>
    </div>
  </div>
</div>