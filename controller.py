from pprint import pprint
from sources.piratebay import Piratebay
from sources.anidex import Anidex
from sources.glo import Glo
from sources.torrentz2 import Torrentz2
from typing import Any, Dict, List


class Controller:
    def __init__(self) -> None:
        self.piratebay = Piratebay()
        self.anidex = Anidex()
        self.glo = Glo()
        self.torrentz2 = Torrentz2()
        self.result = []
        self.page = 1
        self.total_pages = 0

    def _helper(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = sorted(results, key=lambda x: x["seeders"], reverse=True)
        self.total_pages = len(results) // 20 + 1
        self.result = results
        self.page += 1
        return self.result[:20]

    def search(self, search_term: str) -> List[Dict[str, Any]]:
        piratebay_dict = self.piratebay.search(search_term)
        anidex_dict = self.anidex.search(search_term)
        glo_dict = self.glo.search(search_term)
        torrentz2 = self.torrentz2.search(search_term)
        results = piratebay_dict + anidex_dict + glo_dict + torrentz2
        return self._helper(results)

    def get_top_anime(self) -> List[Dict[str, Any]]:
        results = self.anidex.get_top_anime()
        return self._helper(results)

    def get_top_series(self) -> List[Dict[str, Any]]:
        glo_dict = self.glo.get_top_series()
        piratebay_dict = self.piratebay.get_top_series()
        results = glo_dict + piratebay_dict if glo_dict else piratebay_dict
        return self._helper(results)

    def get_top_movies(self) -> List[Dict[str, Any]]:
        glo_dict = self.glo.get_top_movies()
        piratebay_dict = self.piratebay.get_top_movies()
        results = glo_dict + piratebay_dict if glo_dict else piratebay_dict
        return self._helper(results)

    def get_top_audiobooks(self) -> List[Dict[str, Any]]:
        results = self.piratebay.get_top_audiobooks()
        return self._helper(results)

    def get_more(self) -> List[Dict[str, Any]]:
        if self.page < self.total_pages:
            ans = self.result[20 * (self.page - 1) : 20 * self.page]
            self.page += 1
        else:
            ans = self.result[20 * (self.page - 1) :]
        return ans


if __name__ == "__main__":
    control = Controller()
    pprint(control.search("Doctor Strange"))
