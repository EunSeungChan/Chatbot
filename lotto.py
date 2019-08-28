"""
requests를 통해 동행복권 API 요청을 보내어,
1등 번호를 가져와 python list로 만듬
"""
import requests

# 1. requests 통해 요청 보내기
# requests.get('주소')
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
response = requests.get(url)
res_dict = response.json()
print(res_dict)
print(res_dict['drwtNo1'])

# 1등 번호 6개가 담긴 result라는 list를 출력

# 해당 코드를  Flask 서버(app.py) /lotto 함수에 적용.

# Bithnumb open API를 활용하여,
# 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py

result = []

for i in range(1,7):
    result.append(res_dict[f'drwtNo{i}'])

print(result)