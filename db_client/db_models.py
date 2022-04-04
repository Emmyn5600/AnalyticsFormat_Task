from os import listdir
from pydantic import BaseModel, Field
from datetime import datetime

import uuid

def generate_dashbord_id():
    """Generate the table uuid"""
    return str(uuid.uuid4())


def generate_dashboard_date():
    """Generates the current timestamp"""
    return str(datetime.now())
    

class AnnualFootprint(BaseModel):
    dashboard_id: str = Field(default_factory=generate_dashbord_id)
    startYear: str
    endYear: str
    data: list
    dataKeys: list
    created_at: str = Field(default_factory=generate_dashboard_date)
