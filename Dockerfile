FROM python:3.7
LABEL maintainer="gioggi.net"

# download luminati proxy
RUN curl -L https://luminati.io/static/lpm/luminati-proxy-latest-setup.sh | bash

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#install all in tmp
WORKDIR /tmp
RUN mkdir app
WORKDIR ./app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#call alwasy lambda function
ENTRYPOINT ["python","./lambda_function.py"]