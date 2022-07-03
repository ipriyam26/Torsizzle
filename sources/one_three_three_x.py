from pprint import pprint
from typing import Any, Dict, List
import requests
from bs4 import BeautifulSoup
import urllib.parse


class OneThreeThreeX:
    def __init__(self) -> None:
        self.header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62",
        }
        self.link = "https://www.1377x.to"
        self.data = []
        self.threshold = 5


    def _extract_data(self, response: requests.Response) ->  List[Dict[str, Any]]:
        """
        This funtion gets links and makes names, then zips them into a dictonary returning it
        to the calling function
        """
        soup = BeautifulSoup(response.text, "html.parser")
        pkt = soup.select(".icon+ a")
        size = soup.select(".mob-uploader")
        seeders = soup.select(".seeds")

        for i in range(len(pkt)):
            self.data.append(
                {
                    "name": pkt[i].text,
                    "link": self.link+pkt[i].get("href"),
                    "size": size[i].text,
                    "seeders": int(seeders[i].text),
                    "source": "1337x",
                }
            )

        return self.data

    def get_info_hash(self, link:str) -> str:
        """
        This function takes in search torrent and returns the info hash
        as we gonna fix stuff up after getting the torrents from different sources,
        so we should check each one of them and return the info hash if present else just return None
        and check at call to see if this was the correct method
        """
        print("one three three x")
        response = requests.get(link, headers=self.header,timeout=self.threshold)
        soup = BeautifulSoup(response.text, "html.parser")
        magnet = soup.select_one(".l0d669aa8b23687a65b2981747a14a1be1174ba2c").get("href")
        import re
        return re.findall(r"btih:(.*?)&", magnet)[0]
    def search(self, search: str) -> dict:
        params = (
            ("limit", "1"),
            ("format", "txt"),
            ("http", "true"),
            ("country", "US"),
            ("type", "http"),
            ("speed", "20"),
        )
        # response = requests.get("http://pubproxy.com/api/proxy", params=params)
        # print(response.text)
        # proxies = {"http": response.text, "https": response.text}
        q = urllib.parse.quote(search)
        response = requests.get(
            f"https://www.1377x.to/search/{q}/1", headers=self.header,timeout=self.threshold
            # proxies=proxies
        )
        # print(response.text)
        return self._extract_data(response)

    def get_top_movies(self) -> dict:
        response = requests.get(
            "https://www.1377x.to/popular-movies", headers=self.header,timeout=self.threshold
        )
        return self._extract_data(response)

    def get_top_series(self) -> dict:
        response = requests.get("https://www.1377x.to/popular-tv", headers=self.header,timeout=self.threshold
                                )
        return self._extract_data(response)

    def get_top_anime(self) -> dict:
        response = requests.get(
            "https://www.1377x.to/cat/Anime/1/", headers=self.header,timeout=self.threshold
        )
        return self._extract_data(response)


if __name__ == "__main__":

    torrent = OneThreeThreeX()
    menu = torrent.search("Thor")
    pprint(menu)
