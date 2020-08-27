import logging
import time

import src.utils as utils

logging.basicConfig(level=logging.INFO)
logging.info('Select a bot')


def app(username='chiaramusina97'):
    target = "https://www.instagram.com/"
    utils.start_luminati_proxy()
    credentials = utils.export_file_credential(username)
    print(credentials)
    driver = utils.initialize_browser()
    driver.get(target)
    logging.info('start set cookie')
    driver.add_cookie({'name': 'csrftoken', 'value': credentials[4], 'domain': 'www.instagram.com'})
    driver.add_cookie({'name': 'ds_user_id', 'value': credentials[5], 'domain': 'www.instagram.com'})
    driver.add_cookie({'name': 'mid', 'value': credentials[6], 'domain': 'www.instagram.com'})
    driver.add_cookie({'name': 'rur', 'value': credentials[7], 'domain': 'www.instagram.com'})
    driver.add_cookie({'name': 'sessionid', 'value': credentials[8], 'domain': 'www.instagram.com'})
    try:
        driver.add_cookie({'name': 'ig_did', 'value': credentials[10], 'domain': 'www.instagram.com'})
        driver.add_cookie({'name': 'ig_cb', 'value': credentials[11], 'domain': 'www.instagram.com'})
    except:
        print("Old credentials without ig_did and ig_cb")
    logging.info('finish set cookie')
    logging.info('reload page')
    driver.get(target)
    time.sleep(5)
    element_to_check = driver.find_elements_by_class_name("ctQZg")
    if len(element_to_check) < 1:
        logging.info('delete all old cookies')
        driver.delete_all_cookies()
        logging.info('reload page')
        driver.get(target)
        time.sleep(5)
        driver.find_element_by_name("username").send_keys(credentials[0])
        driver.find_element_by_name("password").send_keys(credentials[1])
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)
        element_to_check = driver.find_elements_by_class_name("ctQZg")
        try:
            if len(element_to_check) >= 1:
                new_row = [credentials[0], credentials[1], credentials[2], credentials[3], driver.get_cookie('csrftoken')['value'], driver.get_cookie('ds_user_id')['value'],
                           driver.get_cookie('mid')['value'], driver.get_cookie('rur')['value'], driver.get_cookie('sessionid')['value'],
                           credentials[9], driver.get_cookie('ig_did')['value']]
                utils.update_credentials(new_row)
            else:
                logging.info('Error')
        except:
            logging.info('Assistence neeeded')
    else:
        logging.info("Credentials Ok")
    time.sleep(2)
    driver.quit()
