#%%
import wget

#%%

file_url = 'https://alttpr.com/sprites'

sprites_list = wget.download(file_url, 'sprites_list.json')
# %%
# with open('sprites_list.json', 'r') as f:
    # f.write(wget.download(file_url))
    # go get each sprite sheet

import json
sprites = json.loads(open('sprites_list.json').read())
# %%
for sprite in sprites:
    filename = sprite['file'].replace("\\","")
    wget.download(filename,"zspr/{0}.zspr".format(sprite['name']))