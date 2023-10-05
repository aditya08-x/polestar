
from sqlalchemy import create_engine, Table, Column, MetaData, NUMERIC, VARCHAR, TIMESTAMP, DECIMAL, ForeignKey, UUID

from pytz import timezone


UTC = timezone('UTC')
metadata = MetaData()

ships = Table(
    'ships',
    metadata,
    Column('IMO_number', NUMERIC, primary_key=True),
    Column('ship_name', VARCHAR(255), nullable=False),
    Column('create_ts', TIMESTAMP, nullable=False),
    Column('update_ts', TIMESTAMP, nullable=False)
)

# Define the locations table
locations = Table(
    'locations',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('IMO_number', NUMERIC),
    Column('timestamp', TIMESTAMP, nullable=False),
    Column('latitude', DECIMAL, nullable=False),
    Column('longitude', DECIMAL, nullable=False)
)
