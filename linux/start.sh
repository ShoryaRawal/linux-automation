#!/bin/sh

echo "Starting script..."
sudo chmod a+w sh &&
chmod u+x sh/make-f.sh &&
chmod u+x sh/make-b.sh &&
chmod u+x sh/make-rs.sh &&
chmod a+wx sh/dir.sh

sudo apt-get install python3
sudo apt-get install python3-nltk

python3 .app.py
