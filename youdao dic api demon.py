# /usr/bin/env python
# coding=utf8

import http.client
import hashlib
import urllib
import random
import sys

def read_text():
    # 实例化----使用open函数（函数是不依托于类的，方法是在类中的函数，并且open太常用是built-in函数，意思是自带函数） 创建一个file对象quotes，之后的操作可以利用file类下的各种方法，
    # 字符串中的r 排除转意符
    quotes = open(r"J:\2018.1编程学习\udacity python 印度小哥\第二章，使用函数\movie_quotes")
    # 任何抽象的储存空间都要有一个 变量来储存，
    # 我第一次操作的时候没有给 quotes.read（）赋予变量
    content_of_file = quotes.read()
    print(content_of_file)
    # 养成好习惯，最后关闭文件
    # quotes.close()



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
    # 我认为增加了encode和decode环节
    response_output_decode = response_output.decode("utf-8")
    print (response_output_decode)
# except Exception, e:
#     print
#     e
finally:
    if httpClient:
        httpClient.close()