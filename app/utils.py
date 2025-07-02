from datetime import datetime
import pytz

def convert_timezone(dt: datetime, target_timezone: str) -> datetime:
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(target_timezone)
    dt_ist = ist.localize(dt)
    return dt_ist.astimezone(target)
