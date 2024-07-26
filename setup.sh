#!/bin/bash

echo "Installing dependencies..."
pip3 install requirements.txt --break-system-packages
echo "done"

echo "Copying files..."
cp -R home_folder/* ~/
cp -R appsupport/* '~/Library/Application Support/'
echo "done"

echo "Finished installing. To use, close this terminal window and start up a fresh one or type 'cd ~' first. Then, type 'python3 auratext.py' once in your home folder."