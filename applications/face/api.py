#!encoding:utf-8
import json
import urllib
import urllib2


def AuthService():
    """百度AI人脸识别认证获取token"""
    # 获取token地址
    authHost = "https://aip.baidubce.com/oauth/2.0/token?"
    # 官网获取的 API Key
    clientId = "Hctr9LPRKplAcz0nWo8HEs2H"
    # 官网获取的 Secret Key
    clientSecret = "BgK8ZWG2T47MLUEcF3aA4OiMrxK8TRhr"
    getAccessTokenUrl = authHost + "grant_type=client_credentials" + "&client_id=" + clientId + "&client_secret=" + clientSecret
    request = urllib2.Request(getAccessTokenUrl)
    response_data = urllib2.urlopen(request)
    params = json.loads(response_data.read())
    return params["access_token"]


def Detect(image):
    detectUrl = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
    params = {"max_face_num": 1,
              "face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
              "image": image}
    params = urllib.urlencode(params)
    access_token = AuthService()
    detectUrl = detectUrl + "?access_token=" + access_token
    request = urllib2.Request(url=detectUrl, data=params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    content = json.loads(content)
    try:
        num = content['result'][0]['race_probability']
        return True
    except:
        return False
