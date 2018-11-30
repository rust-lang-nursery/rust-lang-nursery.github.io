#!/usr/bin/env python3
"""
Generates redirects for rust-clippy, based on versions.json.
The rust-clippy repo must be on the gh-pages branch at ../rust-clippy.
"""

from pathlib import Path
import json

TEMPLATE = """
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to https://rust-lang.github.io/rust-clippy/{version}</title>
<link rel="canonical" href="https://rust-lang.github.io/rust-clippy/{version}/">
<noscript>
<meta http-equiv="refresh" content="0; URL=https://rust-lang.github.io/rust-clippy/{version}/">
</noscript>
<script>
window.location.replace("https://rust-lang.github.io/rust-clippy/{version}/" + window.location.hash)
</script>
"""

CLIPPY_REDIRECTS = Path('./rust-clippy')
CLIPPY_REPO = Path('../rust-clippy')

with (CLIPPY_REPO / 'versions.json').open() as versions:
    for version in json.load(versions):
        version_dir = CLIPPY_REDIRECTS / version
        version_file = version_dir / 'index.html'

        version_dir.mkdir(parents=True, exist_ok=True)
        with version_file.open('wt') as redirect:
            redirect.write(TEMPLATE.format(version=version))

        print("Wrote", version_file)
