---
title: 'Looking more deeply into iMessage'
date: Sun, 06 Nov 2011 23:28:00 +0000
draft: false
tags: [UNIX]
---

  
I've been looking at iMessage from time to time as my schedule permits, for some reason that I can't really explain I'm fixated on it.  So, just like I did with FaceTime, I started doing network sniffing to see just what it's doing.  The results were not terribly unexpected.    
  
  
   iPhone.buraglio.com.53140 > st11p01st-courier143-bz.push.apple.com.5223: Flags \[R\], cksum 0x5ec8 (correct), seq 4109691913, win 0, length 0  
14:07:51.665485 IP (tos 0x20, ttl 49, id 11699, offset 0, flags \[DF\], proto TCP (6), length 64, bad cksum 0 (->8fc7)!)  
    st11p01st-courier143-bz.push.apple.com.5223 > iPhone.buraglio.com.53140: Flags \[.\], cksum 0xb792 (correct), seq 76, ack 475, win 192, options \[nop,nop,TS val 154465503 ecr 230925781,nop,nop,sack 1 {474:475}\], length 0  
14:07:51.667170 IP (tos 0x20, ttl 64, id 22535, offset 0, flags \[DF\], proto TCP (6), length 40)  
    iPhone.buraglio.com.53140 > st11p01st-courier143-bz.push.apple.com.5223: Flags \[R\], cksum 0x5ec8 (correct), seq 4109691913, win 0, length 0  
14:07:51.677715 IP (tos 0x20, ttl 46, id 41627, offset 0, flags \[none\], proto TCP (6), length 52, bad cksum 0 (->f541)!)  

  
However, it appears to me, in my initial looking, that the outgoing message is inconsistently using the cellular data network.  I can replicate this by sending a message via my iPhone to another iMessage user, and I never see any traffic from that host on my network.  However, if I get a response, it comes back in similar to the capture above.  It would make sense to me that the service would use wifi when available as opposed to the more expensive cellular data.  
  
If I have my iPad on, I see that traffic as well as it only has wifi.  
  
  
    iPhone.buraglio.com.52084 > st11p01st-courier094-bz.push.apple.com.5223: Flags \[.\], cksum 0x7f0b (correct), seq 160, ack 2436, win 8122, options \[nop,nop,TS val 121427102 ecr 1305430889\], length 0  
    st11p01st-courier066-bz.push.apple.com.5223 > iPad.buraglio.com.57869: Flags \[P.\], cksum 0xbd1c (correct), seq 1327:2436, ack 160, win 501, options \[nop,nop,TS val 3197914588 ecr 1393723712\], length 1109  

  
  
So, nothing terribly conclusive so far in my small amount of testing, more data capture and variables to come.  

  

\[\[ This is a content summary only. Visit my website for full links, other content, and more! \]\]