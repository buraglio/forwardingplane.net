#!/usr/bin/env python3
"""
Blog Post Cleanup Script
Fixes HTML entities, double spaces, removes blogger metadata, converts HTML to markdown,
removes WordPress footers, and detects broken links.
"""

import glob
import re
import os
import argparse
from pathlib import Path
from collections import defaultdict

# HTML entity replacements
HTML_ENTITIES = {
    '&#8230;': '…',
    '&#8217;': "'",
    '&#8220;': '"',
    '&#8221;': '"',
    '&#8211;': '–',
    '&#8212;': '—',
    '&#038;': '&',
    '&#039;': "'",
    '&#091;': '[',
    '&#093;': ']',
    '&#91;': '[',
    '&#93;': ']',
    '&amp;': '&',
    '&nbsp;': ' ',
    '&rsquo;': "'",
    '&lsquo;': "'",
    '&rdquo;': '"',
    '&ldquo;': '"',
    '&mdash;': '—',
    '&ndash;': '–',
    '&quot;': '"',
    '&lt;': '<',
    '&gt;': '>',
}

# Blogger metadata fields to remove
BLOGGER_FIELDS = [
    'blogger_blog',
    'blogger_author',
    'blogger_permalink',
    'blogger_internal'
]

# WordPress/Blogger footer patterns to remove
FOOTER_PATTERNS = [
    r'\[\[ This is a content summary only\. Visit my website for full links, other content, and more! \]\]',
    r'\[This is a content summary only\. Visit my website for full links, other content, and more!\]',
]

def fix_html_entities(content):
    """Replace HTML entities with proper UTF-8 characters"""
    for entity, char in HTML_ENTITIES.items():
        content = content.replace(entity, char)

    # Handle numeric entities like &#123;
    content = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), content)

    return content

def convert_html_to_markdown(content):
    """Convert common HTML tags to markdown equivalents"""

    # Store frontmatter to preserve it
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        body = content[len(frontmatter):]
    else:
        frontmatter = ''
        body = content

    # Convert headers (h1-h6) to markdown
    body = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', body, flags=re.DOTALL)
    body = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', body, flags=re.DOTALL)
    body = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', body, flags=re.DOTALL)
    body = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', body, flags=re.DOTALL)
    body = re.sub(r'<h5[^>]*>(.*?)</h5>', r'\n##### \1\n', body, flags=re.DOTALL)
    body = re.sub(r'<h6[^>]*>(.*?)</h6>', r'\n###### \1\n', body, flags=re.DOTALL)

    # Convert bold and italic
    body = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', body, flags=re.DOTALL)
    body = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', body, flags=re.DOTALL)
    body = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', body, flags=re.DOTALL)
    body = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', body, flags=re.DOTALL)

    # Convert code blocks with pre tags
    body = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', body, flags=re.DOTALL)
    body = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', body, flags=re.DOTALL)

    # Convert inline code
    body = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', body, flags=re.DOTALL)

    # Convert links (but preserve images inside links)
    body = re.sub(r'<a\s+href=["\'](.*?)["\'][^>]*>(.*?)</a>', r'[\2](\1)', body, flags=re.DOTALL)

    # Convert images to markdown (handle both with and without quotes)
    body = re.sub(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*/?>', r'![\2](\1)', body)
    body = re.sub(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*/?>', r'![](\1)', body)

    # Convert unordered lists
    body = re.sub(r'<ul[^>]*>', '\n', body)
    body = re.sub(r'</ul>', '\n', body)
    body = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', body, flags=re.DOTALL)

    # Convert ordered lists
    body = re.sub(r'<ol[^>]*>', '\n', body)
    body = re.sub(r'</ol>', '\n', body)

    # Convert blockquotes
    body = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n> ' + m.group(1).replace('\n', '\n> ') + '\n', body, flags=re.DOTALL)

    # Remove div, span, p tags (keep content)
    body = re.sub(r'</?div[^>]*>', '', body)
    body = re.sub(r'</?span[^>]*>', '', body)
    body = re.sub(r'<p[^>]*>', '\n', body)
    body = re.sub(r'</p>', '\n', body)

    # Convert <br> and <br /> to line breaks
    body = re.sub(r'<br\s*/?>', '\n', body)

    # Remove any remaining HTML tags (but warn about them)
    remaining_tags = re.findall(r'<[^>]+>', body)
    if remaining_tags:
        # Keep some common ones that might be intentional (like in code examples)
        pass

    # Clean up any malformed EOF/heredoc HTML
    body = re.sub(r'<eof[^>]*>.*?</eof>', '', body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<eof[^>]*>', '', body, flags=re.IGNORECASE)

    return frontmatter + body

def remove_wordpress_footer(content):
    """Remove WordPress/Blogger syndication footers"""
    for pattern in FOOTER_PATTERNS:
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
    return content

def fix_double_spaces(content):
    """Replace multiple consecutive spaces with single space"""
    lines = content.split('\n')
    fixed_lines = []
    for line in lines:
        # Don't touch leading whitespace, only fix spaces in content
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        fixed_content = re.sub(r'  +', ' ', stripped)
        fixed_lines.append(indent + fixed_content)
    return '\n'.join(fixed_lines)

def remove_excessive_blank_lines(content):
    """Replace more than 2 consecutive blank lines with 2"""
    return re.sub(r'\n{4,}', '\n\n\n', content)

def remove_blogger_metadata(content):
    """Remove blogger-specific frontmatter fields"""
    lines = content.split('\n')
    result_lines = []
    in_frontmatter = False
    skip_next_indent = False

    for i, line in enumerate(lines):
        # Detect frontmatter boundaries
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result_lines.append(line)
            continue

        # Check if we should skip this line
        if in_frontmatter:
            # Check if this line starts with a blogger field
            is_blogger_field = any(line.strip().startswith(f'{field}:') for field in BLOGGER_FIELDS)

            # Check if this is an indented continuation of a blogger field
            if skip_next_indent and line.startswith('  ') and line.strip().startswith('-'):
                continue  # Skip indented list items under blogger fields

            skip_next_indent = is_blogger_field

            if not is_blogger_field:
                result_lines.append(line)
        else:
            result_lines.append(line)
            skip_next_indent = False

    return '\n'.join(result_lines)

def detect_broken_links(content, filepath):
    """Detect potentially broken links and return list of issues"""
    issues = []

    # Find markdown links with empty or suspicious URLs
    empty_links = re.findall(r'\[([^\]]+)\]\(\s*\)', content)
    if empty_links:
        issues.append(f"Empty link URLs: {empty_links}")

    # Find links with localhost or relative WordPress paths
    wp_links = re.findall(r'\[([^\]]+)\]\(((?:http://)?(?:www\.)?forwardingplane\.net/wp-content/[^\)]+)\)', content)
    if wp_links:
        issues.append(f"WordPress media links (may be broken): {[link[1] for link in wp_links]}")

    # Find malformed image tags
    malformed_imgs = re.findall(r'!\[[^\]]*\]\([^)]*(?:wp-image-|alignleft|alignright|aligncenter)[^)]*\)', content)
    if malformed_imgs:
        issues.append(f"Images with WordPress CSS classes: {malformed_imgs}")

    # Find HTML img tags that weren't converted
    html_imgs = re.findall(r'<img[^>]*>', content)
    if html_imgs:
        issues.append(f"Unconverted HTML img tags: {len(html_imgs)} found")

    # Find HTML anchor tags that weren't converted
    html_links = re.findall(r'<a\s+href=[^>]*>.*?</a>', content)
    if html_links:
        issues.append(f"Unconverted HTML anchor tags: {len(html_links)} found")

    return issues

def process_file(filepath, dry_run=False, report_only=False):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        issues = detect_broken_links(content, filepath)

        if report_only:
            return (False, issues)

        # Apply fixes
        content = fix_html_entities(content)
        content = convert_html_to_markdown(content)
        content = remove_wordpress_footer(content)
        content = fix_double_spaces(content)
        content = remove_excessive_blank_lines(content)
        content = remove_blogger_metadata(content)

        # Only write if changes were made
        if content != original_content:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
            return (True, issues)
        return (False, issues)
    except Exception as e:
        return (False, [f"Error processing file: {e}"])

def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Clean up blog posts from WordPress/Blogger conversion')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    parser.add_argument('--report', action='store_true', help='Only report issues, do not fix anything')
    parser.add_argument('--path', type=str, default='/Users/buraglio/Documents/Dev/forwardingplane.net/content/post',
                        help='Path to posts directory')
    args = parser.parse_args()

    post_dir = Path(args.path)

    if not post_dir.exists():
        print(f"Error: Directory not found: {post_dir}")
        return

    # Get all markdown files
    markdown_files = sorted(list(post_dir.glob('*.md')))
    total_files = len(markdown_files)
    modified_files = 0
    files_with_issues = defaultdict(list)

    mode_str = "REPORT ONLY" if args.report else ("DRY RUN" if args.dry_run else "LIVE MODE")
    print(f"\n{'='*70}")
    print(f"Blog Post Cleanup Tool - {mode_str}")
    print(f"{'='*70}")
    print(f"Processing {total_files} markdown files from: {post_dir}")
    print(f"{'-'*70}\n")

    for i, filepath in enumerate(markdown_files, 1):
        was_modified, issues = process_file(filepath, dry_run=args.dry_run, report_only=args.report)

        if was_modified:
            modified_files += 1
            if args.dry_run:
                print(f"Would modify: {filepath.name}")

        if issues:
            files_with_issues[str(filepath)] = issues

        # Progress indicator
        if i % 50 == 0:
            print(f"Processed {i}/{total_files} files...")

    print(f"\n{'-'*70}")
    print(f"Complete!")
    print(f"{'-'*70}")
    print(f"Total files processed: {total_files}")

    if not args.report:
        if args.dry_run:
            print(f"Files that would be modified: {modified_files}")
        else:
            print(f"Files modified: {modified_files}")
        print(f"Files unchanged: {total_files - modified_files}")

    if files_with_issues:
        print(f"\n{'-'*70}")
        print(f"Files with potential issues: {len(files_with_issues)}")
        print(f"{'-'*70}\n")

        for filepath, issues in sorted(files_with_issues.items()):
            print(f"\n{Path(filepath).name}:")
            for issue in issues:
                print(f"  - {issue}")

    print(f"\n{'='*70}\n")

if __name__ == '__main__':
    main()
