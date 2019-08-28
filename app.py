from flask import Flask
import random
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고,
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '은승찬'

@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}' 

@app.route('/square/<int:num>')
def square(num):
    
    return str(num **2)

@app.route('/menu')
def menu():
    foods = ['바스버거','대우식당','진가와','고갯마루']
    food = random.choice(foods)
    return food

@app.route('/lotto')
def lotto():
    result= []
    winner = []
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
    response = requests.get(url)
    res_dict = response.json()

    
    for i in range(1,7):
        winner.append(res_dict[f'drwtNo{i}'])
        
    result = random.sample(range(1,46),6)

    

    

    #result = [3,5,12,13,14,15]
    cnt = len(set(winner) & set(result))

  

    rank = '꽝'
    if cnt ==6:
        rank = '1등'
    elif cnt ==5:
        rank = '3등'
    elif cnt ==4:
        rank = '4등'
    elif cnt ==3:
        rank = '5등'        
            
    # 만약 6개가 모두 일치하면
    # 1등
    # 만약 5개가 일치하면
    # 3등
    # 만약 4개가 일치하면
    # 4등
    # 5등

    return str(sorted(result))+rank 

    
    

