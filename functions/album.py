def make_album(artist, title, song_count=None):
    album = {'artist': artist, 'title': title}
    if song_count:
        album['song_count'] = song_count
    return album

album_1 = make_album("kendrick lamar", "to pimp a butterfly")
album_2 = make_album("madvillain", "madvillainy")
album_3 = make_album("mf doom", "mm food")
album_4 = make_album("kendrick lamar", "damn", 14)

print(album_1)
print(album_2)
print(album_3)

print(album_4)