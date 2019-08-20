# Flask-loguru
[![Build Status](https://travis-ci.org/Eastwu5788/Flask-Loguru.svg?branch=master)](https://travis-ci.org/Eastwu5788/Flask-Loguru)  
[![Coverage Status](https://coveralls.io/repos/github/Eastwu5788/Flask-Loguru/badge.svg?branch=master)](https://coveralls.io/github/Eastwu5788/Flask-Loguru?branch=master)  
将loguru改造成flask扩展

#### 安装方式
```bash
python setup.py install

或者

pip install flask-loguru
```

#### 配置参数介绍
| 参数 | 介绍 | 实例 |
| :---: | :---:| :---: |
|  LOG_PATH | log输出路径 | /home/work/log/web |
|  LOG_NAME | log输出的文件名称 | run.log |
|  LOG_FORMAT | log输出格式 | {time:YYYY-MM-DD at HH:mm:ss} | {level} | {message} |
|  LOG_ROTATION | log文件翻转时间（秒） | 3600  |

#### 扩展安装方式
```python
from flask import Flask
from flask_loguru import Logger

app = Flask(__name__)

log = Logger()

log.init_app(app, {
    "LOG_PATH": "/home/work/www/log",
    "LOG_NAME": "run.log"
})
```

#### 使用方法
```python
from flask_loguru import logger

logger.critical("Critical Hello world")

logger.error("Fail Hello world")

logger.warning("Warning Hello world")

logger.info("Info Hello world")

logger.debug("Debug Hello world")
```


