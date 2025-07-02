from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import Session, select
from app.database import create_db_and_tables, get_session
from app.models import FitnessClass, Booking
from app.schemas import FitnessClassRead, BookingCreate
from app.utils import convert_timezone
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/classes", response_model=list[FitnessClassRead])
def list_classes(timezone: str = "Asia/Kolkata", session: Session = Depends(get_session)):
    classes = session.exec(select(FitnessClass)).all()
    for cls in classes:
        cls.date_time = convert_timezone(cls.date_time, timezone)
    return classes

@app.post("/book")
def book_class(booking: BookingCreate, session: Session = Depends(get_session)):
    cls = session.get(FitnessClass, booking.class_id)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    if cls.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")
    
    if cls.available_slots <= 3:
        return {"message": "Booking successful", "note": "Hurry! Only a few slots left."}
    
    cls.available_slots -= 1
    new_booking = Booking(**booking.dict())
    session.add(new_booking)
    session.add(cls)
    session.commit()
    response = {"message": "Booking successful"}

    if cls.available_slots <= 3:
        response["note"] = "Hurry! Only a few slots left."

    return response

    return {"message": "Booking successful"}

@app.get("/bookings")
def get_bookings(client_email: str = Query(...), session: Session = Depends(get_session)):
    bookings = session.exec(select(Booking).where(Booking.client_email == client_email)).all()
    return bookings
