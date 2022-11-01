# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:47:33 2022

@author: chonlatid.d
"""

from senginta.static.Google import GSearch
search_spider = GSearch('test')
print(search_spider.to_json())
a = search_spider.get_all()

#%%
import pandas as pd
df_json = pd.read_json('thai-food-open-data/food.json')
