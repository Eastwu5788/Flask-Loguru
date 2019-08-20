# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2019-08-09 08:52'
import os
import pytest
from flask import Flask
from flask import request

from flask_loguru import Logger
from flask_loguru import logger


def clear_logs():
    """ 情况logs文件夹下的所有文件
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.join(base_dir, "static")

    # 处理文件夹缺失情况
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    list_dir = os.listdir(base_dir)
    for f in list_dir:
        c_path = os.path.join(base_dir, f)
        os.remove(c_path)


clear_logs()

app = Flask(__name__)

app.config["LOG_PATH"] = "./tests/static"
app.config["LOG_NAME"] = "test.log"
app.config["LOG_ROTATION"] = 1

log = Logger()
log.init_app(app)


@app.route("/log", methods=["POST"])
def test_handler():
    param = request.form.to_dict()
    logger.info(param)
    return ""


@pytest.fixture
def client():
    """ 构建测试实例
    """
    app.config["TESTING"] = True
    return app.test_client()



