#!/usr/bin/env sh

chmod +x src/main.py
pip3 install -r requirements.txt;
sudo mv ../miomi /usr/local/bin/
sudo ln -sf /usr/local/bin/miomi/main.py /usr/bin/miomi
