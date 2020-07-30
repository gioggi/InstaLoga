import logging
import time

import src.utils as utils

logging.basicConfig(level=logging.INFO)
logging.info('Select a bot')


def app(username='massimiliano_parco', password='Donatello12'):
    utils.start_luminati_proxy()
    driver = utils.initialize_browser()
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(40)
    driver.close()
