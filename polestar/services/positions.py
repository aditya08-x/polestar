from sqlalchemy import select, desc
from polestar.models import models
URL = '/positions/<imo>'

SQL_SESSION = None


def get_ship_position(session, imo):
    query = select(models.locations).where(models.locations.c.IMO_number == imo).order_by(desc(models.locations.c.timestamp))
    output = session.execute(query).fetchall()
    result = []
    for ship in output:
        data = {
            "IMO_number": int(ship.IMO_number),
            "latitude": str(ship.latitude),
            "longitude": str(ship.longitude)
        }
        result.append(data)
    return result

