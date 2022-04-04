from fastapi import FastAPI
from db_client.db_config import create_tables
from server_routes.api import dashboard_route


app: FastAPI = FastAPI()


app.include_router(dashboard_route, prefix="/dashboard")

create_tables()
