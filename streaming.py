#!./venv/bin/python

import platform
import requests
import os
from os import path


if(platform.system()=='Windows' and not path.exists("req.txt")):
    try:
        os.system('iwr -useb get.scoop.sh | iex')
    except:
        os.system('Set-ExecutionPolicy RemoteSigned -scope CurrentUser')
        os.system('iwr -useb get.scoop.sh | iex')   
    os.system('scoop install curl')
    os.system('scoop install aria2') 
    os.system('scoop install nodejs')
    os.system('scoop install vlc')
    os.system('npm i webtorrent-cli')
    with open('req.txt', 'w') as f:
        f.write('met')
if(platform.system()=='Darwin' and not path.exists("req.txt")) :
    with open('req.txt', 'w') as f:
        f.write('met') 
    os.system('cd ~')
    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system('brew install iina')
    os.system('brew install npm')
    os.system('npm i webtorrent-cli -g')
    
    
    
    

Movie = input("What would you like to watch today? ")
paylode = {'q':Movie}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
r = requests.get('https://apibay.org/q.php',params=paylode,headers=headers)
status = r.status_code
t =   r.json() if status==200 else None
if(t!=None ):
    i=1
    selected = 0
    for search in t:
        if( int(search['seeders']) > 20):
            print('[{}] {} ({})'.format(i,search['name'],search['seeders']))
            i=i+1
    
    while True:
        selected = input("\nEnter Number to select : ")
        if(selected.isnumeric):
            if( int(selected)<i):
                break
        print("Please Enter Correct value")
        
    select = int(selected) -1
    print("Playing {}......".format(t[select]['name']) )
    com = 'webtorrent --iina ' + t[select]['info_hash'] if platform.system()=='Darwin' else 'webtorrent --vlc ' + t[select]['info_hash'] 
    os.system(com)
else:
    
    print("Sorry Cannot find what you are searching for :(")    
      
            
        


