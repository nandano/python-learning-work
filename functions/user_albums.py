def make_album(artist, title):
    album = {'artist': artist, 'title': title}
    return album

while True:
    print("\n(enter 'q' to exit the program)")
    user_artist = input("\nEnter artist's name: ")
    if user_artist == 'q':
        break

    user_title = input("Enter album's title: ")
    if user_title == 'q':
        break

    new_album = make_album(user_artist, user_title)
    print(new_album)