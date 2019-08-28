"""
python으로 telegram message 보내기
"""

import requests

# (1) getUpdates를 통해 chat_id를 가져오기
chat_id = ''

# (2) url을 조합하여 requestes로 요청보내기

token = ''
base_url = 'https://api.telegram.org'

url = f'{base_url}/bot{token}/getUpdates'

res = requests.get(url)
res_dict =res.json()

chat_id = res_dict['result'][0]['message']['chat']['id']
msg = 'wow'
url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}'
print(url)