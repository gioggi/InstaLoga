import logging
import os

import boto3

if os.environ.get('AWS_ACCESS_KEY_ID') is not None:
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
if os.environ.get('AWS_BUCKET_BOT_NAME') is not None:
    bucket_bot_name = os.environ['AWS_BUCKET_BOT_NAME']
if os.environ.get('AWS_SECRET_ACCESS_KEY') is not None:
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
if os.environ.get('develop') is not None:
    develop = True
else:
    develop = False


def download(file_name, to):
    if develop:
        logging.info("bella la figa")
    else:
        logging.info("brutta  la figa")

    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        logging.info("start download file  " + file_name)
        s3_client.download_file(bucket_bot_name, file_name, to)
        logging.info("finish download file " + file_name)
    except Exception as e:
        logging.error(e)
