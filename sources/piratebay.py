import requests
from typing import Union
from typing import Any, Dict, List


class Piratebay:
    def __init__(self) -> None:
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
        }
        self.link = "https://apibay.org/"
        self.data: List[Dict[str, Any]] = []

    def _extract_data(self, response) -> List[Dict[str, Any]]:
        """
        This function takes in response from the calling methods and
        process's the json to find all the torrents
        and process them into a dictionary
        """
        results = response.json() if response.status_code == 200 else None
        if results is None:
            return self.data

        for result in results:
            self.data.append(
                {
                    "name": result["name"],
                    "link": result["info_hash"],
                    "size": int(result["size"]) / 10**9,
                    "seeders": int(result["seeders"]),
                    "source": "piratebay",
                }
            )
        return self.data

    def search(self, search: str) -> List[Dict[str, Any]]:
        """
        Use this function to search for queries on piratebay
        this function calls the inner api of piratebay and passes the response to
        _extract_data function to process the json.
        """
        paylode = {"q": search}
        response = requests.get(
            f"{self.link}q.php", params=paylode, headers=self.headers
        )
        return self._extract_data(response)

    def get_top_series(self) -> List[Dict[str, Any]]:
        """
        This function calls the inner api for the top series in pirate bay
        and returns the result to
        _extract_data function to process the json.
        """
        response = requests.get(
            f"{self.link}precompiled/data_top100_205.json", headers=self.headers
        )
        # self.menu = "Top Series"
        return self._extract_data(response)

    def get_top_movies(self) -> List[Dict[str, Any]]:

        response = requests.get(
            f"{self.link}precompiled/data_top100_207.json", headers=self.headers
        )
        # self.menu = "Top Movies HD"
        return self._extract_data(response)

    def get_top_audiobooks(self) -> List[Dict[str, Any]]:
        response = requests.get(
            f"{self.link}precompiled/data_top100_102.json", headers=self.headers
        )
        # self.menu="Top Audiobooks"
        return self._extract_data(response)


if __name__ == "__main__":

    pp = Piratebay()
    print(pp.search("Red Notice"))
