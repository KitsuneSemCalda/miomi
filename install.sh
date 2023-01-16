#!/usr/bin/env sh

sudo rm -rf /usr/local/bin/miomi/
chmod +x src/main.py
pip3 install -r requirements.txt;
sudo mv ../miomi /usr/local/bin/
sudo ln -sf /usr/local/bin/miomi/src/main.py /usr/bin/miomi
