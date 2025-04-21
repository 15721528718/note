# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-18 18:51   #2025/4/18 18:51
@File：flask2.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from flask import Flask,request,jsonify,render_template
from jinja2.ext import debug

app = Flask(__name__)
app.debug = True

# 访问注册页面
@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        hobby = request.form.getlist('hobby')
        print(name)
        print(pwd)
        print(hobby)
        print(request.form)
        # print(request.json)
        return "注册成功"
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        name = request.args.get('username')
        pwd = request.args.get('password')
        print(name)
        print(pwd)
        return "登录成功"

if __name__ == '__main__':
    app.run(host='192.170.1.206',port=5000,debug=True)