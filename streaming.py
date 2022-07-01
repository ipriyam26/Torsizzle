#!./venv/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import platform


from pick import pick

    
from sources.one_three_three_x import OneThreeThreeX 
from sources.piratebay import Piratebay



class Torrent:
    
    def __init__(self):
        self.platform = platform.system()
        self.o33x = OneThreeThreeX()
        self.pirate = Piratebay()
    
    def display_menu(self,options:list,menu:str) -> int:
        return pick(options, menu,indicator='>>')[1]
    
    def _extracted_from_stream_10(self,arg0, name,info_hash, command) -> None:
        print(arg0.format(name))
        com = command+info_hash
        os.system(com)
    
    def stream(self,name,info_hash) -> None:
        options = ["Stream","Download","Exit"]
        selected = self.display_menu(options,"Pick one options")
        if selected==0:
            self._extracted_from_stream_10(
                "Playing {}......", name, info_hash, 'webtorrent --mpv --quiet '
            )
        elif selected==1:
            self._extracted_from_stream_10("Downloading {}......", name, info_hash, 'webtorrent --quiet ')
        else:
            exit()
               
    def search(self) -> None:
        search_term:str = input("What would you like to watch today? ")
        print(search_term)
        response_from_o33x:dict = self.o33x.search(search_term)
        response_from_piratebay:dict = self.pirate.search(search_term)
        total:list = list(response_from_o33x)
        total.append(list(response_from_piratebay))
        menu_entry_index: int = self.display_menu(total, f'Search Results for {search_term.replace("|", " ")}')

        info_hash:str =None
        info_hash = self.pirate.get_info_hash(res = response_from_piratebay,search = total[menu_entry_index])
        if info_hash is None:
            info_hash = self.o33x.get_info_hash(res = response_from_o33x,search = total[menu_entry_index])
        self.stream(name=total[menu_entry_index],info_hash=info_hash)

            
            

        
    
    
    

    
    

        
    
                
      
            
        


