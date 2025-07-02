from app.database import get_session, create_db_and_tables
from app.models import FitnessClass
from datetime import datetime

def seed_data():
    session = next(get_session())
    classes = [
        FitnessClass(name="Yoga", date_time=datetime(2025, 7, 1, 7, 0), instructor="Alice", available_slots=5),
        FitnessClass(name="Zumba", date_time=datetime(2025, 7, 1, 8, 0), instructor="Bob", available_slots=10),
        FitnessClass(name="HIIT", date_time=datetime(2025, 7, 1, 9, 0), instructor="Charlie", available_slots=8),
        FitnessClass(name="GYM", date_time=datetime(2025, 7, 1, 22, 0), instructor="Hari", available_slots=15),
        FitnessClass(name="GYMNASTICS", date_time=datetime(2025, 7, 19, 9, 0), instructor="Ayyappa", available_slots=34),
        FitnessClass(name="SWIMMING", date_time=datetime(2025, 7, 1, 18, 0), instructor="Sachin Tendulkar", available_slots=14)
        
    ]
    session.add_all(classes)
    session.commit()

if __name__ == "__main__":
    create_db_and_tables()
    seed_data()
