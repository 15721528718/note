# -*- coding: utf-8 -*-
"""
@Auth：bee
@Time：2025-04-22 18:48   #2025/4/22 18:48
@File：flask3.PY
@IDE：PyCharm
@Motto：南风知我意
"""
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
app.debug = True

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('')