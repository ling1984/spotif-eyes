import requests

# loading secrets
from dotenv import load_dotenv
import os, json

load_dotenv('.env.undocumented')
sp_dc_cookie = os.getenv('SP_DC_COOKIE')

def getAccessToken(sp_dc_cookie):
    result = requests.get(url='https://open.spotify.com/get_access_token?reason=transport&productType=web_player', headers={ "Cookie" : f"sp_dc={sp_dc_cookie}"})
    if "accessToken" in result.json():    
        return result.json()["accessToken"]
    return None

def getFriendActivity(access_token):
    result = requests.get(url="https://guc-spclient.spotify.com/presence-view/v1/buddylist", headers = { "Authorization" : f"Bearer {access_token}"})
    return result.json()




# accessToken = getAccessToken(sp_dc_cookie)
accessToken = "BQAEwsQdpG5jyqq3FT1121kLjq6FMRwJBNPdCv18Cz2TGol38wQghNr2jxbERq4wxMUPUCHVwklwzNmke17BU_lVp0OAQV5ik5jnfn0Csn_1r333uiFfIQqFuD5vvkRVdDWJPm6UYdTg18yHHXmNei7ZnrCb86rQBbldRj8SxEHXAuAOht8E5ml_KgACAX_2KEvIx_e0bEkELC_dfeDUMdtCgIsy414ukJoRfxboowgys3DFCUUdMAbbMySJDqal_WJ8lkQ-x5SsbpA346tbQztI0XZV6Bjg6t0IgWBKDEQP8ER4yWS2PsFf0U9J"
if accessToken:
    friendsjson = getFriendActivity(accessToken)
    for friend in friendsjson["friends"]:
        print(friend["user"]["name"], ": ")
        print(friend["track"]["name"], " - ", friend["track"]["artist"]["name"])