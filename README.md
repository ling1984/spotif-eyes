# Spotif-eyes
 
 Spotif-eyes is a Python script that monitors friend activity and compares it to your favourite artists.

 If there is a match, it adds it to a playlist for you.

## Features
The script is controlled by a small shell and here is a list of possible instructions:
* `start` - start the listening process
* `stop` - stop the listening process, print number of recommendations
* `status` - prints a list of all your mates, the artist they are listening to, the song, and the songs URI (Uniform Resource Identifier
(spotify identification code))
* `save` - saves the current recommendations to your Friend Recs playlist on Spotify (creates it if you haven't run this before)
* `exit` - stops the listener, saves the recommendations, exits the script


## Set-up
To get this script to work, you will need to create two files in this folder:
* .env.documented
* .env.undocumented

In **.env.documented** it should say:


`SPOTIPY_CLIENT_ID=your_spotify_client_id`

`CLIENT_SECRET=your_spotify_client_secret`

`REDIRECT_URI=your_redirect_uri`

You can get these using the instructions on the [Spotify website](https://developer.spotify.com/documentation/web-api/concepts/apps). It doesn't matter the name or the description and if you don't know better use a Redirect URI of `http://localhost:8000/callback`.

In **.env.undocumented** it should say:

`SP_DC_COOKIE=your_cookie`

You can find this cookie by using a browser extension for viewing/editing cookies and going on [Spotify Web Player](https://open.spotify.com/). 

## Troubleshooting
1. Check your SP_DC_COOKIE is up-to-date
2. As it is an unofficial API, this may not work anymore
3. If you are getting errors or exceptions, you are welcome to fork the code and add some try/ except blocks.

## Credit + How it is made

Made using the [Spotify API](https://developer.spotify.com/documentation/web-api) and [Spotipy](https://github.com/spotipy-dev/spotipy), as well as this [git repo](https://github.com/valeriangalliat/spotify-buddylist).

Full credit to [valeriangalliat](https://github.com/valeriangalliat) for finding and writing about the Spotify unofficial API for this usage.

## Responsible API Usage

As we are using an unofficial API for Spotify, the requests are set to only call every 30 seconds. Also this is a request which the app makes itself so it is likely to continue to be supported.
