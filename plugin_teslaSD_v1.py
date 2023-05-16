import json
import numpy as np
import quart
import quart_cors
from quart import request


app = quart_cors.cors(quart.Quart(__name__))

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS = {}

@app.post("/tslSD")
async def get_teslasaledata():
    request = await quart.request.get_json(force=True)
    tslSD=np.array([0,184000,185000,187000,189000,191000,192000,195000,344000,346000,348000,388888,399999]);
    # print(month_check(check_content("January")))
    # print(request["month"])
    # return quart.Response(response=tslSD[month_check(check_content(request["month"]))],status=200)
    print("request>>>>>>>>>>>>",request)
    returnData=tslSD[month_check(check_content(request["month"]))];
    
    # print("returnData:",returnData)
    
    
    
    return quart.Response(response=str(returnData),status=200)
    # return quart.Response(status=200);

    # for m in months:
        # num+=1;
        # if m == request["month"]:
            # return quart.Response(response= str(tslSD[num]), status=200)
            
    # print("get_tslsd:month=",tslSD[request["month"]]);
    # print(tslSD[int(request["month"])])
    # print(getattr(obj,request["month"]))
    # return quart.Response(response= str(tslSD[int(request["month"])]), status=200)
    # return quart.Response(response= str(months), status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("manifest.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

# 定义一个月份字典
month_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
# 定义一个月份检测函数
def month_check(content):
    # 判断参数的类型
    if isinstance(content, int):
        # 如果是整数，直接返回该数字
        return content
    elif isinstance(content, str):
        # 如果是字符串，查找字典中是否有对应的键
        if content in month_dict:
            # 如果有，返回对应的值
            return month_dict[content]
        else:
            # 如果没有，返回一个错误信息
            return 0
    else:
        # 如果不是整数或字符串，返回一个错误信息
        return 0

# 定义一个月份检测函数
# 定义一个函数
def check_content(content):
    # 判断参数的类型
    if isinstance(content, (int, float)):
        # 如果是数字，直接返回该数字
        return content
    elif isinstance(content, str):
        # 如果是字符串，用 isdigit() 方法来判断字符串内容是否是纯数字
        if content.isdigit():
            # 如果是纯数字，用 int() 函数来转换为数字并返回
            return int(content)
        else:
            # 如果不是纯数字，则返回该字符串
            return content
    else:
        # 如果不是数字或字符串，返回一个错误信息
        return 0


def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
    
