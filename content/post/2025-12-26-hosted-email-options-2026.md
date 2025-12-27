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

Email. Possibly the most useful and least sexy of the core set of internet applictions. In past lives I ran [Microsoft Exchange](https://en.wikipedia.org/wiki/Microsoft_Exchange_Server), [Postfix](https://en.wikipedia.org/wiki/Postfix_(software)), [cc:Mail](https://en.wikipedia.org/wiki/Cc:Mail), and very, very large [Sendmail](https://en.wikipedia.org/wiki/Sendmail) installations. Since early 2005, though, I have outsourced my own personal email to Google. As an original "google Apps for Your Domain" tester, I had early access to the bevy of tools that Google had to offer, and at my favorite price - $0. 
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

### Nice to have, no preference in weight:

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

I will also add that I do, in fact, like gmail hosting. It's worked for me for literally two decades. It has essentially everything I need and my requirements are fairly tightly tied to it. Coincidentally, one of the largest concerns I have for this potential move is that 1. I will miss something I truly need, and secondarily, but only slightly, that I will have a bear of a time de-coupling what I use "Login with Google" for. Ideally those things would all become passkeys, but we all know that process is slow.
A looming, but not insignificant issue, too, is the mining of my data for advertising (kinda came to grips with that, sadly) and more concerningly AI. Google is all-in and I don't necessarily want my personal email to be used for that even if it is largely inevitable due to the sheer footprint of gmail. I like privacy, and did move one of my mail domains to proton for about 8 months a few years ago.

This is obviously non-comprehensive and should be double checked as things chance and I can make mistakes.

# Comprehensive Family Email Service Comparison (2025)
## Google Workspace • Apple iCloud+ / Apple One Mail • [Proton Family; Referral Link](https://pr.tn/ref/XE0EKRE2) • Microsoft 365 Family • Cloudflare Email Routing

This post makes an attemt to compare, to the best possible approxomation:

- **Google Workspace**
- **Apple iCloud+ / Apple One Mail**
- **Proton Family**
- **Microsoft 365 Family**
- **Cloudflare Email Routing**

with emphasis on:

- Custom domains
- Aliases and groups
- Hosting vs forwarding (Cloudflare)
- Ecosystem / apps
- Spam filtering
- IPv6 and standards
- Costs and typical use cases

Cloudflare is fundamentally different from the other four: it provides **routing/forwarding**, not mailboxes or a hosted inbox, but it is powerful and could be used to simply move around an email address.

---

## 1. Overall positioning

| Service                     | Type of service                                   | Hosting vs forwarding                               | Ideal for                                                |
|----------------------------|---------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
| **Google Workspace**       | Full email + productivity suite                   | **Hosting**: mailboxes + apps                       | Families / small orgs wanting Gmail + Docs/Drive/Meet   |
| **Apple iCloud+ / One**    | Consumer iCloud storage + mail                    | **Hosting**: mailboxes in Apple’s cloud             | All‑Apple households                                     |
| **Proton Family**          | Privacy‑focused encrypted bundle                  | **Hosting**: encrypted mailboxes                    | Families prioritizing privacy and Swiss jurisdiction    |
| **Microsoft 365 Family**   | Consumer Office + Outlook + OneDrive              | **Hosting**: Outlook mailboxes                      | Families needing Office apps + 1 TB/user storage        |
| **Cloudflare Email Routing** | Email routing/forwarding layer only             | **Forwarding only**: no inboxes, no sending         | Using your own inbox elsewhere with free custom-domain addresses |

Cloudflare Email Routing acts as an SMTP “traffic director”: it receives mail for your domain, then forwards it on to another mailbox you own (Gmail, Outlook, Proton, etc.). It **does not** store mail long‑term or provide an inbox, and you cannot send mail directly from Cloudflare’s addresses without pairing it with another outbound provider.

---

## 2. Custom domains, aliases, and groups

### 2.1 Core domain & family structure

| Feature                            | Google Workspace          | Apple iCloud+ / One      | Proton Family                      | Microsoft 365 Family               | Cloudflare Email Routing                    |
|------------------------------------|---------------------------|--------------------------|-------------------------------------|------------------------------------|----------------------------------------------|
| Custom domain for email            | Yes (first‑class)         | Yes via iCloud+          | Yes, multiple domains               | Not in consumer; needs business   | Yes (for routing only)                       |
| Who owns the mailbox?             | Google                    | Apple                    | Proton                              | Microsoft                          | Your downstream provider (Gmail, etc.)       |
| “Family plan” concept              | Business plan used by family | iCloud Family Sharing | Dedicated family bundle             | Family plan (up to 6 users)       | N/A (per domain; no user accounts)          |
| Per‑user separation                | Full accounts             | Individual Apple IDs     | Separate encrypted accounts         | Separate Microsoft accounts        | Not applicable (no mailboxes)               |

### 2.2 Aliases, groups, and catch‑all

| Aspect                            | Google Workspace                         | Apple iCloud+                          | Proton Family                         | Microsoft 365 Family                  | Cloudflare Email Routing                                |
|-----------------------------------|------------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|--------------------------------------------------------|
| Aliases per user                  | Many (up to ~30)                         | Several per iCloud mailbox             | Multiple addresses/aliases per user    | Multiple per Outlook.com account      | Many routing rules per domain                          |
| Aliases serve inbox where?       | Same user mailbox                        | Same Apple ID mailbox                  | Same Proton mailbox                    | Same Outlook mailbox                  | Forward to *another* provider’s mailbox                |
| Shared/group email (e.g., support@) | First‑class groups, shared mailboxes   | No true groups; manual forwarding      | No multi‑user group inbox              | No consumer distribution list         | Can create `support@` → single destination mailbox     |
| One address → multiple recipients | Yes (groups / distribution lists)       | Not natively                           | No                                     | Not in consumer tier                  | One rule = one destination; fan‑out requires tricks    |
| Catch‑all                         | Supported                                | No                                     | Supported                              | No                                   | Supported (catch‑all can forward anywhere)             |

**Cloudflare difference:**  
Cloudflare can easily create many addresses and a catch‑all, but **each routing rule forwards to one destination mailbox**. A given `support@domain.com` rule goes to a single inbox, not multiple users directly. If you want fan‑out, you chain Cloudflare into another system (e.g., a list at your final provider, or use Workers for custom logic).

---

## 3. Hosting vs forwarding in practical terms

### 3.1 What “hosting” means (Google, Apple, Proton, Microsoft)

For **Google Workspace, Apple iCloud+, Proton Family, Microsoft 365 Family**:

- They host:
  - Mailboxes (inboxes, sent mail, etc.)
  - IMAP/POP/SMTP or similar protocols
  - Storage and indexing, search, spam filtering
- You log in directly to them to read and send mail.

### 3.2 What “forwarding” means (Cloudflare Email Routing)

For **Cloudflare Email Routing**:

- Cloudflare:
  - Receives mail for your domain (MX records point to Cloudflare).
  - Does light processing and authentication checks.
  - Immediately forwards mail to another mailbox you own (e.g., `you@gmail.com`).
  - Does not provide:
    - A mailbox UI,
    - Long‑term storage,
    - Native ability to send mail as that address.

To **send** mail as `you@yourdomain.com` when using Cloudflare:

- You configure your final mail provider (Gmail/Outlook/Proton via SMTP, etc.) to send mail with that From address.
- Cloudflare is invisible in the outbound path; it only affects inbound mail.

---

## 4. Cloud app ecosystems and integration

| Category                | Google Workspace                           | Apple iCloud+ / One                       | Proton Family                             | Microsoft 365 Family                     | Cloudflare Email Routing                    |
|-------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|----------------------------------------------|
| Email client            | Gmail web + apps, IMAP/POP                 | Mail apps + iCloud.com                     | Proton web/app + Bridge                    | Outlook desktop/web/mobile                 | None (uses your target provider’s client)    |
| Documents/Office        | Docs, Sheets, Slides                       | Pages, Numbers, Keynote                    | None (use external editors)                | Word, Excel, PowerPoint, OneNote           | None                                        |
| Storage                 | Google Drive                               | iCloud Drive                               | Proton Drive (encrypted)                   | OneDrive (1 TB/user)                       | None                                        |
| Calendar                | Google Calendar                            | Apple Calendar                             | Proton Calendar                            | Outlook Calendar                           | None                                        |
| Extra privacy tools     | Admin + security tools                     | Private Relay (limited), Hide My Email     | Encrypted Calendar/Drive, VPN, Pass        | Defender, Family Safety                    | Email security/analytics via routing rules   |

Cloudflare fits as a useful **front‑door** in front of whichever hosted mailbox solution you choose, rather than competing with them directly.

---

## 5. Spam filtering, rules, and quality

| Aspect                    | Google Workspace                           | Apple iCloud+                          | Proton Family                             | Microsoft 365 Family                     | Cloudflare Email Routing                           |
|---------------------------|--------------------------------------------|----------------------------------------|--------------------------------------------|--------------------------------------------|-----------------------------------------------------|
| Spam filtering strength   | Industry‑leading ML filtering              | Good consumer filtering                 | Good, sometimes strict                     | Enterprise‑grade [Exchange](https://en.wikipedia.org/wiki/Microsoft_Exchange_Server) backend         | Light filtering & auth checks; major filtering is at destination mailbox |
| Rules / filters           | Powerful filters + labels                  | Basic rules                             | Powerful filtering & labels                | Rich Outlook rules                         | Routing rules; advanced scripting via Workers       |
| Abuse protections         | Mature anti‑abuse stack                    | Good enough for consumers               | Strong, privacy‑centric                    | Enterprise‑grade protections               | [SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework)/[DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)/DMARC‑aware forwarding and SRS rewriting   |

Cloudflare’s main contribution is **properly forwarding authenticated mail** (SPF, DKIM, DMARC) without breaking deliverability, not spam scoring. The downstream mailbox still does the heavy spam work.

---

## 6. IPv6 and standards

| Network / Standard        | Google Workspace                 | Apple iCloud Mail               | Proton Mail / Family               | Microsoft 365 Family              | Cloudflare Email Routing                                      |
|---------------------------|----------------------------------|---------------------------------|------------------------------------|-----------------------------------|----------------------------------------------------------------|
| IPv6 on MX (inbound mail) | **Yes** (dual‑stack)            | **Yes** (dual‑stack)           | **No** (IPv4‑only MX)              | **Yes** (dual‑stack)             | **Yes**: Cloudflare MX supports IPv6 for inbound              |
| Forwarding over IPv6      | Will connect to upstream via IPv6 if destination MX has AAAA| Will connect to upstream via IPv6 if destination MX has AAAA| N/A                                |Will connect to upstream via IPv6 if destination MX has AAAA| Will connect to upstream via IPv6 if destination MX has AAAA  |
| [SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework)/[DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)/DMARC            | Fully supported                 | Supported, mostly automatic     | Fully supported                    | Fully supported                  | Preserves auth; uses SRS for envelope sender rewriting        |
| DNS control               | You manage domain DNS            | Limited to Apple’s UI           | You manage domain DNS              | Full in business; fixed in consumer | Cloudflare manages DNS if domain is on Cloudflare             |

Key points:

- **Cloudflare Email Routing**:
  - Provides IPv6‑capable MX endpoints.
  - Forwards mail using IPv6 when the *destination* provider supports it; falls back to IPv4 otherwise.
- **Proton Mail**:
  - As of now, Proton’s MX records are **IPv4‑only**, so mail directly to Proton requires IPv4 connectivity.
  - This limitation disappears if you place Cloudflare in front, since Cloudflare terminates on IPv4 and can still be dual‑stack at the outer edge. However, the web front ends are also IPv4-only, so Proton is functionally a single stacked solution as if now. They have slowly been rolling IPv6 out for things like VPN, so I do expect it "some day". 

---

## 7. Costs and typical usage patterns

| Service                | Plan type                 | Approx yearly cost (US) | Users           | Storage headline                   | Notes                          |
|------------------------|---------------------------|--------------------------|-----------------|------------------------------------|---------------------------------|
| Google Workspace       | Business Starter          | ~$72/user/year          | Per user        | 30 GB/user (more in higher tiers)  | Business product used by families |
| Apple iCloud+ Family   | 200 GB–2 TB tiers         | ~$36–$120/year total    | Up to 6         | 200 GB–2 TB shared iCloud          | Includes mail + Photos + Drive |
| Proton Family          | Family bundle             | ~$240–$360/year total   | ~6              | Hundreds of GB–few TB encrypted    | Includes VPN + Pass            |
| Microsoft 365 Family   | Family plan               | ~$100/year total        | Up to 6         | 1 TB OneDrive per user (6 TB total) | Includes Office apps           |
| Cloudflare Email Routing | Included with Cloudflare | Typically free for routing | Per domain    | None (no mailbox storage)         | You must still pay for a mailbox provider |

Cloudflare Email Routing effectively reduces cost by letting you:

- Use a free/cheap mailbox (Gmail, Outlook.com, etc.).
- Put your **custom domain branding** in front via Cloudflare.
- Avoid paying for separate hosted mail per domain when all you need is forwarding.

---

## 8. Choosing where Cloudflare fits in

Practical patterns:

- **Forwarding into Gmail/Outlook/Proton:**  
  Use Cloudflare MX for your domain, route `name@domain.com` to a Gmail/Outlook/Proton mailbox. You manage spam and sending from that provider; Cloudflare only routes.

- **Alias and catch‑all front‑end:**  
  Use Cloudflare to generate many aliases or a catch‑all, all forwarding into one or a few real mailboxes. This keeps your main mailbox provider simple and cheap.

- **Not a replacement for a real host:**  
  Cloudflare does not replace Google Workspace, Proton, or Microsoft 365. You still need one of them (or some other host) for:

  - Mailbox storage
  - Search
  - Calendars/contacts
  - Sending mail

---

## 9. Quick “best use” summary including Cloudflare

- **Google Workspace** – Best when you want *full* business‑grade email hosting, collaboration, and admin for a family or small group.
- **Apple iCloud+** – Best for an all‑Apple household that wants simple, integrated mail and storage.
- **Proton Family** – Best for families that value privacy, encryption, and Swiss jurisdiction over convenience and integrations.
- **Microsoft 365 Family** – Best for families wanting Office apps plus large personal storage (1 TB per user) with solid consumer email.
- **Cloudflare Email Routing** – Best as a **free, DNS‑level front door** to give your domain professional emails that forward into an existing mailbox; useful when you want:

  - Custom domain addresses,
  - No separate mail server,
  - And are happy to keep a Gmail/Outlook/Proton mailbox behind it.

---



For me, google is still the clear winner, but it does come with the large pill of "if the product is free, you're the product". A very close second is Proton, which I still may completely move to.

_Last updated: December 26th, 2025._
