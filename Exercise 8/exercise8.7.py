def make_album(artist, title, songs=None):
    """Build a dictionary describing a music album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album_dict['songs'] = songs
    return album_dict

print(make_album('am', 'no. 1 party anthem'))
print(make_album('beethoven', 'ninth symphony'))
print(make_album('willie nelson', 'red-headed stranger'))
print(make_album('iron maiden', 'piece of mind', songs=9))