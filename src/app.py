import logging
import src.utils as utils

logging.basicConfig(level=logging.INFO)
logging.info('Select a bot')


def app():
    utils.start_luminati_proxy()
    driver = utils.initialize_browser()
