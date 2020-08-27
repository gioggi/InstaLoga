import logging
import sys

from src.app import app

logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    logging.info("Starting")
    app(event['username'])
    logging.info('finish')


if __name__ == '__main__':
    event = []
    username = sys.argv[1]
    event = {
        "username": username
    }
    lambda_handler(event, {})
