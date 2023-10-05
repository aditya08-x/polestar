from sqlalchemy import select
from polestar.models import models
URL = '/health'

SQL_SESSION = None


def get_help_status():
    session = SQL_SESSION()
    query = select(models.ships)
    output = session.execute(query).fetchone()
    if output:
        return "Health is good"
    else:
        return "Not in a good state"
