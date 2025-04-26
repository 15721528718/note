# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-18 13:16   #2025/4/18 13:16
@File：flask.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from flask import Flask,request,jsonify,render_template
app = Flask(__name__)
app.debug = True
# /index.html?age=18
@app.route('/index.html',methods=['GET','POST'])
def index():
    # 获取get方法传入的参数
    # age = request.args.get('age')

    # 获取post方法传入form格式的参数
    # xx = request.form.get('x')

    # 获取post方法传入json格式的参数
    # yy = request.json

    # return jsonify({"nihao":112})
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='192.170.1.206', port=5000, debug=True)








