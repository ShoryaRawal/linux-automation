#!/bin/sh

echo "starting script..."
sudo chmod a+w sh &&
chmod u+x sh/make-f.sh &&
chmod u+x sh/make-b.sh &&
chmod u+x sh/make-rs.sh &&
chmod a+wx sh/dir.sh

python3 .app.py
