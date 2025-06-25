#!/usr/bin/bash

echo '===== setup tsinghua pip repo ====='
sudo apt install -y python3-pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

echo '===== install pip dependencies ====='
pip install .

# copy file to /opt/EmotiVoice
echo '===== install zhttsServer.py ====='
sudo cp zhttsServer.py /usr/bin/zhttsServer.py
