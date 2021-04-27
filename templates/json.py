import requests
import json
# GET
res = requests.get('http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=GdWTDEeLjnO0YeiW5E4occlcHvqg03IlkDh5FCkW/JpS4g1l2idd09uocu8pLVYvNBp3GL0qvikxil85BaJy4A==&numOfRows=10&pageNo=1&base_date=20210427&base_time=0230&nx=55&ny=127&dataType=JSON')
print(res.status_code)
print(res.text)
