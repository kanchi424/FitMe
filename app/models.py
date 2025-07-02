from sqlmodel import SQLModel, Field
from datetime import datetime

class FitnessClass(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class Booking(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    class_id: int
    client_name: str
    client_email: str
