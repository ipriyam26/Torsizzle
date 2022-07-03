from pprint import pprint
from typing import Any, Dict, List
from unicodedata import name
from unittest import result
import requests
from bs4 import BeautifulSoup


class Glo:
    def __init__(self):
        self.headers = {
            "authority": "gtdb.cc",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7",
            "cache-control": "no-cache",
            "cookie": "Guest=hoc6l2ia5s65knj88a2s54vog1; lang=0",
            "dnt": "1",
            "pragma": "no-cache",
            "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
        }
        self.link = "https://gtdb.cc/"
        self.data: List[Dict[str, Any]] = []
        self.retry = 5

    def get_info_hash(self, link: str) -> str:
        import re
        print(link)
        return re.findall(r"btih:(.*?)&", link)[0]

    def get_top_series(self):
        params = (
            ("search", ""),
            ("cat", "41"),
            ("incldead", "0"),
            ("inclexternal", "0"),
            ("lang", "0"),
            ("sort", "seeders"),
            ("order", "desc"),
        )
        return self._extract_data(params)


    def get_top_movies(self):
        params = (
            ("search", ""),
            ("cat", "1"),
            ("incldead", "0"),
            ("inclexternal", "0"),
            ("lang", "0"),
            ("sort", "seeders"),
            ("order", "desc"),
        )
        return self._extract_data(params)


    def get_top_anime(self):
        params = (
            ("search", ""),
            ("cat", "28"),
            ("incldead", "0"),
            ("inclexternal", "0"),
            ("lang", "0"),
            ("sort", "seeders"),
            ("order", "desc"),
        )
        return self._extract_data(params)


    def search(self, search: str) -> List[Dict[str, Any]]:
        params = (
            ("search", search),
            ("cat", "41"),
            ("incldead", "0"),
            ("inclexternal", "0"),
            ("lang", "0"),
            ("sort", "seeders"),
            ("order", "desc"),
        )
        return self._extract_data(params)


    def _extract_data(self, params):
        
        response = requests.get(
            f"{self.link}search_results.php", headers=self.headers, params=params
        )
        
        for _ in range(self.retry):
            try:
                response = requests.get(
                f"{self.link}search_results.php", headers=self.headers, params=params
            )
            except Exception:
                response = requests.get(
                f"{self.link}search_results.php", headers=self.headers, params=params
            )
        soup = BeautifulSoup(response.text, "html.parser")
        names = soup.select(".ttable_col2 a+ a b")
        sizes = soup.select(".ttable_col1:nth-child(5)")
        seeders = soup.select(".ttable_col2 font b")
        links = soup.select(".ttable_col2~ .ttable_col2 a")

        for i in range(len(names)):
            if "btih" not in links[i].get('href'):
                continue
            self.data.append(
                {
                    "name": names[i].text,
                    "link": f"{self.link}{links[i].get('href')}",
                    "size": sizes[i].text,
                    "seeders": int(seeders[i].text.replace(",", "")),
                    "source": "glo",
                }
            )
        return self.data


if __name__ == "__main__":
    obj = Glo()
    pprint(obj.get_top_series())

