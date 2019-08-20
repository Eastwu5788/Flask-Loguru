# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
__author__ = 'Wu Dong <wudong@eastwu.cn>'
__time__ = '2019-04-19 10:52'
import os
from flask import Flask
from flask import request

from flask_loguru import Logger
from flask_loguru import logger


def clear_logs():
    """ 情况logs文件夹下的所有文件
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.join(os.path.dirname(base_dir), "tests")
    list_dir = os.listdir(os.path.join(base_dir, "static"))
    for f in list_dir:
        c_path = os.path.join(base_dir, "static", f)
        os.remove(c_path)


app = Flask(__name__)

app.config["LOG_PATH"] = "./static"
app.config["LOG_NAME"] = "test.log"
app.config["LOG_ROTATION"] = 2

log = Logger()
log.init_app(app)


@app.route("/log", methods=["POST"])
def test_handler():
    param = request.form.to_dict()
    logger.info(param)
    return ""


if __name__ == "__main__":
    app.run(port=14890)
