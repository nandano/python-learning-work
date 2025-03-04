favorite_places = {
    'jack': ['new york', 'new delhi', 'paris'],
    'rose': ['antarctica', 'paris', 'dublin'],
    'mike': ['helsinki', 'nairobi', 'toronto'],
}

for name in favorite_places.keys():
    print(f"\n{name.title()}'s favorite places are:")
    for place in favorite_places[name]:
        print(f"\t{place.title()}")