######################################################
#                                                    #
#       PHISHME ALPHA 1                              #
#                                                    #
# by:     ANIR0Y                                     #
#                                                    #
# Telegram Group: https://t.me/anir0y                #
# YouTube Channel: https://youtube.com/c/arishtilive #
# Twitter: https://twitter.com/anir0y                #
#                                                    #
######################################################

from wget import download
from os import path, remove, system
from platform import system as systemos, architecture
from subprocess import check_output
from urllib.request import urlopen
from core.view import *
from zipfile import ZipFile
from subprocess import check_output

def connected(host='https://anir0y.in'):
    try:
        urlopen(host)
        return True
    except:
        return False

def unzip(source_filename, dest_dir):
    with ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def checkNgrok():
    if path.isfile('base/Server/ngrok') == False: 
        ngrokNot()
        if 'Android' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/bNyj1mQVY4c/' + filename
        # https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz # latest version
        download(url)
        unzip(filename, 'base/Server/')
        remove(filename)
        system('chmod +x base/Server/ngrok')
        clear()

def checkPHP():
    if 256 != check_output(['which', 'php']):
        return True        
    else:
        return False
 
def pre():
    checkNgrok()
    if connected() == False:
        conNot()       
    if checkPHP() == False:
        phpNot()
