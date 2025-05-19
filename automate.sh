#!/bin/bash

git status

git add .

git commit -m "Control 3 (pypackage) commit: $(date +%Y-%m-%d)"

git push

echo Files successfully pushed to Remote Repository

