# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:31:29 2022

@author: chonlatid.d
"""
#%% import
import twint
import nest_asyncio
import pandas as pd
nest_asyncio.apply()
#%% get hashtag

config = twint.Config()
# config.Username = "elonmusk"
config.Search = "#สูตรอาหาร"
config.Pandas = True
config.Lang = "th"
twint.run.Search(config)
df = twint.storage.panda.Tweets_df

#%%เ get follower
c = twint.Config()
c.Username = "twitter"
c.User_full = True
c.Pandas = True
df = twint.run.Followers(c)