SDK Version: 5.x 6.x
# 代码拷贝自twilio官网sdk
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python

# 为什么是from xxx import xxx ，可不可以直接import xxx？
# 用pip安装完twilio后，twilio存在于 python/lib/site-packages/twilio中
# t有一个rest文件夹，rest文件夹中有一个python文件，python文件内有一个Client的类
# 这里导入的不是一整个模块，而仅仅是模块中的一个类
from twilio.rest import Client

# 当下面调用rest.client（aa）这个类的时候，实际上在调用一个..init..的函数，这个函数会自动填进去初始配置

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12316851234",
    from_="+15555555555",
    body="Hello there!")