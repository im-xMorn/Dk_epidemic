import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import urllib3
# 关闭请求警告报错
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def Dk_auto(Bearer):
    url = 'https://sac.cqvie.edu.cn/schoolapi//api-prevention/signinfo/savebatch'
    headers = {
        'content-type': 'application/json',
        'Authorization': Bearer,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    data = {"isTravel": 0, "isContact": 0, "isCohabit": 0, "isFatigue": 0, "isShortnessBreath": 0,
            "travelInfoVo": {"relationshipInfo": [{"contactInfo": "", "name": "", "relationship": "", "key": 0}]},
            "contactInfo": {}, "cohabitInfo": [
            {"name": "", "province,city,disctrict": "", "returnTime": "", "transType": "", "transTypeValue": "",
            "transNumber": "", "currentDetailResidence": "", "contactInfo": 0, "highRiskInfo": 0,
            "governmentQuarantine": 0, "homeQuarantine": 0, "healthCardInfo": "", "healthCardUrl": "", "travelInfo": "",
            "travelUrl": "", "nucleicAcid": "", "nucleicAcidMethod": "", "nucleicAcidPointName": "",
            "nucleicAcidSamplingDate": "", "nucleicAcidAgency": "", "nucleicAcidTime": "", "nucleicAcidResult": "",
            "nucleicAcidImg": "", "key": 0}], "healthCardInfo": 0, "healthStatus": 0, "travelInfo": 0,
            "locateDetailedAddress": "重庆工程职业技术学院江津校区-第一教学楼", "locateLatitude": 29.346417, "locateLongitude": 106.25855,
            "city": "重庆市", "disctrict": "江津区", "cityCode": "023", "disctrictCode": "500116", "province": "重庆市"}
    data = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=data).text
    if response[13:16] == '401':
        return '令牌已过期!请及时更换!'
    else:
        print(response)
        return '今日已打卡'
if __name__=='__main__':
    Bearer = '01302218-7ba7-43d0-a125-dce8dab7b96b'
    Begin = Dk_auto(Bearer)
    print(Begin)

"""
    返回字段值
"""
# token-Bearer字段 已过期
# {"resp_code":401,"resp_msg":"Invalid access token: 82ae0853-5ca7-4248-97ae-8669949bae5d"}

# 今日已打卡
# {"data":null,"code":-1,"msg":"今日已打卡"}

# 不在打卡时间段
# {"data":null,"code":-1,"msg":"不在打卡时段。"}
