import requests

from background.access_token import get_token
from individual.models import Order


def getWXACode():
    access_token = get_token()
    print(access_token)
    if not access_token:
        pass
    else:
        url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token={}'.format(access_token)
        data = {"path": "pages/chargeDetail/chargeDetail?id=24",  # todo 传参
                "width": 1280,
                "auto_color": False,
                "line_color": {"r": 133, "g": 218, "b": 70},  # 自定义颜色 auto_color 为 false 时生效
                # "line_color": {"r": 233, "g": 195, "b": 65},  # 自定义颜色
                "is_hyaline": True , # 是否需要透明底色
                }
        # todo 不能使用data 要使用json
        # ret = requests.post(url, json=data)
        ret = requests.post(url, json=data)

        # print(ret.text)
        print(ret.content)
        with open('getWXACode.png', 'wb') as f:
            f.write(ret.content)