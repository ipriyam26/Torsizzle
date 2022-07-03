from typing import Any, Dict, List



class Base:
    def __init__(self) -> None:
        pass

    def get_info_hash(self, link:str) -> str:
        return ""
        
    def search(self, search: str) ->  List[Dict[str, Any]]:
        return []

    def get_top_movies(self) ->  List[Dict[str, Any]]:
        return []

    def get_top_series(self) ->  List[Dict[str, Any]]:
        return []

    def get_top_anime(self) ->  List[Dict[str, Any]]:
        return []
    
    def get_top_audiobooks(self) -> List[Dict[str, Any]]:
        return []


