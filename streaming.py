#!./venv/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
from typing import Dict
from typing import Any, Dict, List
import os
import platform
from pick import pick
from controller import Controller


class Torrent:
    def __init__(self):
        self.platform = platform.system()
        self.controller = Controller()
        self.debug = False
    

    def main_menu(self):
        options = ["Search","Top Series", "Top Movies","Top Anime", "Top Audiobooks", "Exit"]    
        menu = "Welcome to Torsizzle, Pick one option to continue"
        selected= self.display_menu(options, menu)
        print("Please wait while we are loading your data...")
        self.logic(selected)

    def main_menu_selection(self, selected_option):
        data:List[Dict[str, Any]] = selected_option()
        self._helper_controller(data)
    
    
    def display_menu(self, options: list, menu: str) -> int:
        os.system("clear")
        return pick(options, menu, indicator=">>")[1]


    def stream(self, name, info_hash) -> None:
        options = ["Stream", "Download", "Exit"]
        selected = self.display_menu(options, "Pick one options")
        self.logic2(name, info_hash, selected) 


    def search_menu(self) -> None:
        search_term: str = input("What would you like to watch today? ")
        data: List[Dict[str, Any]] = self.controller.search(search_term)
        self._helper_controller(data)
        
    def quit(self) -> None:
        os.system("clear")
        print("Thanks for using Torsizzle!, See you soon!")    
        exit()
        
    def logic(self, selected):
        if selected == 0:
            self.search_menu()
        elif selected == 5:
            self.quit() 
        selected_option:Dict[int,function] = {
            1: self.controller.get_top_series,
            2: self.controller.get_top_movies,
            3: self.controller.get_top_anime,
            4: self.controller.get_top_audiobooks,
        }
        self.main_menu_selection(selected_option[selected])
        
    def logic2(self, name, info_hash, selected):
        if selected == 0:
            self._player(
                "Playing {}......", name, info_hash, "webtorrent --mpv --quiet "
            )
        elif selected == 1:
            self._player(
                "Downloading {}......", name, info_hash, "webtorrent --quiet "
            )
        else:
            self.quit()

    def beautify_name(self,data:List[Dict[str, Any]])-> List[str]:
        if self.debug:
            pprint(data)
        result:List[str] = []
        for movies in data:
            space = "" if movies["id"]>9 else " "
            name = f'[{movies["id"]}]{space} - {str(movies["name"]).replace("."," ").replace("  "," ")} [{movies["size"]}] {movies["source"]}'
            result.append(name)
        return result
    
    def _helper_controller(self, data):
        result = self.beautify_name(data)
        selected_2 = self.display_menu(result, "Pick one option")
        info_hash = self.controller.get_info_hash(data[selected_2])
        self.stream(name=str(data[selected_2]["name"]).replace("."," ").replace("  "," "), info_hash=info_hash)
        
    def _player(self, arg0, name, info_hash, command) -> None:
        print(arg0.format(name))
        com = command + info_hash
        os.system(com)
        

if __name__ == '__main__':
    obj = Torrent()
    obj.main_menu()