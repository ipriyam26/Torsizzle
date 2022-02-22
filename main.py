


from simple_term_menu import TerminalMenu
import streaming


def start_menu():
    
    options = ['[1] Search','[2] Top 100 Movies','[3] Top 100 HD Movies','[4] Top 100 Series','[5] Top Audiobooks','[6] Exit']
    terminal_menu = TerminalMenu(options,clear_screen=True,title="Menu",menu_highlight_style=("bg_red", "fg_yellow"))
    menu_entry_index = terminal_menu.show()
    return int(menu_entry_index)+1




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
    
    


    