#!/bin/bash
echo Sit and relax, let me do the installation
echo installing PHP...
sleep 1
sudo apt install php -y
clear 
echo installaing PIP3
sleep 1
sudo apt install -y python3-pip 
clear
pip3 --version
sleep 1 
clear 
echo Python package installing... 
sudo pip3 install -r requirements.txt 
echo done!!
sleep 1
clear 
python3 phishme.py

