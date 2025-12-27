---
title: Hosted email options for 2026
date: 2025-12-26
author: Nick Buraglio
layout: post
categories:
    - ipv6
    - email
    - cloud
tags:
    - ipv6
    - email
    - cloud
    - productivity
---

Email. Possibly the most useful and least sexy of the core set of internet applictions. In past lives I ran exchange, postfix, CC:Mail, and very, very large sendmail installations. Since early 2005, though, I have outsourced my own personal email to Google. As an original "google Apps for Your Domain" tester, I had early access to the bevy of tools that Google had to offer, and at my favorite price - $0. 
Occasionally I'd look at other options, but I always come back to GSuite.

This time around I put some time into it, taking some notes and fully intending to try to move my primary domain away. I had a set of "must" requirements, but am willing to make some major concessions.

### Must do: 

- Web Interface
- Integrated calendar support
- Vacation / Away message
- Up to 10 users (negotiable - 6 would work)
- Decent Spam control
- Filtering / tagging with robust match criteria
- Reasonably strong email search capabilities

### Nice to have, weighted 1st to last

- Supports Email Alias 
- Supports multi-recepient aliases
- Suports IPv6
- Supports catch-all for domain
- Drive / storage support
- Office / Productivity suite included


### Out of scope

- Self Hosting. 

I've tasted that pain and simply have no desire to do it again.

---

I will also add that I do, in fact, like gmail hossting. It's worked for me for literally two decades. It has essentially everything I need and my requirements are fairly tightly tied to it. Coincidentally, one of the largest concerns I have for this potential move is that 1. I will miss something I truly need, and secondarily, but only slightly, that I will have a bear of a time de-coupling what I use "Login with Google" for. Ideally those things would all become passkeys, but we all know that process is low. 
A looming, but not insignificant issue, too, is the mining of my data for advertising (kinda came to grips with that, sadly) and more concerningly AI. Google is all-in and I don't necessarily want my personal email to be used for that even if it is largely inevitable due to the sheer footprint of gmail. I like privacy, and did move one of my mail domains to proton for about 8 months a few years ago.

## 1. Overall positioning

| Service | Primary Focus | Privacy / Data Handling | Ideal For |
|----------|----------------|--------------------------|------------|
| **Google Workspace** | Business collaboration suite with Gmail, Docs, Drive, and Meet | Secure, but U.S.-based; metadata processed in cloud | Families comfortable with a business-tier plan for strong collaboration |
| **Apple iCloud+ / Apple One Mail** | Consumer services integrated into Apple devices | Apple-managed, privacy-conscious but not E2EE mail | All-Apple households wanting simple setup |
| **Proton Family** | Privacy-first encrypted bundle: Mail, Calendar, Drive, VPN, Pass | Swiss jurisdiction, zero-access encryption | Families prioritizing privacy and independence from Big Tech |
| **Microsoft 365 Family** | Consumer Office suite + Outlook + 1 TB OneDrive per user | Secure U.S-based enterprise infrastructure | Windows/macOS families needing storage & Office apps |

---

## 2. Custom domains, aliases, and groups

| Feature                            | Google Workspace | Apple iCloud+ / Apple One | Proton Family | Microsoft 365 Family |
|------------------------------------|------------------|----------------------------|----------------|----------------------|
| **Custom domain email**            | Yes, core feature | Yes, via iCloud+ setup | Yes, multiple domains | No native (requires business plan) |
| **Plan structure**                 | Per-user business | Family Sharing (6 users) | Family plan (multiple users) | 6-person family plan |
| **Email aliases per user**         | Up to 30 | 3–5 | Multiple per user | Up to 10 aliases |
| **Shared/group address support**   | Yes, groups + shared mailboxes | No built-in groups | No shared inbox, forwarding only | No consumer groups |
| **Catch-all**                      | Supported | Not available | Supported | Not supported |

---

## 3. Cloud ecosystems and integration

| Category | Google Workspace | Apple iCloud+ | Proton Family | Microsoft 365 Family |
|-----------|------------------|----------------|----------------|----------------------|
| **Email client** | Gmail Web & Mobile | Apple Mail/iCloud.com | Proton apps + Bridge | Outlook desktop/web/mobile |
| **Documents/Office** | Docs, Sheets, Slides | Pages, Numbers, Keynote | – | Word, Excel, PowerPoint |
| **Storage** | Google Drive | iCloud Drive | Proton Drive (encrypted) | OneDrive (1 TB/user) |
| **Calendar** | Google Calendar | Calendar | Proton Calendar | Outlook Calendar |
| **Password Manager** | Google Password Manager | iCloud Keychain | Proton Pass | Microsoft Autofill |
| **VPN / Privacy** | None | Private Relay (limited) | Proton VPN included | Defender VPN limited rollout |
| **Cross-platform quality** | Excellent | Best on Apple | Cross-platform (privacy focus) | Excellent, esp. Windows |

---

## 4. Spam filtering and rule flexibility

| Aspect | Google Workspace | Apple iCloud+ | Proton Family | Microsoft 365 Family |
|---------|------------------|----------------|----------------|----------------------|
| **Spam filtering** | Industry-leading, ML-powered | Very good, less configurable | Excellent but strict | Enterprise-grade |
| **User filters/rules** | Full Gmail filter engine | Basic server filters | Rules & labels | Rich Outlook rules |
| **Inbox organization** | Primary/Social/Promotions tabs | Standard folders | Folders/labels | Focused Inbox |
| **Anti-abuse/controls** | Mature | Basic | Strong | Enterprise-class |

---

## 5. Network and standards (corrected IPv6 info)

| Protocol / Standard | Google Workspace | Apple iCloud Mail | Proton Mail / Family | Microsoft 365 Family |
|----------------------|------------------|--------------------|----------------------|----------------------|
| **IPv6 support (MX)** | ✅ Dual-stack IPv6/IPv4 | ✅ Dual-stack | ❌ IPv4-only – no MX AAAA records | ✅ Dual-stack |
| **SPF/DKIM/DMARC** | Fully supported | Automatic (Apple-managed) | Fully supported | Fully supported |
| **DNS management** | Full control | Limited iCloud setup | Full DNS control | Limited unless business plan |
| **Protocol support** | IMAP/POP/SMTP, Web | IMAP/SMTP | Proton Bridge (IMAP/SMTP) | IMAP/POP/Exchange ActiveSync |

> **Note:** Proton Mail supports IPv6 for its VPN and general web properties, but not yet for incoming email delivery (MX hosts remain IPv4-only).

---

## 6. Approximate pricing (2025 USA Market)

| Service | Plan | Yearly Approx. Cost | Users | Storage |
|----------|------|---------------------|--------|----------|
| **Google Workspace** | Business Starter | ~$72/user/year | Per-user | 30 GB/user |
| **Apple iCloud+** | Family (200GB–2TB) | ~$36–$120/year | Up to 6 | 200 GB–2 TB shared |
| **Proton Family** | Proton Family bundle | ~$240–$360/year | ~6 | 500 GB–3 TB encrypted |
| **Microsoft 365 Family** | Family plan | ~$100/year | Up to 6 | 1 TB/user (6 TB total) |

---

## 7. Summary Recommendations

| Priority | Best Fit |
|-----------|-----------|
| **All-around collaboration and admin** | Google Workspace |
| **Apple-only household simplicity** | iCloud+ Family |
| **Privacy-first and encryption** | Proton Family |
| **Cross-platform productivity + storage** | Microsoft 365 Family |

---

## 8. Key Takeaways

- **Proton Mail lacks IPv6 on MX** (IPv4-only inbound mail).  
- **Google Workspace** and **Microsoft 365** deliver enterprise-grade spam filtering with proper IPv6 dual-stack.  
- **Apple iCloud+** offers simple family sharing and domain email for Apple users.  
- **Proton Family** is the strict privacy champion but trades off deeper mail routing and IPv6.  

---

_Last updated: December 2025._
