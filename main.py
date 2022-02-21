from os import path
import setup
import streaming

def start_menu():
    print("""
1. Search 
2. Top 100 Movies
3. Top 100 HD Movies
4. Top 100 Series
5. Top Audiobooks
6. Exit
    """)
    while True:
        selected = input("\nEnter Number to select : ")
        if(selected.isnumeric):
            if( int(selected)<7):
                break
        print("Please Enter Correct value")
    return int(selected)



if(not path.exists("req.txt")) :
    setup.setup()

selection = start_menu()

torrent = streaming.Torrent()
if selection==1:
    torrent.seach_stream()
elif selection==2:
    torrent.top_movies()
elif selection==3:
    torrent.top_movies_HD()
elif selection==4:
    torrent.top_series()
elif selection==5:
    torrent.top_audiobooks()
else:
    print("Exiting....") 
    exit()
    
    
    

    