import json
from dotenv import load_dotenv
from collections import defaultdict
from time import sleep
import threading

## undocumented api call
from PeekFriends import PeekFriends

#### imports for spotify public api
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# loading secrets
from dotenv import load_dotenv
import os
load_dotenv('.env.documented')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')


### globals
recs = []
recartist = []
source = []
favs = defaultdict(list)


## using Spotify Api
class Load():
    def __init__(self):
        pass

    ## returns your top artists in the short term on spotify
    def getTopArtists(self):
        top_artists = set()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_secret=client_secret, redirect_uri=redirect_uri, scope='user-top-read'))
        results = sp.current_user_top_artists(time_range="short_term", limit=50)
        for item in results['items']:
            top_artists.add(item['name'])
        return top_artists

    ## uses your top_artists to make a dictionary of the songs you like from them
    def getTopArtistsLikedSongs(self, top_artists):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))
        maxSongs = 500
        numSongsChecked = 0
        size = 50
        while numSongsChecked < maxSongs: 
            results = sp.current_user_saved_tracks(limit=size, offset=numSongsChecked)
            for item in results["items"]:
                # use all the artists for the comparison
                for artist in item["track"]["artists"]:
                    if artist["name"] in top_artists:
                        string = "".join(item["track"]["name"])
                        favs[artist["name"]].append(string)
                        break
            numSongsChecked+=size

    ## populates the favs dictionary with artists and top songs
    def update(self):
        top_artists = self.getTopArtists()
        self.getTopArtistsLikedSongs(top_artists)

## writes your recs to file (they are globals)
def writeToRecs():
    with open('recs.json', 'r') as f:
        data = json.load(f)
    data["recs"] += recs
    data["recartist"] += recartist
    data["source"] += source
    with open('recs.json', 'w') as f:
        json.dump(data, f, indent=4)
    return True

# background process
def listenerProcess(peaky, cycleLength):
    while running:
        for i in range(cycleLength):
            if not running:
                print("Listener stopped.")
                return
            sleep(1)
        ## checked every second for cycleLength
        ## end of the cycle we use listening to friends
        friends = peaky.getFriendSongList()
        # [friendname, songname, artistname]
        fri, son, art = 0, 1, 2
        for friend in friends:
            if (friend[art] in favs) and (friend[son] not in recs): # (friend[son] not in favs[friend[art]]) 
                recs.append(friend[son])
                recartist.append(friend[art])
                source.append(friend[fri])
                print("\nFound a rec\n")


def main():
    print("Starting spotif-eyes...")

    l = Load()
    l.update()
    print("Loaded your top artists and favourite songs.\n")

    peaky = PeekFriends()
    global running
    running = False
    listener = threading.Thread(target=listenerProcess, args=(peaky, 30))

    print('Enter "start" to start the listening')
    while True:
        usin = input(">")
        match usin:
            case "start":
                if not running:
                    running = True
                    listener.start()
                    print("Now listening to your friends...")
                else:
                    print("Already running.")
            case "stop":
                if running:
                    running = False
                    listener.join()
                    print("You have ", len(recs), " new recommendations.")
                else:
                    print("Not started, nothing to stop.")
            case "status":
                print("here it will print what your mates are listening to, number of new recs since recs called")
                print(peaky.getFriendSongList())
            case "recs":
                print("will give you ur list of recs")
                for song, artist, friend in zip(recs, recartist, source):
                    print(song, "- ", artist, " from ", friend)
            case "saverecs":
                print("saves your recs to your liked songs")
                writeToRecs()
            case "exit":
                if running:
                    print("Stopping listener...")
                    running = False
                    listener.join()                
                print("Saving your recs to file...")
                writeToRecs()
                sleep(0.1)
                print("File saved.")
                sleep(1)
                exit()
            case _:
                print("unknown input")
main()
