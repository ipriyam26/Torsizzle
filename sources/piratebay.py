import requests
from typing import Union

class Piratebay:
    
    def __init__(self) -> None:
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        }
        self.names = []
        self.info_hash = []
        
    
    def get_info_hash(self,search: str,res: dict) -> str:
        
        """
        This function takes in selected torrent and returns the info hash
        as we gonna fix stuff up after getting the torrents from different sources,
        so we should check each one of them and return the info hash if present else just return None 
        and check at call to see if this was the correct method
        """

        return  res.get(search) if res.get(search)!=None else None
        
        
    def _add_to_dict(self,response) -> Union[dict,None]:
        """
        This function takes in response from the calling methods and 
        process's the json to find all the torrents
        and process them into a dictionary
        """
        t =   response.json() if response.status_code==200 else None
        if t is None:
            print("Sorry, coundn't find the data....")
            return None

        for element in t:
            if int(element['seeders']) >10:
                size = float("{:.2f}".format(float(element['size'])/1000000000.0))
                self.names.append(f"{element['name']}  [{size}GB]")
                self.info_hash.append(element['info_hash'])
        return dict(zip(self.names, self.info_hash))
            
            
    def search(self,search: str)-> dict:
        """
        Use this function to search for queries on piratebay
        this function calls the inner api of piratebay and passes the response to 
        _add_to_dict function to process the json.
        """
        paylode = {'q':search}
        response = requests.get('https://apibay.org/q.php',params=paylode,headers=self.header)
        #  self.menu = "Search Results for {}".format(search)
        return self._add_to_dict(response)     
        

        
    def get_top_series(self)-> dict:
        """
        This function calls the inner api for the top series in pirate bay 
        and returns the result to 
        _add_to_dict function to process the json.
        """
        response = requests.get('https://apibay.org/precompiled/data_top100_205.json',headers=self.headers)
        # self.menu = "Top Series"
        return self._add_to_dict(response)
        
    def get_top_movies_HD(self)-> dict:
        
        response = requests.get('https://apibay.org/precompiled/data_top100_207.json',headers=self.headers)
        # self.menu = "Top Movies HD"
        return self._add_to_dict(response)    
        
    def get_top_audiobooks(self)-> dict:
        response = requests.get('https://apibay.org/precompiled/data_top100_102.json',headers=self.headers)
        # self.menu="Top Audiobooks"
        return self._add_to_dict(response)

if __name__== "__main__":
    
    pp = Piratebay()
    print(pp.search("Red Notice"))
    
    