import json, urllib
from urllib import parse
from urllib import request

#全部开放基金
def adk_fund_data_req_all(m="GET"):

    url = "http://web.juhe.cn:8080/fund/netdata/all"

    params = {
        "key" : 'bbc9749b5402705326c0c687b209b796', #APPKEY值
    }
    params = parse.urlencode(params)

    if m =="GET":

    	f = request.urlopen("%s?%s" % (url, params))
    else:
        f = request.urlopen(url, params)
 
    content = f.read()

    # 返回dict类型
    res = json.loads(content)

   
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print ("请求成功")
            return res
        else:
            print ("%s:%s" % (res["error_code"],res["reason"]))
            return -1
    else:
        print ("request api error")
        return -1
    
# 解析数据包, 并把基金编号和基金代码映射到一个dict中
def adk_fund_id_code_map(res):

    # res是dict类型, [key, value]
    # dict_keys(['resultcode', 'reason', 'result', 'error_code'])

    # res["result"]是list类型, 里面只有一个dict元素,fund_data_all[0]
    fund_data_all = res["result"]
    #print(type(fund_data_all))
    #print(fund_data_all)
    
    # fund_data_all[0], dict_key = ['1', ..., '6129'], 1 - 6129为基金编号
    #print(type(fund_data_all[0]))
    #print(fund_data_all[0].keys())
    #print(len(fund_data_all[0]))


    # 记录基金编号,并与基金代码进行映射<key, value> = <code, id>
    fund_dict = {}
    
    for i in fund_data_all[0]:

       	fund_dict[fund_data_all[0][i]["code"]] = i
       
    #print(fund_dict)
   
    # fund_data_all[0]里有6129个dict类型, 例如fund_list[0]["1"]
    # print(type(fund_data_all[0]["1"]))
    # print(fund_data_all[0]["1"])
    # print(fund_data_all[0]["1"].keys())
    # dict_keys(['code', 'name', 'newnet', 'totalnet', 'dayincrease', 'daygrowrate',  
    #            'weekgrowrate', 'monthgrowrate', 'annualincome', 'time'])
    #
    # "code"          : 基金代码
    # "name"          : 基金名称
    # "newnet"        : 当前净值
    # "totalnet"      : 累计净值
    # "dayincrease"   : 日增幅
    # "daygrowrate"   : 日增长率
    # "weekgrowrate"  : 周增长率
    # "monthgrowrate" : 月增长率
    # "annualicome"   : 年收入
    # "time"          : 净值日期
