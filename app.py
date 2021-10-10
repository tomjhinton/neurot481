from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random
img = Image.new('RGBA', (6000, 6000), color='white')
from dotenv import load_dotenv
import tweepy
import os
import io
import sys
import numpy as np
from PIL import Image, ImageFont
import requests
import matplotlib.pylab as plt
import matplotlib.colors as mclr
from random import randint, seed
import json
import math
import PIL



def Random_Alpha():
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return l[random.randint(0,25)]

def create():

    quote_font = ImageFont.truetype('Art-Dystopia-2.ttf', randint(350, 1000))
    quote_font1 = ImageFont.truetype('Passio-Graphis.otf', randint(350, 1000))
    quote_font2 = ImageFont.truetype('FerriteCoreDX-Medium.otf', randint(350, 1000))


    arr = [quote_font, quote_font1, quote_font2]


    im2 = Image.new("RGB", (1000, 1000))
    draw = ImageDraw.Draw(im2)

    offset = 0


    for i in range(randint(1000, 3000)):
            draw = ImageDraw.Draw(im2)
            draw.multiline_text((randint(-10, 1000),randint(-10, 1000)), Random_Alpha(), tuple(np.random.randint(256, size=3)), font=arr[randint(0, 2)])
            quote_font = ImageFont.truetype('Art-Dystopia-2.ttf', randint(350, 1000))
            quote_font1 = ImageFont.truetype('Passio-Graphis.otf', randint(350, 1000))
            quote_font2 = ImageFont.truetype('FerriteCoreDX-Medium.otf', randint(350, 1000))
            arr = [quote_font,  quote_font1, quote_font2,
            ]
            im2 = im2.rotate(45)

    draw = ImageDraw.Draw(im2)


    for i in range(randint(15, 20)):
        im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)




    c_k = os.getenv("API_key")
    c_s = os.getenv("API_secret_key")
    a_k = os.getenv("Access_token")
    a_s = os.getenv("access_token_secret")
    auth = tweepy.OAuthHandler(c_k, c_s)
    auth.set_access_token(a_k, a_s)
    api = tweepy.API(auth)

    mapikc= os.getenv('musixmatch')

    albums = ['16157246', '28512785', '14257472']

    trackIds = requests.get(
  'https://api.musixmatch.com/ws/1.1/album.tracks.get?apikey='
  +  mapikc +
  '&album_id=' + albums[randint(0,2)]
)


    ids = trackIds.json()


    lyrics = requests.get(
      'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey='
      + mapikc +
      '&track_id=' + str(ids['message']['body']['track_list'][randint(0,len(ids['message']['body']['track_list'])-1 )]["track"]["track_id"])
    )

    lyrics = lyrics.json()




    i = lyrics['message']['body']['lyrics']['lyrics_body'].upper().split('\n')

    i = list(filter(lambda x : len(x) > 4 , i))
    buf = io.BytesIO()
    im2.save(buf, format='PNG')
    buf.seek(0)
    thing = buf.getvalue()
    test = api.media_upload('art.png',file= buf)
    api.update_status(status=i[randint(0,len(i)-3)], media_ids=[test.media_id])

create()
