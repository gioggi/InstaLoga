import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

from src.aws_utils import download


def is_development() -> bool:
    import json
    with open('envs.json') as json_file:
        data = json.load(json_file)
        if data['environment'] is not None:
            if data['environment'] == "production" or data['environment'] == 'test':
                return False
            else:
                return True
        else:
            raise Exception("Envs must contain environment var")


def start_luminati_proxy():
    if is_development():
        logging.info('Manual launch luminati proxy')
    else:
        os.system('[ -e ~/luminati_proxy_manager/.luminati.json ] && rm ~/luminati_proxy_manager/.luminati.json')
        os.system('[ -e ~/luminati_proxy_manager/.luminati.json.backup ] && rm '
                  '~/luminati_proxy_manager/.luminati.json.backup')
        download("configFile/luminati.json", "/root/luminati_proxy_manager/.luminati.json")
        download("configFile/luminati.json.backup", "/root/luminati_proxy_manager/.luminati.json.backup")
        time.sleep(3)
        os.system('luminati --daemon')


def initialize_browser() -> object:
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    proxy_url = "127.0.0.1:24001"
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_url
    proxy.ssl_proxy = proxy_url
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)
    if is_development():
        return webdriver.Chrome('./bin/chromedriver.exe', chrome_options=chrome_options,
                                desired_capabilities=capabilities)
    else:
        chrome_options.add_argument('--data-path=/tmp/data-path')
        chrome_options.add_argument('--homedir=/tmp')
        chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        return webdriver.Chrome(chrome_options=chrome_options,desired_capabilities=capabilities)


