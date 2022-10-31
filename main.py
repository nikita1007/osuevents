from xml.etree.ElementTree import tostring
import requests
import json
import urllib.parse
from dotenv import dotenv_values


#* Take environment variables from .env
config = dotenv_values(".env")


params = urllib.parse.urlencode({
  'group_id': 'gamehub',
})

url = "https://api.vk.com/method/groups.getById?{params}&access_token={token}&v={api_version}".format(params=params,token=config.get('VK_APP_API_KEY'), api_version=config.get('VK_APP_VER'))

r = requests.get(url)

# f = open('response.json', 'w+')

# f.write(r.text)

print(r.json()['response'][0]['id'])

params = urllib.parse.urlencode({
  'owner_id': '-137861565',
  'count': '10',
})

url = "https://api.vk.com/method/wall.get?{params}&access_token={token}&v={api_version}".format(params=params,token=config.get('VK_APP_API_KEY'), api_version=config.get('VK_APP_VER'))

r = requests.get(url)

f = open('group_wall.json', 'w+')

f.write(r.text)

print(r.json())