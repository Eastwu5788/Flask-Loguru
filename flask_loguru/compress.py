# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2019-08-09 12:29'
# sys
import datetime
import os
import zipfile

# project
from .macro import k_log_name, k_log_path


def zip_logs(config, file_list):
    """ 超过7天的文件按天打成zip包
    """
    day = datetime.datetime.today().date() - datetime.timedelta(days=7)

    # 设置zip位置
    zip_name = config[k_log_name] + str(day) + ".zip"

    # 启动zip写入对象
    zp = zipfile.ZipFile(os.path.join(config[k_log_path], zip_name), "w")
    for tar in file_list:
        zp.write(tar, os.path.basename(tar))

    zp.close()

    for tar in file_list:
        os.remove(tar)
