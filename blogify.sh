#!/bin/bash

# Go from bp ipynb to files in cm.gh.com repo

jupyter nbconvert --to 'markdown' --TemplateExporter.exclude_input=True writeup.ipynb
sed -E -f iframe.sed writeup.md | cat bp_frontmatter.txt - > index.md
rm writeup.md
mv index.md ../colinmorris.github.com/_posts/2017-10-30-size-of-things.md
mv writeup_files/* ../colinmorris.github.com/assets/sizeof/
cp *.png *.jpg ../colinmorris.github.com/assets/sizeof/

