# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2024-10-03 16:34   #2024/10/3 16:34
@File：模块-socket.PY
@IDE：PyCharm
@Motto：南风知我意
"""
import socket
# 创建socket对象
sk = socket.socket()
# 绑定ip和端口号
sk.bind(('0.0.0.0', 8999))
# 设置监听
sk.listen(5)
# 等待客户端连接
conn,addr = sk.accept()
while True:
    # 接收客户端发送的信息
    accept_data = conn.recv(1024).decode('utf-8')
    if accept_data is not None:
        print(f'接收到客户端发送的信息："{accept_data}"')
        # 回复客户端收到信息
        send_data = f'我是服务器，我收到了你发给我的“{accept_data}”'
        conn.send(send_data.encode('utf-8'))