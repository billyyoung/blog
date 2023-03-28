#!/bin/bash

# to run a local server see notes.txt, or:
# hugo server --buildDrafts --buildFuture

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
hugo -t ezhil # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd public
# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
    then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push

# Come Back up to the Project Root
cd ..
