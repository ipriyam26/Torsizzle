#!./venv/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
from typing import Dict
from typing import Any, Dict, List
import requests
import os
import platform
from pick import pick
from controller import Controller


class Torrent:
    def __init__(self):
        self.platform = platform.system()
        # self.o33x = OneThreeThreeX()
        self.controller = Controller()
    
    def beautify_name(self,data:List[Dict[str, Any]])-> List[str]:
        result:List[str] = []
        for movies in data:
            name = f'[{movies["id"]}] - {movies["name"]} [{movies["size"]}]'
            result.append(name)
        return result

    def main_menu(self):
        options = ["Search","Top Series", "Top Movies","Top Anime", "Top Audiobooks", "Exit"]    
        menu = "Welcome to Torsizzle, Pick one option to continue"
        selected= self.display_menu(options, menu)
        if selected == 0:
            self.search()
        self.main_menu_selection(selected)
        
    def main_menu_selection(self, selected:int):
        
        selected_option:Dict[int,function] = {
            1: self.controller.get_top_series,
            2: self.controller.get_top_movies,
            3: self.controller.get_top_anime,
            4: self.controller.get_top_audiobooks,
        }
        data:List[Dict[str, Any]] = selected_option[selected]()
        result = self.beautify_name(data)
        print(self.display_menu(result, "Pick one option"))
    
    
    def display_menu(self, options: list, menu: str) -> int:
        return pick(options, menu, indicator=">>")[1]

    def _extracted_from_stream_10(self, arg0, name, info_hash, command) -> None:
        print(arg0.format(name))
        com = command + info_hash
        os.system(com)

    def stream(self, name, info_hash) -> None:
        options = ["Stream", "Download", "Exit"]
        selected = self.display_menu(options, "Pick one options")
        if selected == 0:
            self._extracted_from_stream_10(
                "Playing {}......", name, info_hash, "webtorrent --mpv --quiet "
            )
        elif selected == 1:
            self._extracted_from_stream_10(
                "Downloading {}......", name, info_hash, "webtorrent --quiet "
            )
        else:
            exit()

    def search(self) -> None:
        search_term: str = input("What would you like to watch today? ")
        data: List[Dict[str, Any]] = self.controller.search(search_term)
        result = self.beautify_name(data)
        print(self.display_menu(result, "Pick one option"))
        # self.stream(name=total[menu_entry_index], info_hash=info_hash)

if __name__ == '__main__':
    obj = Torrent()
    obj.main_menu()