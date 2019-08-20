# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2019-08-09 08:57'
import time
import os
import json


class TestLog(object):

    def test_log_write(self, client):
        test_data = {
            "timestamp": str(int(time.time())),
            "message": "Hello world"
        }
        resp = client.post("/log", data=test_data)

        assert resp.status_code == 200

        base_dir = os.path.abspath(os.path.dirname(__file__))

        log_file = os.path.join(base_dir, "static", "test.log")

        with open(log_file, "r") as f:
            log_info = json.load(f)
            assert log_info["record"]["message"] == test_data
