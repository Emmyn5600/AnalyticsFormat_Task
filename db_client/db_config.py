from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb",
                    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
                    region_name=getenv("REGION_NAME"))


tables = [
    {
        "TableName": "annualFootprint",
        "KeySchema": [
            {
                'AttributeName': 'startYear',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'dashboard_id',
                'KeyType': 'RANGE'
            },

        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'startYear',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'dashboard_id',
                'AttributeType': 'S'
            }
           
        ],
    },
]



def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)
