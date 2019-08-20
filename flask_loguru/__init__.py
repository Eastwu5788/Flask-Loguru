# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
__author__ = 'Wu Dong <wudong@eastwu.cn>'
__time__ = '2019-04-19 10:52'
# sys
import os
import time

# 3p
from loguru import logger

# project
from .compress import zip_logs
from .macro import k_log_path, k_log_name, k_log_enqueue, k_log_format
from .macro import k_log_rotation, k_log_serialize


class Logger(object):
    """This class is used to config loguru
    """

    def __init__(self, app=None, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        self.config = config

        if app is not None:
            self.init_app(app, config)

    def init_app(self, app, config=None):
        """This is used to initialize logger with your app object
        """
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        base_config = app.config.copy()
        if self.config:
            base_config.update(self.config)
        if config:
            base_config.update(config)

        config = base_config

        config.setdefault(k_log_path, None)
        config.setdefault(k_log_name, "")
        config.setdefault(k_log_rotation, 60 * 60)
        config.setdefault(k_log_format, "")
        config.setdefault(k_log_enqueue, True)
        config.setdefault(k_log_serialize, True)

        self._set_loguru(app, config)

    def _set_loguru(self, app, config):
        """ Config logru
        """
        path = config[k_log_name]
        if config[k_log_path] is not None:
            path = os.path.join(config[k_log_path], config[k_log_name])

        def should_rotate(message, file):
            filepath = os.path.abspath(file.name)
            creation = os.path.getctime(filepath)
            now = message.record["time"].timestamp()
            return now - creation > config[k_log_rotation]

        def should_retention(logs):
            """ 检查是否需要进行压缩
            """
            # 依次查找写入
            file_list = list()
            for log in logs:
                file_path = os.path.abspath(log)

                if file_path.endswith(".zip"):
                    continue

                if time.gmtime(time.time() - os.path.getctime(file_path)).tm_mday == 7:
                    file_list.append(file_path)

            if file_list:
                zip_logs(config, file_list)

        logger.add(path, format=config[k_log_format], rotation=should_rotate,
                   enqueue=config[k_log_enqueue], serialize=config[k_log_serialize],
                   retention=should_retention)

        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions.setdefault("loguru", {})
        app.extensions["loguru"][self] = logger
