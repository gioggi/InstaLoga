import logging
from src.app import app

logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    logging.info("Starting")
    app()
    logging.info('finish')


if __name__ == '__main__':
    event = []
    lambda_handler(event, {})
