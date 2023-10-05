from sqlalchemy import select
from polestar.models import models
URL = '/ships'


def get_all_ships(session):
    query = select(models.ships)
    output = session.execute(query).fetchall()
    result = []
    for ship in output:
        data = {
            "IMO_number": ship.IMO_number,
            "ship_name": ship.ship_name
        }
        result.append(data)
    return result