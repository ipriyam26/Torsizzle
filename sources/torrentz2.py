import requests
from bs4 import BeautifulSoup

class Torrentz2:
    
    def __init__(self, *args, **kwargs):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Pragma': 'no-cache',
            'Referer': 'https://2torrentz2eu.in/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }
        self.data = []
    
    def search(self, search):
        params = (
            ('q', search),
        )
        response = requests.get('https://2torrentz2eu.in/data.php', headers=self.headers, params=params)
        return self._extract_data(response=response)

    def _extract_data(self,response):
        soup = BeautifulSoup(response.text, 'html.parser')
        names = soup.select('td > span')
        seeds = soup.select('.age-data+ td')
        sizes = soup.select('td:nth-child(5)')
        link = soup.select('.magnet-link')

        for i in range(len(names)):
            self.data.append({
                'name': names[i].text,
                'seeds': seeds[i].text,
                'size': sizes[i].text,
                'link': f"https://2torrentz2eu.in/{link[i].get('href')}",
                'source': 'torrentz2'
            })
        return self.data
    

if __name__ == '__main__':
    obj = Torrentz2()
    print(obj.search("game of thrones"))
