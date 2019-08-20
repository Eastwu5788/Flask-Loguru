FROM python:3.6

MAINTAINER LeonardWoo <wudong@eastwu.cn>

VOLUME [ "/data" ]

WORKDIR /data

COPY . /data

RUN pip install -r requirements.test.txt

CMD ["/bin/bash"]
