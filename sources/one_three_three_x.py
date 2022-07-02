import requests
from bs4 import BeautifulSoup
from simple_term_menu import TerminalMenu
import urllib.parse


class OneThreeThreeX:
    def __init__(self) -> None:
        self.header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62",
        }
        self.names = []
        self.links = []

    def add_to_dict(self, response) -> dict:
        """
        This funtion gets links and makes names, then zips them into a dictonary returning it
        to the calling function
        """
        soup = BeautifulSoup(response.text, "html.parser")
        pkt = soup.select(".icon+ a")
        size = soup.select(".mob-uploader")
        i = 0
        while i < pkt.__len__():
            self.names.append(f"{pkt[i].text} ({size[i].text})")
            self.links.append(f"{pkt[i].get('href')}")
            i += 1

        return dict(zip(self.names, self.links))

    def get_info_hash(self, res: dict, search: str) -> str:
        """
        This function takes in search torrent and returns the info hash
        as we gonna fix stuff up after getting the torrents from different sources,
        so we should check each one of them and return the info hash if present else just return None
        and check at call to see if this was the correct method
        """
        print(search)
        q = res.get(search)
        if q != None:

            response = requests.get(f"https://www.1377x.to{q}", headers=self.header)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.select_one(".infohash-box span").text
        else:
            return None

    def search(self, search: str) -> dict:
        params = (
            ("limit", "1"),
            ("format", "txt"),
            ("http", "true"),
            ("country", "US"),
            ("type", "http"),
            ("speed", "20"),
        )
        response = requests.get("http://pubproxy.com/api/proxy", params=params)
        print(response.text)
        proxies = {"http": response.text, "https": response.text}
        q = urllib.parse.quote(search)
        response = requests.get(
            f"https://www.1377x.to/search/{q}/1", headers=self.header, proxies=proxies
        )
        # print(response.text)
        return self.add_to_dict(response)

    def get_top_movies(self) -> dict:
        response = requests.get(
            "https://www.1377x.to/popular-movies", headers=self.header
        )
        return self.add_to_dict(response)

    def get_top_series(self) -> dict:
        response = requests.get("https://www.1377x.to/popular-tv", headers=self.header)
        return self.add_to_dict(response)

    def get_top_anime(self) -> dict:
        response = requests.get(
            "https://www.1377x.to/cat/Anime/1/", headers=self.header
        )
        return self.add_to_dict(response)


if __name__ == "__main__":

    torrent = OneThreeThreeX()
    menu = torrent.search("Thor")
    print(menu)
