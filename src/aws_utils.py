import logging
import os

import boto3

aws_access_key_id = None
bucket_bot_name = None
aws_secret_access_key = None
develop = False

if os.environ.get('AWS_ACCESS_KEY_ID') is not None:
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
if os.environ.get('AWS_BUCKET_BOT_NAME') is not None:
    bucket_bot_name = os.environ['AWS_BUCKET_BOT_NAME']
if os.environ.get('AWS_SECRET_ACCESS_KEY') is not None:
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
if os.environ.get('develop') is not None:
    develop = True


def download(file_name, to):
    if aws_secret_access_key is None or bucket_bot_name is None or aws_access_key_id is None:
        raise Exception("Needed environments (AWS_ACCESS_KEY_ID,AWS_BUCKET_BOT_NAME,AWS_SECRET_ACCESS_KEY)")
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


def upload_to_s3(local_path='', destination_path=''):
    try:
        logging.info('start upload to s3 {}'.format(local_path))
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        s3_client.upload_file(local_path, bucket_bot_name, destination_path)
        logging.info('finish upload to s3 {}'.format(local_path))
    except Exception as e:
        logging.error(e)
