import json

import requests

from PCCR.settings import APPID, SECRET


def get_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(APPID
                                                                                                           ,SECRET)
    respon = requests.get(url)
    content = respon.content

    content = content.decode('utf-8')
    data = json.loads(content)
    return data.get("access_token")