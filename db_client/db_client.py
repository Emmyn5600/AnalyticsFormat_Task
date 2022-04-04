"""
Provides functionalities to interact with the database that applies to all records
"""


from db_client.db_config import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key


table = dynamodb.Table("annualFootprint")


def create_dashboard_object(dashboard: dict):
    """
    Create the dashboard object record in the database
    Inputs:
        - dashboard: Represents the dashboard dictionary.
    """
    try:
        table.put_item(Item=dashboard)
        return dashboard
    except ClientError as e:
        print(e)
        return JSONResponse(content=e.response["Error"], status_code=400)


def retrieve_all_available_dashboard_objects():
    """
    Retrieves the list of dashboard objects in the database
    Returns:
        - List of available UUIDs.
    """
    try:
        response = table.scan(
            Limit=5,
            AttributesToGet=["dashboard_id"])
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=400)


def retrieve_dashboard_object_by_uuid_and_sub(id: str, sub: str):
    """
    Retrieves the dashboard object in the database based on the id and sub.
    Inputs:
        id: Represents the target id.
        sub: Represents the target key.
    Returns:
        - Single dashboard object record.
    """
    retrieved_records = table.scan(
            Limit=10,
            AttributesToGet=["dashboard_id", "data"])
    records_list = retrieved_records["Items"]
    for item in records_list:
        if item["dashboard_id"] == id and item["data"] == sub:
            return item
    return JSONResponse(
        content="No Dashboard object found", status_code=404)
