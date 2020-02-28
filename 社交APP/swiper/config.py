'''业务配置以及第三方平台的配置'''


REWIND_TIMES = 3


# 云资讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_PARAMS = {
    "sid": 'fa6b4d3c19fa56f251630a5c8ae7ef6d',
    "token": '0fa9ccb35e01af1b76a8611af1fa9003',
    "appid": 'f8355a3257054c8d9675da2b914225c1',
    "templateid": "490497",
    "param": None,
    "mobile": None,
}


# 七牛云配置
QN_URL_PREFIX = 'http://pvi7xomg5.bkt.clouddn.com'
QN_ACCESS_KEY = '83heu5Lfycpd0WjQrATvY12xlQQwmxaFcj8HRwca'
QN_SECRET_KEY = 'kuEQkudF-iVjybBMlsKM01pS4rNWtVYJl7PfslIJ'
QN_BUCKET = 'seven'
