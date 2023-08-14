# Using Python image
# （後で調べたらDebianでした。）
FROM --platform=linux/amd64 python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/google/chrome



# Install jp fonts
RUN apt-get install -y --no-install-recommends \
    fonts-noto-cjk \
    fonts-noto-cjk-extra 

# install requirements
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# 環境用意あとは、起動しっぱなし。execで入れるようにする
RUN echo "running! scraping!"