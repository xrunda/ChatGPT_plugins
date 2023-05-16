import requests;
import json;
import sys;
# 测试程序，接受1个参数，
# 参数 m 月份
month=sys.argv[1];

# 设置请求头
headers={
    "Content-Type":"application/json"
}
data={
    "month":month
}
# 发送post请求
requests=requests.post("http://127.0.0.1:5003/tslSD",headers=headers,data=json.dumps(data));