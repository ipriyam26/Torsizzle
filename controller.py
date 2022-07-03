from pprint import pprint
from sources.piratebay import Piratebay
from sources.anidex import Anidex
from sources.glo import Glo
from sources.torrentz2 import Torrentz2
from sources.one_three_three_x import OneThreeThreeX
from typing import Any, Callable, Dict, List


class Controller:
    def __init__(self) -> None:
        self.piratebay = Piratebay()
        self.anidex = Anidex()
        self.glo = Glo()
        self.torrentz2 = Torrentz2()
        self._1337x = OneThreeThreeX()
        self.result = []
        self.page = 1
        self.total_pages = 0

    def _helper(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        results = sorted(results, key=lambda x: x["seeders"], reverse=True)
        for id in range(len(results)):
            results[id]["id"] = id
        self.total_pages = len(results) // 20 + 1
        self.result = results
        self.page += 1
        return self.result[:20]
    
    def get_info_hash(self,object:Dict[str, Any]) -> str:
        source:str = object["source"]
        info_hash:Dict[str,function] = {
            "piratebay": self.piratebay.get_info_hash,
            "anidex": self.anidex.get_info_hash,
            "glo": self.glo.get_info_hash,
            "torrentz2": self.torrentz2.get_info_hash,
            "1337x": self._1337x.get_info_hash
        }
        return info_hash[source](object.get("link"))
        
        
    def search(self, search_term: str) -> List[Dict[str, Any]]:
        piratebay_dict = self.piratebay.search(search_term) or []
        anidex_dict = self.anidex.search(search_term) or []
        glo_dict = self.glo.search(search_term) or []
        torrentz2_dict = self.torrentz2.search(search_term) or []
        _1337x_dict = self._1337x.search(search_term) or []
        return self._helper(piratebay_dict + anidex_dict + glo_dict + torrentz2_dict)

    def get_top_anime(self) -> List[Dict[str, Any]]:
        results = self.anidex.get_top_anime()
        _1337x_dict = self._1337x.get_top_anime() or []
        
        return self._helper(results + _1337x_dict)

    def get_top_series(self) -> List[Dict[str, Any]]:
        glo_dict = self.glo.get_top_series() or []
        piratebay_dict = self.piratebay.get_top_series() or []
        _1337x_dict = self._1337x.get_top_series() or []
        results = glo_dict + piratebay_dict + _1337x_dict
        return self._helper(results)

    def get_top_movies(self) -> List[Dict[str, Any]]:
        glo_dict = self.glo.get_top_movies() or []
        piratebay_dict = self.piratebay.get_top_movies() or []
        _1337x_dict = self._1337x.get_top_movies() or []
        results = glo_dict + piratebay_dict + _1337x_dict
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
