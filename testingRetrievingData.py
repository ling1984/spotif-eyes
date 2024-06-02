# Shows the top artists for a user
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# loading secrets
from dotenv import load_dotenv
import os
load_dotenv('.env.documented')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')


# actual code
scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
shorterm, mediterm, longterm = {}, {}, {}

for sp_range in ['short_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        shorterm[item['name']] = i

print(shorterm)