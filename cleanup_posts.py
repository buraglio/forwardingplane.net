#!/usr/bin/env python3
"""
Blog Post Cleanup Script
Fixes HTML entities, double spaces, and removes blogger metadata
"""

import glob
import re
import os
from pathlib import Path

# HTML entity replacements
HTML_ENTITIES = {
    '&#8230;': "",
    '&#8217;': "'",
    '&#8220;': '"',
    '&#8221;': '"',
    '&#8211;': '–',
    '&#8212;': '—',
    '&#038;': '&',
    '&amp;': '&',
    '&nbsp;': ' ',
    '&rsquo;': "'",
    '&lsquo;': "'",
    '&rdquo;': '"',
    '&ldquo;': '"',
    '&mdash;': '—',
    '&ndash;': '–',
}

# Blogger metadata fields to remove
BLOGGER_FIELDS = [
    'blogger_blog',
    'blogger_author',
    'blogger_permalink',
    'blogger_internal'
]

def fix_html_entities(content):
    """Replace HTML entities with proper UTF-8 characters"""
    for entity, char in HTML_ENTITIES.items():
        content = content.replace(entity, char)
    return content

def fix_double_spaces(content):
    """Replace multiple consecutive spaces with single space"""
    # Fix multiple spaces (but preserve indentation at line start)
    lines = content.split('\n')
    fixed_lines = []
    for line in lines:
        # Don't touch leading whitespace, only fix spaces in content
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        fixed_content = re.sub(r'  +', ' ', stripped)
        fixed_lines.append(indent + fixed_content)
    return '\n'.join(fixed_lines)

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

def process_file(filepath):
    """Process a single markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Apply fixes
        content = fix_html_entities(content)
        content = fix_double_spaces(content)
        content = remove_blogger_metadata(content)

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main execution function"""
    post_dir = Path('/Users/buraglio/Documents/Dev/forwardingplane.net/content/post')

    if not post_dir.exists():
        print(f"Error: Directory not found: {post_dir}")
        return

    # Get all markdown files
    markdown_files = list(post_dir.glob('*.md'))
    total_files = len(markdown_files)
    modified_files = 0

    print(f"Processing {total_files} markdown files...")
    print("-" * 60)

    for i, filepath in enumerate(markdown_files, 1):
        if process_file(filepath):
            modified_files += 1

        # Progress indicator
        if i % 50 == 0:
            print(f"Processed {i}/{total_files} files...")

    print("-" * 60)
    print(f"Complete!")
    print(f"Total files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print(f"Files unchanged: {total_files - modified_files}")

if __name__ == '__main__':
    main()
