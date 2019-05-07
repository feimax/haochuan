# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pic import Download
from msg import Msg

if __name__ == '__main__':

    # 这里要填写从 人工智能AIST 公众号里获取的下载密钥。
    # 首先您需要是图片收集任务的发起人，才可以获取到下载密钥。
    dn = Download('PC80000000')

    # 获取该图片收集任务的图片列表，包含图片在云端的名称，数据大小和贡献者的wx_openid
    print(dn.ls())
    # 获取该图片收集任务的图片列表，包含
    dn.ls('1.csv')

    # 下载所有的图片文件到 test 文件夹下去
    dn.all('test')

    # 这里要填写从 人工智能AIST 公众号里获取的数据通道的密钥。
    # 您需要练习 人工智能AIST 公众号来获取该项功能。
    msg = Msg('MS0000000')

    # push 方法直接将您想得到的信息直接通过我们的微信公众号推送给您。但是这种方法有两个限制：
    # 1、每天的推送不能超过1500条，请仅仅推送重要的信息。
    # 2、微信只允许在48小时之内发过信息给公众号的用户接受到公众号的推送。
    #    也就是说，如果您超过48小时没有给我们的公众号发送过任何信息，我们将没有权限推送信息给您。
    #    所以，为了确保您的使用，请经常发信息给公众号。
    print(msg.push('这是一条推送信息'))

    # put 方法是将数据或者信息暂存，然后您任何时间都可以到我们的 人工智能AIST 公众号里去查询。
    # 这种方法暂时没有条数限制，如果不是重要的信息，最好使用该方法。该方法同时会帮你记录数据暂存的时间，使用GMT标准时间。请自行换算时区
    print(msg.put('这是一条正常信息'))

