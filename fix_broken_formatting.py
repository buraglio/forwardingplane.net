#!/usr/bin/env python3
"""Fix broken formatting from Perl script"""

import re
from pathlib import Path

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix pattern: "text *\n\n*text**" -> "text **text**"
    content = re.sub(r'(\w+)\s+\*\s*\n\s*\n\s*\*(\w+)\s+\*\*', r'\1 **\2**', content)

    # Fix pattern: "text *\n\n*text**\n" -> "text **text**\n"
    content = re.sub(r'(\w+)\s+\*\n\n\*(\w+)\*\*\n', r'\1 **\2**\n', content)

    # Fix standalone ** ** patterns
    content = re.sub(r'\*\* \*\*', '', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Fix the specific problematic files
files = [
    '2012-11-06-juniper-ex-4200-arp-ndp-problem-or-things-id-like-to-see-in-a-tac.md',
    '2010-09-02-updating-srx-idp-signatures.md',
    '2010-10-13-android-nexus-one-or-iphone.md',
    '2011-02-07-upgrading-a-new-srx-3600.md',
    '2011-02-18-sync-catalogs-iphoto-itunes-on-a-mac.md',
    '2011-07-30-macos-10-7-and-ipv6-privacy-addressing.md',
    '2011-10-22-a-security-oversight-in-mail-app-or-a-hidden-bcc-field.md',
    '2012-04-27-nsr-and-issu-on-juniper-mx-series-with-logical-routers.md',
    '2012-10-18-a-tale-of-two-isps.md',
    '2012-10-19-microflow-policing-on-cisco-sup2t.md',
    '2012-10-27-host-based-sflow-or-sflow-for-more-than-just-network-traffic.md',
    '2012-11-09-scinet-a-privileged-few.md',
]

post_dir = Path('/Users/buraglio/Documents/Dev/forwardingplane.net/content/post')
fixed = 0

for filename in files:
    filepath = post_dir / filename
    if filepath.exists():
        if fix_file(filepath):
            print(f"Fixed: {filename}")
            fixed += 1

print(f"\nTotal files fixed: {fixed}")
