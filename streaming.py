#!./venv/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import platform
if platform.system()=='Windows':
    from pick import pick
else:
    from simple_term_menu import TerminalMenu



class Torrent:
    
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
            } 
        self.menu = " "
        self.platform = platform.system()


    def parser(self,r):
        t =   r.json() if r.status_code==200 else None
        if(t!=None  ):
            i=1
            selected = 0
            options =[]
            while i<len(t): 
                size = float("{:.2f}".format(float(t[i]['size'])/1000000000.0))
                if int(t[i]['seeders'])>10:
                    options.append(f" {t[i]['name']}  [{size}GB]")
                i+=1
            if len(options)==0:
                print("Sorry no results found......")
            options.append("Exit") 
            options.append("Search Again")
            
            menu_entry_index = self.display_menu(options) 

            if(options[menu_entry_index]=="Exit"):
                exit()
            elif(options[menu_entry_index]=="Search Again"):
                self.seach_stream()
            else:
                self.stream(menu_entry_index,t)
                


        else:
            print("Sorry Cannot find what you are searching for :(")
    
    def display_menu(self,options):
        if self.platform == 'Windows':
            option, menu_entry_index = pick(options, self.menu,indicator='>>')
        else:
            terminal_menu = TerminalMenu(options,title=self.menu,clear_screen=True,menu_highlight_style=("bg_red", "fg_yellow")) 
            menu_entry_index = terminal_menu.show()
        return menu_entry_index
    
    def top_parser(self,r,start,end):
        
        status = r.status_code
        t =   r.json() if status==200 else None
        if(t!=None):
            i=start

            options =[]
            while i<end:
                
                size = float("{:.2f}".format(float(t[i]['size'])/1000000000.0))
                options.append(f"{i+1}. {t[i]['name']}  [{size}GB]")
                i+=1
            if(start>=10):
                options.append('Go to Last Page')
            if(end<100):
                options.append("Go to Next Page") 
            options.append("Exit") 
            menu_entry_index = self.display_menu(options) 
            if(options[menu_entry_index]=="Go to Next Page"):
                self.top_parser(r,end,end+10)
            elif(options[menu_entry_index]=="Go to Last Page"):
                self.top_parser(r,start-10,start)
            elif(options[menu_entry_index]=="Exit"):
                exit()
            else:
                self.stream(menu_entry_index+start,t)
    
    
    def stream(self,select,t):
        options = ["Stream","Download","Exit"]
        menu_entry_index = self.display_menu(options)
        
        if menu_entry_index==0:
            print("Playing {}......".format(t[select]['name']) )
            com = 'webtorrent --mpv --quiet ' + t[select]['info_hash']
            os.system(com) 
        elif menu_entry_index==1:
            print("Downloading {}......".format(t[select]['name']) )
            com = 'webtorrent ' + t[select]['info_hash'] 
            os.system(com)
        else:
            exit()
        
    def seach_stream(self):
        Movie = input("What would you like to watch today? ")
        paylode = {'q':Movie}
        r = requests.get('https://apibay.org/q.php',params=paylode,headers=self.headers)
        self.menu = "Search Results for {}".format(Movie)
        self.parser(r)

    def top_movies(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_201.json',headers=self.headers)
        self.top_parser(response,0,10)
        
    def top_series(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_205.json',headers=self.headers)
        self.top_parser(response,0,10)
        
    def top_movies_HD(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_207.json',headers=self.headers)
        self.top_parser(response,0,10)    
        
    def top_audiobooks(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_102.json',headers=self.headers)
        self.top_parser(response,0,10)
                
      
            
        


