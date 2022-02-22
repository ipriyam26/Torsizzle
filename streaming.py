#!./venv/bin/python
# -*- coding: utf-8 -*-

import requests
import os
from simple_term_menu import TerminalMenu



class Torrent:
    
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
            } 

    def parser(self,r,menu):
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
            terminal_menu = TerminalMenu(options,title=menu,clear_screen=True,menu_highlight_style=("bg_red", "fg_yellow")) 
            menu_entry_index = terminal_menu.show()
            # print(menu_entry_index)

            if(options[menu_entry_index]=="Exit"):
                exit()
            elif(options[menu_entry_index]=="Search Again"):
                self.seach_stream()
            else:
                self.stream(menu_entry_index,t)
                


        else:
            print("Sorry Cannot find what you are searching for :(")
    
    
    def top_parser(self,r,start,end,menu):
        
        status = r.status_code
        t =   r.json() if status==200 else None
        if(t!=None):
            i=start

            options =[]
            while i<end:
                
                size = float("{:.2f}".format(float(t[i]['size'])/1000000000.0))
                options.append(f" {t[i]['name']}  [{size}GB]")
                i+=1
            if(start>=10):
                options.append('Go to Last Page')
            if(end<100):
                options.append("Go to Next Page") 
            options.append("Exit") 
            terminal_menu = TerminalMenu(options,title=menu,clear_screen=True,menu_highlight_style=("bg_red", "fg_yellow")) 
            menu_entry_index = terminal_menu.show()
            # print(menu_entry_index)
            
            
            if(options[menu_entry_index]=="Go to Next Page"):
                self.top_parser(r,end,end+10,menu)
            elif(options[menu_entry_index]=="Go to Last Page"):
                # print(f"start = {start-10} end = {start}")
                self.top_parser(r,start-10,start,menu)
            elif(options[menu_entry_index]=="Exit"):
                exit()
            else:
                self.stream(menu_entry_index+start,t)
            

            
    
    
    def stream(self,select,t):
        options = ["Stream","Download","Exit"]
        terminal_menu = TerminalMenu(options,title=f"{t[select]['name']}",clear_screen=True,menu_highlight_style=("bg_red", "fg_yellow"))
        selected = terminal_menu.show()
        if selected==0:
            print("Playing {}......".format(t[select]['name']) )
            com = 'webtorrent --mpv --quiet ' + t[select]['info_hash']
            os.system(com) 
        elif selected==1:
            print("Downloading {}......".format(t[select]['name']) )
            com = 'webtorrent ' + t[select]['info_hash'] 
            os.system(com)
        else:
            exit()
               

        
        

            
        
    def seach_stream(self):
        Movie = input("What would you like to watch today? ")
        paylode = {'q':Movie}
        r = requests.get('https://apibay.org/q.php',params=paylode,headers=self.headers)
        self.parser(r,menu=Movie)



    def top_movies(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_201.json',headers=self.headers)
        self.top_parser(response,0,10,menu="Top 100 Movies")
        
    def top_series(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_205.json',headers=self.headers)
        self.top_parser(response,0,10,menu="Top 100 Series")
        
    def top_movies_HD(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_207.json',headers=self.headers)
        self.top_parser(response,0,10,menu="Top 100 Movies HD")    
        
    def top_audiobooks(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_102.json',headers=self.headers)
        self.top_parser(response,0,10,menu="Top 100 Audiobooks")
                
      
            
        


