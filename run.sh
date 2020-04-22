#!/bin/sh
rm output.png 2> /dev/null
pipenv run python src/news365.py
feh output.png
