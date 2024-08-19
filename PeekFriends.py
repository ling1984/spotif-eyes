import requests

# loading secrets
from dotenv import load_dotenv
import os, json


class PeekFriends():
    def __init__(self):
        load_dotenv('.env.undocumented')
        self.sp_dc_cookie = os.getenv('SP_DC_COOKIE')

    def getAccessToken(self, sp_dc_cookie):
        result = requests.get(url='https://open.spotify.com/get_access_token?reason=transport&productType=web_player', headers={ "Cookie" : f"sp_dc={sp_dc_cookie}"})
        if "accessToken" in result.json():    
            return result.json()["accessToken"]
        return None

    def getFriendActivity(self, access_token):
        result = requests.get(url="https://guc-spclient.spotify.com/presence-view/v1/buddylist", headers = { "Authorization" : f"Bearer {access_token}"})
        return result.json()

    def getFriendSongList(self):
        accessToken = self.getAccessToken(self.sp_dc_cookie)
        output = []
        if accessToken:
            friendsjson = self.getFriendActivity(accessToken)
            for friend in friendsjson["friends"]:
                output.append([friend["user"]["name"], friend["track"]["name"], friend["track"]["artist"]["name"], friend["track"]["uri"]])
        return output