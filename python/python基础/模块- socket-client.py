# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-03 17:26   #2024/10/3 17:26
@File：模块- socket-client.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import socket
# 创建socket对象
sk = socket.socket()
# 连接服务器
sk.connect(('127.0.0.1', 8999))
while True:
    socket_data = input('请输入您要发送的内容：').encode('utf-8')
    if socket_data is not None:
        # 发送数据到服务器
        sk.send(socket_data)
        # 等待服务器响应
        accept_data = sk.recv(1024).decode('utf-8')
        print(accept_data)
