#!/bin/bash

# Work out Path for Script
SCR_PATH=$(echo $0 | awk -F'[/]' '{$NF=""; print $0}' | tr " " "/")

cd ${SCR_PATH}

source bin/activate

python scraper.py
