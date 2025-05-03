#!/bin/bash

git status

git add .

git commit -m "Automated commit: $(date +%Y-%m-%d)"

git push

echo Files successfully pushed to Remote Repository

