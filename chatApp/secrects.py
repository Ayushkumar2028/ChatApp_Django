import boto3
import json
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "rds!cluster-a0785ecf-ab92-4352-97f0-72b1ba275b42"
    region_name = "eu-north-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
