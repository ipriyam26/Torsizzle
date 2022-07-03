from streaming import Torrent

from pick import pick


def start_menu():

    options = [
        "[1] Search",
        "[2] Top 100 Movies",
        "[3] Top 100 HD Movies",
        "[4] Top 100 Series",
        "[5] Top Audiobooks",
        "[6] Exit",
    ]

    option, menu_entry_index = pick(options, "Menu:", indicator=">>")

    return int(menu_entry_index) + 1


# selection = start_menu()

torrent = Torrent()
torrent.search()
