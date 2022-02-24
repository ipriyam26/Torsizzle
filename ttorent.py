

import requests
from bs4 import BeautifulSoup
from simple_term_menu import TerminalMenu
import urllib.parse

class OneThreeThreeX:
    
    def __init__(self) -> None:
        self.header = {
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        }
        self.names = []
        self.links = []

    def add_list(self,response):
        """
        This funtion gets links and makes names, then zips them into a dictonary returning it
        to the calling function
        """
        # print(response.text
        soup = BeautifulSoup(response.text, 'html.parser')
        pkt = soup.select('.icon+ a')
        size = soup.select('.mob-uploader')
        i=0

        while(i<pkt.__len__()):
            self.names.append(f"{pkt[i].text} ({size[i].text})")
            self.links.append(f"{pkt[i].get('href')}")
            i+=1
        
        res = dict(zip(self.names, self.links))
        return  res  
            
            
            
    def get_info_hash(self,res,selected):
        # terminal_menu = TerminalMenu(self.names,clear_screen=True,title=menu,menu_highlight_style=("bg_red", "fg_yellow"))
        # menu_entry_index = terminal_menu.show()
        """
        This function gets the info hash from the selected torrent
        
        """

        q=res.get(selected)
        response = requests.get(f'https://www.1377x.to{q}', headers=self.header)
        soup = BeautifulSoup(response.text,'html.parser') 
        return soup.select_one('.infohash-box span').text
    
    
    
    
    def search_parser(self,search):

        q= urllib.parse.quote(search)
        response = requests.get(f"https://www.1377x.to/search/{q}/1", headers=self.header)
        print(response.text)
        self.add_list(response)
    
    def popular_parser(self):
        response = requests.get('https://www.1377x.to/popular-movies', headers=self.header)
        self.add_list(response,menu="Popular Movies")
    
    def popular_tv_parser(self):
        response = requests.get('https://www.1377x.to/popular-tv', headers=self.header)
        self.add_list(response,menu="Popular TV")
    
    def popular_anime_parser(self):
        response = requests.get('https://www.1377x.to/cat/Anime/1/', headers=self.header)
        self.add_list(response,menu="Popular Anime")

    
    

# search = input("Enter the name of the torrent: ")
tt = OneThreeThreeX()
tt.popular_anime_parser()