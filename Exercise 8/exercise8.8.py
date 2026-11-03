def make_album(artist, title, songs=None):
    """Build a dictionary describing a music album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album_dict['songs'] = songs
    return album_dict

while True:
    print("\nPlease enter the album information:")
    print("(enter 'q' at any time to quit)")
    
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
        
    album_title = input("Album title: ")
    if album_title == 'q':
        break
        
    album = make_album(artist_name, album_title)
    print(album)