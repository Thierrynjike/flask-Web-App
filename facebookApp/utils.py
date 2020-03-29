import random
import os
# from PIL import Image, ImageDraw, ImageFont
# import textwrap
from facebookApp.models import Content


def find_content():
    contents = [Content.query.get(i).description for i in range(1,len(Content.query.all())+1)]
    return random.choice(contents)

#['You will being married at most on 31st february 2021', 'you will born twins in 2 years and the father will not be your husband',
#                                      'Your will get a proposal in few weeks. oups sorry for you COVID19 is out',
#                'Congratulations, you just earned a coupon for openclassroom premium account. haha i am joking go and sleep', "don't go out, i had a dream that you were contaminated by covid19 in ",
#               'your best friend will find a work in Amsterdam and she will cheat on his husband']

# class OpenGraphImage:

# def __init__(self, uid, first_name,description):
# background = self.base()
# self.print_on_img(background,first_name.capitalize(), 70, 50)
# #description, we split the description into several
# # sentences of 60 characters
# sentences = textwrap.wrap(description,width=60)
# current_h, pad==180, 10
# for sentence in sentences:
# w,h=self.print_on_img(background,sentence,40,current_h)
# current_h+=h+pad
# background.save(_path(uid))

# def base(self):
# #create a basic image
# img=Image.new('RGB',(1200,630),'#18BC9C')
# return img

# def print_on_img(self,img,text,size,height):
# #we start to load the used police
# font=ImageFont.truetype(os.path.join('fbapp','static',
# 'fonts','Arcon-Regular.otf'),size)
# #creation of a new instance
# draw=ImageDraw.Draw(img)

# #textsize returns the lenght and the width in pixels
# #of a string
# w,h=draw.textsize(text,font)

# #then we calculate the position to make the text to be
# #centered intead of being left aligned
# position=((img.width-w)/2, height)

# #Now we add the text on the image
# draw.text(position,text,(255,255,255), font=font)
# return (w,h)

# def _path(self,uid):
# return os.path.join('facebookApp','static','tmp','{}.jpg'.format(uid))

# description="""Toi, tu sais comment utiliser la console, t'es jamais 
# à court d'idées pour réaliser ton objectif, tu es déterminé-e et
# et persévérant. Tes amis disent d'ailleurs volontier que
# tu as du caracctère et que tu ne te laisses pas marcher sur
# les pieds. un peu hacker sur les bords, tu aimes trouver des
# solutions à tout problème. N'aurais-tu pas un petit problème
# d'autorité?"""


# OpenGraphImageT('hierry',description)
