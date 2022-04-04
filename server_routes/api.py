from fastapi import APIRouter, Path
from db_client.db_models import AnnualFootprint
from db_client.db_client import create_dashboard_object
from db_client.db_client import retrieve_all_available_dashboard_objects
from db_client.db_client import retrieve_dashboard_object_by_uuid_and_sub

dashboard_route = APIRouter()



@dashboard_route.post("/create", response_model=AnnualFootprint)
def create_dashboard(dashboard: AnnualFootprint):
    return create_dashboard_object(dashboard.dict())

@dashboard_route.get("/all")
def retrieve_dashboard_objects():
    return retrieve_all_available_dashboard_objects()


@dashboard_route.get("/retrieve")
def retrieve_by_uuid_and_sub(dashboard_uuid: str, data: str):
    return retrieve_dashboard_object_by_uuid_and_sub(dashboard_uuid, data)
