import json
import boto3

def get_email_config():
    secret_name = "Morfin_Landscaping/emailConfig"
    region_name = "us-west-2"

    client = boto3.client("secretsmanager", region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])

    return secret["senderEmail"], secret["gatewayAddress"], secret["appKey"]

senderEmail, gatewayAddress, appKey = get_email_config()