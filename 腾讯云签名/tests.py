from django.test import TestCase

# Create your tests here.

# from rest_framework import serializers
# from individual.models import *
#
#
# class AvailableSerializer(serializers.ModelSerializer):
#     time = serializers.CharField(source='preabout.time')
#
#     class Meta:
#         model = Available
#         fields = ("date", "time")
#
#
# class ApplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apply
#         fields = ("id", "name", "creation_time", "date_birth", "mobile_phone")
#
#
# # 预约员 待咨询
# class WxuserSerializer(serializers.ModelSerializer):
#     # Apply表的 id  name  creation_time   date_birth  mobile_phone
#     apply = ApplySerializer()
#     # id = serializers.CharField(source='apply.id', read_only=True)
#     # apply_name = serializers.CharField(source='apply.name', read_only=True)
#     # creation_time = serializers.CharField(source='apply.creation_time', read_only=True)
#     # date_birth = serializers.CharField(source='apply.date_birth', read_only=True)
#     # mobile_phone = serializers.CharField(source='apply.mobile_phone', read_only=True)
#     # user表里面的 name
#     user_name = serializers.CharField(source='user.name', read_only=True)
#     # Available表里面的 date  Preabout表里的time
#     ava = AvailableSerializer()
#     # date = serializers.DateField(source='available.date', read_only=True)
#     # time = serializers.CharField(source='available.time', read_only=True)
#     # review 表里的 status
#     review_status = serializers.IntegerField(source="review.status", read_only=True)
#
#     class Meta:
#         model = Wxuser
#         fields = ('apply', 'ava', 'user_name', 'order_status', 'openid', "review_status")


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# import requests
# import sys
# import json
# import hashlib
# import time
# import base64
# import hmac
# import random
#
#
# class Qcloud(object):
#     def __init__(self, config, Id, key):
#         self.config = config
#         self.url = 'https://cdn.api.qcloud.com/v2/index.php'
#         self.id = ''
#         self.Key = ''
#
#     def Auth(self):
#         data = {}
#         Singna = []
#         Random = range(1000000)
#         number = random.choice(Random)
#         data['SecretId'] = self.id
#         data['Nonce'] = number
#         data['Timestamp'] = int(time.time())
#         data = dict(data, **self.config)
#         base = sorted(data.items(), key=lambda data: data[0])
#         for i in base:
#             Singna.append(str(i[0]) + '=' + str(i[1]) + '&')  # end='')
#             result = 'POSTcdn.api.qcloud.com/v2/index.php?' + ''.join(Singna).rstrip('&')
#         self.Key = self.Key.encode(encoding='utf-8')
#         result = result.encode(encoding='utf-8')
#         uri = hmac.new(self.Key, result, digestmod=hashlib.sha1).digest()
#         key = base64.b64encode(uri)
#         data['Signature'] = key
#         return data
#
#
# if __name__ == '__main__':
#     config = {
#         'Action': 'DescribeCdnHosts', 'detail': '1'}
#     res = Qcloud(config, 'access_key', 'securt_key')
#     data = res.Auth()
#     html = requests.post(res.url, data=data)
#     print(json.loads(html.text))

#
import hashlib, hmac, json, os, sys, time
from datetime import datetime
#
# # 密钥参数
# secret_id = "AKIDQlJlxsl9SUJr88hQh6EJ2VkjeJhpbZ1C "
# secret_key = "9dvxkIkywdhFZyYBblgLPFrCqFOIvKZZ"
#
# service = "cvm"
# host = "cvm.tencentcloudapi.com"
# endpoint = "https://" + host
# region = "ap-guangzhou"
# action = "DescribeInstances"
# version = "2020-02-24"
# algorithm = "TC3-HMAC-SHA256"
# # timestamp = int(time.time())
# timestamp = 1551113065
# date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
# params = {"Limit": 1, "Filters": [{"Name": "instance-name", "Values": [u"未命名"]}]}
#
# # ************* 步骤 1：拼接规范请求串 *************
# http_request_method = "POST"
# canonical_uri = "/"
# canonical_querystring = ""
# ct = "application/json; charset=utf-8"
# payload = json.dumps(params)
# canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
# signed_headers = "content-type;host"
# hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
# canonical_request = (http_request_method + "\n" +
#                      canonical_uri + "\n" +
#                      canonical_querystring + "\n" +
#                      canonical_headers + "\n" +
#                      signed_headers + "\n" +
#                      hashed_request_payload)
# print(canonical_request)
#
# # ************* 步骤 2：拼接待签名字符串 *************
# credential_scope = date + "/" + service + "/" + "tc3_request"
# hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
# string_to_sign = (algorithm + "\n" +
#                   str(timestamp) + "\n" +
#                   credential_scope + "\n" +
#                   hashed_canonical_request)
# print(string_to_sign)
#
#
# # ************* 步骤 3：计算签名 *************
# # 计算签名摘要函数
# def sign(key, msg):
#     return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
#
#
# secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
# secret_service = sign(secret_date, service)
# secret_signing = sign(secret_service, "tc3_request")
# signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
# print(signature)
#
# # ************* 步骤 4：拼接 Authorization *************
# authorization = (algorithm + " " +
#                  "Credential=" + secret_id + "/" + credential_scope + ", " +
#                  "SignedHeaders=" + signed_headers + ", " +
#                  "Signature=" + signature)
# print(authorization)
#
# print('curl -X POST ' + endpoint
#       + ' -H "Authorization: ' + authorization + '"'
#       + ' -H "Content-Type: application/json; charset=utf-8"'
#       + ' -H "Host: ' + host + '"'
#       + ' -H "X-TC-Action: ' + action + '"'
#       + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
#       + ' -H "X-TC-Version: ' + version + '"'
#       + ' -H "X-TC-Region: ' + region + '"'
#       + " -d '" + payload + "'")

import base64
import hashlib
import hmac
import time

import requests

secret_id = "AKIDMTK0SjCarztX2KSVN0TeaIm8HAzjeYga "
secret_key = "ylIUJuFKNCm6OSIsFOM6jSwCCOO0OoCV"

import random


def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    sorted(s)
    print(s)
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str


def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)


if __name__ == '__main__':
    endpoint = "cvm.tencentcloudapi.com"
    data = {
        'Action': 'DescribeInstances',
        'InstanceIds.0': 'ins-85uer78h',
        'Limit': 20,
        'Nonce': random.randint(10000, 99999),
        'Offset': 0,
        'Region': 'ap-beijing',
        'SecretId': 'AKIDMTK0SjCarztX2KSVN0TeaIm8HAzjeYga',
        'Timestamp': int(time.time()),
        'Version': '2017-03-12'
    }
    Timestamp = int(time.time())
    print(Timestamp)
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    print(data)
    print(data["Signature"])
    print(s)
    print(endpoint)
    # 此处会实际调用，成功后可能产生计费
    resp = requests.get("https://" + endpoint, params=data)
    print(resp.url)

