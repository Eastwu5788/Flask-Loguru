# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2019-08-09 12:21'
import os
import time


class TestRotate(object):

    def test_log_rotate(self, client):
        """ 测试文件翻转
        """
        time.sleep(2)

        # 重新检查一遍文件写入
        test_data = {
            "timestamp": str(int(time.time())),
            "message": "Hello world"
        }
        resp = client.post("/log", data=test_data)

        assert resp.status_code == 200

        time.sleep(2)

        # 检查翻转文件
        log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static")
        list_dir = os.listdir(log_dir)

        assert len(list_dir) > 1
