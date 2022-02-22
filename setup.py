import os
from os import path
import platform


def setup():
    os.system("pip install requests")
    if(platform.system()=='Windows' and not path.exists("req.txt")):
        try:
            os.system('iwr -useb get.scoop.sh | iex')
        except:
            os.system('Set-ExecutionPolicy RemoteSigned -scope CurrentUser')
            os.system('iwr -useb get.scoop.sh | iex')   
        os.system('scoop install curl')
        os.system('scoop install aria2') 
        os.system('scoop install nodejs')
        os.system('scoop install mpv')
        os.system('npm i webtorrent-cli')

            
    if(platform.system()=='Darwin' and not path.exists("req.txt")) :
        os.system('cd ~')
        os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system('brew install mpv')
        os.system('brew install npm')
        os.system('npm i webtorrent-cli -g')
    
    os.system('pip install -r requirement.txt')
    with open('req.txt', 'w') as f:
        f.write('met') 
    

    
setup()
