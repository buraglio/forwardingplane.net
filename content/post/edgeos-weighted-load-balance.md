---
title: 'EdgeOS weighted load balance'
date: Mon, 18 Feb 2019 17:37:39 +0000
draft: false
---

```
set load-balance group LoadBalance\_WAN interface  route-test initial-delay 15  
set load-balance group LoadBalance\_WAN interface  route-test interval 5  
set load-balance group LoadBalance\_WAN interface  route-test type ping target   
set load-balance group LoadBalance\_WAN interface  weight 95 # weight based on more bandwidth   
set load-balance group LoadBalance\_WAN interface  route-test initial-delay 15  
set load-balance group LoadBalance\_WAN interface  route-test interval 5  
set load-balance group LoadBalance\_WAN interface  route-test type ping target   
set load-balance group LoadBalance\_WAN interface  weight 5 # weight based on less bandwidth
```