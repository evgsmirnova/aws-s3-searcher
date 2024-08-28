import loggers
import boto3
from config import Config
from botocore.exceptions import ClientError
client = boto3.client('s3')
paginator = client.get_paginator('list_objects_v2')


def get_object_list(config: Config) -> list:
    """using paginator searches for keys in list_objects_v2 output that are equal to extention_name given in config.json, returns list of found filepathes"""
    loggers.logging.info("Searching for files on AWS")
    try:
        s3_page_iterator = paginator.paginate(Bucket=config.bucket_name, Prefix=config.prefix_name)
        res = []
        for page in s3_page_iterator:
            for key in page['Contents']:
                res.append(key)
    except ClientError as e:
        loggers.logging.error(e)
        exit()

    res = [f"s3://{config.bucket_name}/{key['Key']}" for key in res if
           key['Key'].endswith(config.extension_name)]
    return res
