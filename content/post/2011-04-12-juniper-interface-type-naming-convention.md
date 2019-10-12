I found most of this on a web page somewhere tha tI can&#8217;t seem to find again. Below are some common useful junos tidbits regarding routing tables and interface types/names:

JunOS CLI supports the basic grep command (like | include) so any show commands can be grepped. I believe the grep command implies the -i flag for case insensitivity.

The routing table is presented in such a way to group types of routes.

**<span>inet.0 is the ipv4 unicast routing table</p> 

<p>
  </span></b>
</p>

<div>
  <b><span>inet.1 is the ipv4 multicast routing table</p> 
  
  <p>
    </span></b></div> 
    
    <div>
      <b><span>inet.3 is the MPLS routing table</p> 
      
      <p>
        </span></b></div> 
        
        <div>
          <b><span>inet6.0 is the ipv6 routing table</span></b></p> 
          
          <p>
            Juniper interface types
          </p>
          
          <p>
            Most common ones you&#8217;ll probably see:
          </p>
          
          <p>
            <b>fe: Fast Ethernet 100Base-TX (Fast Ethernet, 100 Mbps).</p> 
            
            <p>
              fxp0: Management and internal Ethernet The management Ethernet interface is an out-of-band management interface within the routing platform.
            </p>
            
            <p>
              fxp1: Interface that connects the routing engine and packet forwarding engine.
            </p>
            
            <p>
              xe: 1GE optical interface on ex switches
            </p>
            
            <p>
              ge: Gigabit and 10gigabit Ethernet. Includes Gigabit Ethernet IQ interfaces.
            </p>
            
            <p>
              me0: &#8211; out of band management interface on ex switches
            </p>
            
            <p>
              lo: Loopback This interface is internally generated. The logical interface lo0.16383 is a non-configurable interface for routing platform control traffic.
            </p>
            
            <p>
              vcp: &#8211; virtual chassis interface (EX4200 only)
            </p>
            
            <p>
              Other ones you may run into:
            </p>
            
            <p>
              ae: Aggregated Ethernet A virtual aggregated link.
            </p>
            
            <p>
              </b>
            </p>
            
            <div>
              <b>as: Aggregated SONET/SDH A virtual aggregated link.</p> 
              
              <p>
                </b></div> 
                
                <div>
                  <b>at: ATM1 or ATM2 IQ Asynchronous Transfer Mode</p> 
                  
                  <p>
                    </b></div> 
                    
                    <div>
                      <b>cau4: Channelized AU-4 IQ Configured on the Channelized STM-1 IQ PIC.</p> 
                      
                      <p>
                        </b></div> 
                        
                        <div>
                          <b>coc1: Channelized OC-1 IQ Configured on the Channelized OC-12 IQ PIC.</p> 
                          
                          <p>
                            </b></div> 
                            
                            <div>
                              <b>coc12: Channelized OC-12 IQ Configured on the Channelized OC-12 IQ PIC.</p> 
                              
                              <p>
                                </b></div> 
                                
                                <div>
                                  <b>cstm1: Channelized STM-1 IQ Configured on the Channelized STM-1 IQ PIC.</p> 
                                  
                                  <p>
                                    </b></div> 
                                    
                                    <div>
                                      <b>ce1: Channelized E1 IQ Configured on the Channelized E1 IQ PIC or Channelized STM-1 IQ PIC.</p> 
                                      
                                      <p>
                                        </b></div> 
                                        
                                        <div>
                                          <b>ct1: Channelized T1 IQ Configured on the Channelized DS-3 IQ PIC or Channelized OC-12 IQ PIC.</p> 
                                          
                                          <p>
                                            </b></div> 
                                            
                                            <div>
                                              <b>ct3: Channelized T3 IQ Configured on the Channelized DS-3 IQ PIC or Channelized OC-12 IQ PIC.</p> 
                                              
                                              <p>
                                                </b></div> 
                                                
                                                <div>
                                                  <b>cp: Collector Configured on the Monitoring Services II PIC.</p> 
                                                  
                                                  <p>
                                                    </b></div> 
                                                    
                                                    <div>
                                                      <b>ds: DS-0 Configured on the Channelized DS-3 to DS-0 PIC, Channelized E1 PIC, Channelized OC-12 IQ PIC,</p> 
                                                      
                                                      <p>
                                                        </b></div> 
                                                        
                                                        <div>
                                                          <b>dsc: Discard Allows you to identify the ingress point of a denial-of-service (DoS) attack.</p> 
                                                          
                                                          <p>
                                                            </b></div> 
                                                            
                                                            <div>
                                                              <b>e1: E1 Includes the channelized STM-1 to E1 interfaces.</p> 
                                                              
                                                              <p>
                                                                </b></div> 
                                                                
                                                                <div>
                                                                  <b>e3: E3 Includes the E3 IQ interfaces.</p> 
                                                                  
                                                                  <p>
                                                                    </b></div> 
                                                                    
                                                                    <div>
                                                                      <b>es: Encryption, Allows you to configure a security association (SA) name with a logical interface.</p> 
                                                                      
                                                                      <p>
                                                                        </b></div> 
                                                                        
                                                                        <div>
                                                                          <b>gr: Generic Route Encapsulation tunnel Allows you to configure a unicast tunnel using GRE encapsulation.</p> 
                                                                          
                                                                          <p>
                                                                            </b></div> 
                                                                            
                                                                            <div>
                                                                              <b>gre: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                              
                                                                              <p>
                                                                                </b></div> 
                                                                                
                                                                                <div>
                                                                                  <b>ip: IP-over-IP encapsulation tunnel Allows you to configure a unicast tunnel using IP-IP encapsulation.</p> 
                                                                                  
                                                                                  <p>
                                                                                    </b></div> 
                                                                                    
                                                                                    <div>
                                                                                      <b>ipip: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                      
                                                                                      <p>
                                                                                        </b></div> 
                                                                                        
                                                                                        <div>
                                                                                          <b>ls: Link services Supports bundles that contain links.</p> 
                                                                                          
                                                                                          <p>
                                                                                            </b></div> 
                                                                                            
                                                                                            <div>
                                                                                              <b>lsi: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                              
                                                                                              <p>
                                                                                                </b></div> 
                                                                                                
                                                                                                <div>
                                                                                                  <b>ml: Multilink Includes Multilink Frame Relay and Multilink PPP.</p> 
                                                                                                  
                                                                                                  <p>
                                                                                                    </b></div> 
                                                                                                    
                                                                                                    <div>
                                                                                                      <b>mo: Monitoring services Includes the monitoring services and monitoring services<br />II interfaces: The logical interface mo-fpc/pic/port.16383 is an internally generated, non-configurable interface for routing platform control traffic.</p> 
                                                                                                      
                                                                                                      <p>
                                                                                                        </b></div> 
                                                                                                        
                                                                                                        <div>
                                                                                                          <b>mt: Multicast tunnel Internal routing platform interface for VPNs.</p> 
                                                                                                          
                                                                                                          <p>
                                                                                                            </b></div> 
                                                                                                            
                                                                                                            <div>
                                                                                                              <b>mtun: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                                              
                                                                                                              <p>
                                                                                                                </b></div> 
                                                                                                                
                                                                                                                <div>
                                                                                                                  <b>oc3: OC-3 IQ Configured on the Channelized OC-12 IQ PIC.</p> 
                                                                                                                  
                                                                                                                  <p>
                                                                                                                    </b></div> 
                                                                                                                    
                                                                                                                    <div>
                                                                                                                      <b>pe: This interface is present on the first-hop routing platform. Encapsulates packets destined for the rendezvous point (RP) routing platform.</p> 
                                                                                                                      
                                                                                                                      <p>
                                                                                                                        </b></div> 
                                                                                                                        
                                                                                                                        <div>
                                                                                                                          <b>pd: This interface is present on the RP De-encapsulates packets at the RP.</p> 
                                                                                                                          
                                                                                                                          <p>
                                                                                                                            </b></div> 
                                                                                                                            
                                                                                                                            <div>
                                                                                                                              <b>pimd: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                                                              
                                                                                                                              <p>
                                                                                                                                </b></div> 
                                                                                                                                
                                                                                                                                <div>
                                                                                                                                  <b>pime: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                                                                  
                                                                                                                                  <p>
                                                                                                                                    </b></div> 
                                                                                                                                    
                                                                                                                                    <div>
                                                                                                                                      <b>rlsq: &#8211; a redundant bundle interface, made of two or more lsq interface. If you have redundant AS Pics.</p> 
                                                                                                                                      
                                                                                                                                      <p>
                                                                                                                                        </b></div> 
                                                                                                                                        
                                                                                                                                        <div>
                                                                                                                                          <b>se: Serial Includes the EIA-530, V.35, and X.21 interfaces.</p> 
                                                                                                                                          
                                                                                                                                          <p>
                                                                                                                                            </b></div> 
                                                                                                                                            
                                                                                                                                            <div>
                                                                                                                                              <b>so: SONET/SDH Both are widely used methods for very high speed transmission of voice and data signals across the numerous world-wide fiber-optic networks.</p> 
                                                                                                                                              
                                                                                                                                              <p>
                                                                                                                                                </b></div> 
                                                                                                                                                
                                                                                                                                                <div>
                                                                                                                                                  <b>sp: Adaptive services The logical interface sp-fpc/pic/port.16383 is an internally generated, non-configurable interface for routing platform control traffic.</p> 
                                                                                                                                                  
                                                                                                                                                  <p>
                                                                                                                                                    </b></div> 
                                                                                                                                                    
                                                                                                                                                    <div>
                                                                                                                                                      <b>t1: T1 Includes the channelized DS-3 to DS-1 interfaces.</p> 
                                                                                                                                                      
                                                                                                                                                      <p>
                                                                                                                                                        </b></div> 
                                                                                                                                                        
                                                                                                                                                        <div>
                                                                                                                                                          <b>t3: T3 Includes the channelized OC-12 to DS-3 interfaces.</p> 
                                                                                                                                                          
                                                                                                                                                          <p>
                                                                                                                                                            </b></div> 
                                                                                                                                                            
                                                                                                                                                            <div>
                                                                                                                                                              <b>tap: Internally generated This interface is internally generated and is not configurable.</p> 
                                                                                                                                                              
                                                                                                                                                              <p>
                                                                                                                                                                </b></div> 
                                                                                                                                                                
                                                                                                                                                                <div>
                                                                                                                                                                  <b>vsp: Voice services, The Adaptive Services (AS) Physical Interface Card (PIC) supports the compressed real-time transport protocol (RTP) on this interface.</p> 
                                                                                                                                                                  
                                                                                                                                                                  <p>
                                                                                                                                                                    </b></div> 
                                                                                                                                                                    
                                                                                                                                                                    <div>
                                                                                                                                                                      <b>vt: Virtual loopback tunnel On routing platforms equipped with a Tunnel PIC, enables egress filtering.<br /></b><br />Other interesting terminology regarding the juniper architecture is the module layout:</p> 
                                                                                                                                                                      
                                                                                                                                                                      <p>
                                                                                                                                                                        <b>RE: Routing Engine, Like a cisco supervisor module. Central brains of the system</p> 
                                                                                                                                                                        
                                                                                                                                                                        <p>
                                                                                                                                                                          </b>
                                                                                                                                                                        </p>
                                                                                                                                                                        
                                                                                                                                                                        <div>
                                                                                                                                                                          <b>PFE: Packet forwarding Engine. Controls the data packet forwarding of the system.</p> 
                                                                                                                                                                          
                                                                                                                                                                          <p>
                                                                                                                                                                            </b></div> 
                                                                                                                                                                            
                                                                                                                                                                            <div>
                                                                                                                                                                              <b>SCB: Switch control board. Contains ASICs that handle route lookups and memory management.</p> 
                                                                                                                                                                              
                                                                                                                                                                              <p>
                                                                                                                                                                                </b></div> 
                                                                                                                                                                                
                                                                                                                                                                                <div>
                                                                                                                                                                                  <b>PIC: Physical interface card. Sort of like a port, but can contain multiple interfaces.</p> 
                                                                                                                                                                                  
                                                                                                                                                                                  <p>
                                                                                                                                                                                    </b></div> 
                                                                                                                                                                                    
                                                                                                                                                                                    <div>
                                                                                                                                                                                      <b>FPC: Flexible PIC concentrator. Like a linecard that has module slots. Can handle different types of PICs</b>
                                                                                                                                                                                    </div></div> </div> 
                                                                                                                                                                                    
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
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-37" class="share-twitter sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-email">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="" class="share-email sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=email" target="_blank" title="Click to email this to a friend"><span>Email</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-print">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="" class="share-print sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/" target="_blank" title="Click to print"><span>Print</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-linkedin">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-37" class="share-linkedin sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=linkedin" target="_blank" title="Click to share on LinkedIn"><span>LinkedIn</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-facebook">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-37" class="share-facebook sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=facebook" target="_blank" title="Click to share on Facebook"><span>Facebook</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-reddit">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-tumblr">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="" class="share-tumblr sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=tumblr" target="_blank" title="Click to share on Tumblr"><span>Tumblr</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-pinterest">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="sharing-pinterest-37" class="share-pinterest sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=pinterest" target="_blank" title="Click to share on Pinterest"><span>Pinterest</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-pocket">
                                                                                                                                                                                              <a rel="nofollow noopener noreferrer" data-shared="" class="share-pocket sd-button share-icon" href="http://www.forwardingplane.net/2011/04/juniper-interface-type-naming-convention/?share=pocket" target="_blank" title="Click to share on Pocket"><span>Pocket</span></a>
                                                                                                                                                                                            </li>
                                                                                                                                                                                            <li class="share-end">
                                                                                                                                                                                            </li>
                                                                                                                                                                                          </ul>
                                                                                                                                                                                        </div>
                                                                                                                                                                                      </div>
                                                                                                                                                                                    </div>