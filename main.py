#!/usr/bin/env python3

from pathlib import Path
import pycparser
import pycparser_fake_libc
import subprocess

def parse(source, output=None):
    source = Path(source)
    if output is None:
        output = source.stem
    cmd = f"gcc -E -std=c99 -I{pycparser_fake_libc.directory} {source} -o {output}"
    subprocess.run(cmd, shell=True)
    return pycparser.parse_file(output)

if __name__ == "__main__":
    ast = parse("main.c")