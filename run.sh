#!/bin/bash

rm -rf styles && git clone --depth 1 --branch master https://github.com/citation-style-language/styles styles

python process_styles.py