import urllib.request
import time
import json
import random
import hashlib
import urllib.parse
 
 
 
class LookUpTheWord_baidu():
    def do_word(self,word):
        # 做查询操作
        url = "https://fanyi.baidu.com/sug"
                    
        formdata = {
            'kw':word,
        }

        data = urllib.parse.urlencode(formdata).encode()
        # 给服务器发送post请求
                    
        # 构造headers
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept-Language":"zh-CN,zh;q=0.9",
                    "Accept - Encoding": "gzip, deflate, br",
                    "Content-Length": len(data),
                    "Cookie":"BAIDUID=2BBF51781FE3905BF27FE07204103174:FG=1; BIDUPSID=2BBF51781FE3905BF27FE07204103174; PSTM=1552104392; pgv_pvi=6709946368; delPer=0; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1432_21120_18559_28768_28724_28964_28837_28585_26350_28604; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1557369112; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1557369112; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
                    "Connection":"keep-alive",
                    "Accept":"application/json, text/javascript, */*; q=0.01",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host":"fanyi.baidu.com",
                    "Referer":"https://fanyi.baidu.com/?aldtype=16047",
                    "Origin": "https://fanyi.baidu.com"
                    }
                    
        req = urllib.request.Request(url,
                                    data,
                                    headers,
                                    method="POST")

        response = urllib.request.urlopen(req)
        info = response.read().decode("utf-8")

        # json decode: json str --> dict
        jsonLoads = json.loads(info)
        res = ''
        try:
            resu = jsonLoads['data'][0]
            res += resu['v']
        except:
            res += word
        finally:
            return res

