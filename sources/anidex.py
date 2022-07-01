from os import link
from typing import Any, Dict, List
import requests
from bs4 import BeautifulSoup

class Anidex:
    
    def __init__(self, *args, **kwargs):
        self.headers = {
            'authority': 'anidex.info',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'cookie': '__ddgid_=8XwWh7hGVDSAdYnS; __ddgmark_=Rx17LtZHRdPOVMlG; __ddg2_=FsLNp8QMgQ8PyrNC; __ddg1_=VpjXDFa44WMjZ9LNFR9V; PHPSESSID=ouedpmqj96e3u2mpjb2cluluis',
            'dnt': '1',
            'pragma': 'no-cache',
            'referer': 'https://anidex.info/?q=Fighting+Spirit',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
        }
        self.link = 'https://anidex.info'
        self.data:List[Dict[str,Any]] = []

    def _add_to_dict(self, response):
        pass
    
    def get_info_hash(self):
        for anime in self.data:
            response = requests.get(f"{self.link}{anime.get('link')}", headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            print(soup.select('kbd')[0].text)

    def get_top_anime(self):
        params = (
            ('q', ''),
            ('id', '1,2,3'),
            ('s', 'seeders'),
            ('o', 'desc'),
        )
        response = requests.post('https://anidex.info/', headers=self.headers, params=params)
        return self._extract_data(response=response)



    def search(self, search):
        paylode = {'q': search}
        response = requests.get(self.link, headers=self.headers, params=paylode)
        return self._extract_data(response=response)
    
    def _extract_data(self, response:requests.Response):
        soup = BeautifulSoup(response.text, 'html.parser')
        names = soup.select('.span-1440')
        llp = soup.select('.text-left+ td')
        sizes = soup.select('td:nth-child(7)')
        seeders = soup.select('td.text-success.text-right')
        
        for i in range(len(names)):
            self.data.append({
                'name': names[i].text,
                'link': llp[i].select_one('a').get('href'),
                'size': sizes[i].text,
                'seeders': seeders[i].text,
                'source': 'anidex'
            })
        
        return self.data

        
        


if __name__ == '__main__':
    ani = Anidex()
    # ani.search('Naruto')
    # ani.get_info_hash()
    print(ani.get_top_anime())