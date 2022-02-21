#!./venv/bin/python
# -*- coding: utf-8 -*-

from urllib import response
import requests
import os
from os import path



class Torrent:
    
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
            } 

    def parser(self,r):
        
        status = r.status_code
        t =   r.json() if status==200 else None
        if(t!=None  ):
            i=1
            selected = 0
            for search in t:
                if( int(search['seeders']) > 20):
                    print('[{}] {} ({})'.format(i,search['name'],search['seeders']))
                    i=i+1
            
            while True:
                selected = input("\nEnter Number to select : ")
                if(selected.isnumeric):
                    if( int(selected)<i):
                        break
                print("Please Enter Correct value")
                

            self.stream(int(selected)-1,t)

        else:
            print("Sorry Cannot find what you are searching for :(")
    
    
    def top_parser(self,r,start,end):
        
        status = r.status_code
        t =   r.json() if status==200 else None
        if(t!=None):
            i=start
            selected=0
            while i<end:
                size = float("{:.2f}".format(float(t[i]['size'])/1000000000.0))
                print(f"[{i+1}] {t[i]['name']} ({t[i]['seeders']}) [{size}GB]")
                # print(f'[{i+1}] {t[i]['name']}  [{float(t[i]['size'])/1000000000.0}GB]')
                i+=1
                
            while True:
                selected = input(
f"""
-> Enter Number to select [{start+1} - {end}]
-> Press n to go to next page
-> Press p to go to previous page
-> Enter: """)
                
                if( selected=='n' or selected=='p'):
                    break
                elif(selected.isnumeric):
                    if( int(selected)<=i ):
                        break
                print("Please Enter Correct value")   
            try:
                if selected=='n' and end<100:
                    self.top_parser(r,end,end+20)
                elif selected =='p' and start>=20:
                    self.top_parser(r,start-20,start)    
                elif(selected.isnumeric):
                    self.stream(int(selected)-1,t)
                else: 
                    print("Page does not exists....")
                    print("Sending you back to home screen...")
                    self.top_parser(r,0,20)
            except:
                print("There was an error please pick again....")
                self.top_parser(r,start,end)        
            
                 
    
    
    def stream(self,select,t):
        print("Playing {}......".format(t[select]['name']) )
        com = 'webtorrent --mpv ' + t[select]['info_hash'] 
        os.system(com)
        

            
        
    def seach_stream(self):
        Movie = input("What would you like to watch today? ")
        paylode = {'q':Movie}
        r = requests.get('https://apibay.org/q.php',params=paylode,headers=self.headers)
        self.parser(r)



    def top_movies(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_201.json',headers=self.headers)
        self.top_parser(response,0,20)
        
    def top_series(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_205.json',headers=self.headers)
        self.top_parser(response,0,20)
        
    def top_movies_HD(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_207.json',headers=self.headers)
        self.top_parser(response,0,20)    
        
    def top_audiobooks(self):
        response = requests.get('https://apibay.org/precompiled/data_top100_102.json',headers=self.headers)
        self.top_parser(response,0,20)
                
      
            
        


