from types import MethodType
from flask import Flask, render_template, jsonify
import flask
import requests
import json, re
from datetime import datetime
from flask_cors import CORS

def getres():
    onul=datetime.today().strftime("%Y%m%d")
    res = requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=GdWTDEeLjnO0YeiW5E4occlcHvqg03IlkDh5FCkW/JpS4g1l2idd09uocu8pLVYvNBp3GL0qvikxil85BaJy4A==&numOfRows=10&pageNo=1&base_date='+onul+'&base_time=0230&nx=55&ny=127&dataType=JSON')
    return res.text

app=Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET','POST'])
def index():
    onul=datetime.today().strftime("%Y%m%d")

    baseDate=[]
    baseTime=[]
    category=[]
    fcstDate=[]
    fcstTime=[]
    fcstValue=[]
    nx=[]
    ny=[]

    for i in getres().split(','):
        if 'baseDate' in i:
            baseDate.append(i)
        elif 'baseTime' in i:
            baseTime.append(i)
        elif 'category' in i:
            category.append(i)
        elif 'fcstDate' in i:
            fcstDate.append(i)
        elif 'fcstTime' in i:
            fcstTime.append(i)
        elif 'fcstValue' in i:
            fcstValue.append(i)
        elif 'nx' in i:
            nx.append(i)
        elif 'ny' in i:
            ny.append(i)
        else:
            None


    strbaseDate=re.findall(r'"([^"]*)"',str(baseDate))
    baseDate.clear()
    for i in range(3,22,2):
        baseDate.append(strbaseDate[i])


    strbaseTime=re.findall(r'"([^"]*)"',str(baseTime))
    baseTime.clear()
    for j in range(1,20,2):
        baseTime.append(strbaseTime[j])


    strcategory=re.findall(r'"([^"]*)"',str(category))
    category.clear()
    for k in range(1,20,2):
        category.append(strcategory[k])


    strfcstDate=re.findall(r'"([^"]*)"',str(fcstDate))
    fcstDate.clear()
    for z in range(1,20,2):
        fcstDate.append(strfcstDate[z])


    strfcstTime=re.findall(r'"([^"]*)"',str(fcstTime))
    fcstTime.clear()
    for x in range(1,20,2):
        fcstTime.append(strfcstTime[x])


    strfcstValue=re.findall(r'"([^"]*)"',str(fcstValue))
    fcstValue.clear()
    for y in range(1,20,2):
        fcstValue.append(strfcstValue[y])



    a=(
    {
    "data": {
        "fields": [
            { "name": "baseDate", "type": "TEXT" },
            { "name": "baseTime", "type": "TEXT" },
            { "name": "category", "type": "TEXT" },
            { "name": "fcstDate", "type": "TEXT" },
            { "name": "fcstTime", "type": "TEXT" },
            { "name": "fcstValue", "type": "TEXT" }
        ],
        "results": [
            [ baseDate[0], baseTime[0], category[0], fcstDate[0], fcstTime[0], fcstValue[0] ],
            [ baseDate[1], baseTime[1], category[1], fcstDate[1], fcstTime[1], fcstValue[1] ],
            [ baseDate[2], baseTime[2], category[2], fcstDate[2], fcstTime[2], fcstValue[2] ],
            [ baseDate[3], baseTime[3], category[3], fcstDate[3], fcstTime[3], fcstValue[3] ],
            [ baseDate[4], baseTime[4], category[4], fcstDate[4], fcstTime[4], fcstValue[4] ],
            [ baseDate[5], baseTime[5], category[5], fcstDate[5], fcstTime[5], fcstValue[5] ],
            [ baseDate[6], baseTime[6], category[6], fcstDate[6], fcstTime[6], fcstValue[6] ],
            [ baseDate[7], baseTime[7], category[7], fcstDate[7], fcstTime[7], fcstValue[7] ],
            [ baseDate[8], baseTime[8], category[8], fcstDate[8], fcstTime[8], fcstValue[8] ],
            [ baseDate[9], baseTime[9], category[9], fcstDate[9], fcstTime[9], fcstValue[9] ]
        ]
    }
    }
    )

    b=(
        {
    "error": {
        "code": 0,
        "messages": "Oh, There's someting wrong"
    }
    }
    )

    if onul in baseDate:
        return json.dumps(a)
    else:
        return json.dumps(b)

@app.route('/ex', methods = ['GET','POST'])
def index_ex_post():
    a = {
        "data": {
            "fields": [
                { "name": "DATETIME", "type": "TEXT" },
                { "name": "HOST", "type": "TEXT" },
                { "name": "FACILITY", "type": "TEXT" },
                { "name": "PRIORITY", "type": "TEXT" },
                { "name": "LEVEL", "type": "TEXT" },
                { "name": "LEVEL_INT", "type": "INTEGER" },
                { "name": "TAG", "type": "TEXT" },
                { "name": "PROGRAM", "type": "TEXT" }
            ],
            "results": [
                [ "20200403103601", "tsdn-svr1", "kern", "warning", "warning", 5, "04", "kernel" ],
                [ "20200403103601", "tsdn-svr1", "kern", "notice", "notice", 6, "05", "kernel" ],
            ]
        }
    }

    return json.dumps(a)

@app.route('/error', methods = ['GET','POST'])
def error_code():
    a = {
    "error": {
        "messages": "Oh, There is someting wrong"
    },
}

    return json.dumps(a)

@app.route('/success', methods = ['GET','POST'])
def success_code():
    a = {
    "success": {
        "messages": "OKAY"
    },
}

    return json.dumps(a)

if __name__ == '__main__':
    app.run(debug=True)