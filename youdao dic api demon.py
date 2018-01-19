# /usr/bin/env python
# coding=utf8

import http.client
import hashlib
import urllib
import random
import sys

appKey = '6286b0511003c804'
secretKey = 'OyTpxnhmhEEgvXctb2KBBcIHrF9EVa2B'

httpClient = None
myurl = '/api'
q = 'I love you'
fromLang = 'EN'
toLang = 'zh-CHS'
salt = random.randint(1, 65536)



sign = appKey + q + str(salt) + secretKey
sign1 = sign.encode("utf8")
m1 = hashlib.md5()
m1.update(sign1)
sign = m1.hexdigest()
myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()

    response_output = response.read()

    response_output_decode = response_output.decode("utf-8")
    print (response_output_decode)
# except Exception, e:
#     print
#     e
finally:
    if httpClient:
        httpClient.close()