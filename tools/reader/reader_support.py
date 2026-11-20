"""Shared publishing rules: keep personal notes and archives out of the reader."""
import re

def excluded(path):
    for part in path.parts:
        key = re.sub(r'[^a-z0-9]', '', part.lower())
        if part.startswith('.') or part.endswith('.dSYM') or key in {'mynotes', 'notes', 'brokenfiles','90personalnotes','98archive','99buildartifacts','tools'} or 'backup' in key:
            return True
    return False

def article_number(path):
    parts = path.parts
    chapter = re.match(r'^(\d+)[_. -]', parts[0])
    item = re.match(r'^(\d+)[_. -]', path.stem)
    if chapter and item and len(parts)>1:
        return chapter[1]+'.'+item[1]
    return item[1] if item else ''

def publish_markdown(raw):
    # Add code emphasis to known commands in labelled prose, without touching fences.
    lines=[]; fence=False
    for line in raw.splitlines():
        if re.match(r'^\s*(```|~~~)',line): fence=not fence
        if not fence and re.match(r'^\*\*(LEARN|LAB|EVIDENCE|INTERVIEW|INTERNAL / LATENCY)',line) and '`' not in line:
            line=re.sub(r'\b(SO_RCVBUF|IP_ADD_MEMBERSHIP|EAGAIN|ss|sar|ethtool|tcpdump|sendmsg|recvmsg|bind|connect|listen|accept|send|recv|memoryview|struct)\b',r'`\1`',line)
        lines.append(line)
    return '\n'.join(lines)+'\n'
