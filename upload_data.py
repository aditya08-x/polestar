import pandas as pd
from sqlalchemy import create_engine, Table, Column, MetaData, NUMERIC, VARCHAR, TIMESTAMP, DECIMAL, ForeignKey, UUID, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from datetime import datetime
from pytz import timezone
import uuid
from dateutil import parser

UTC = timezone('UTC')

metadata = MetaData()
ships = Table(
    'ships',
    metadata,
    Column('IMO_number', Integer, primary_key=True),
    Column('ship_name', VARCHAR(255), nullable=False),
    Column('create_ts', TIMESTAMP, nullable=False),
    Column('update_ts', TIMESTAMP, nullable=False)
)

# Define the locations table
locations = Table(
    'locations',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('IMO_number', Integer, ForeignKey("ships.IMO_number"), nullable=False),
    Column('timestamp', TIMESTAMP, nullable=False),
    Column('latitude', DECIMAL, nullable=False),
    Column('longitude', DECIMAL, nullable=False)
)


def create_engine_postgress():
    postgres_user = 'postgres'
    postgres_password = 'password'
    postgres_host = 'localhost'
    postgres_port = '5433'
    postgres_db = 'polestar'
    db_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'
    engine = create_engine(db_url)
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine


def create_table():
    engine = create_engine_postgress()
    # Create all tables in the database
    metadata.create_all(engine)


def add_data_in_ships(engine, dic_for_ships):
    Session = sessionmaker(bind=engine)
    session = Session()
    for ship in dic_for_ships:
        IMO_number = ship
        ship_name = dic_for_ships[ship]
        create_ts = datetime.now(UTC)
        update_ts = datetime.now(UTC)
        ins = ships.insert().values(IMO_number=IMO_number, ship_name=ship_name, create_ts=create_ts, update_ts=update_ts)
        session.execute(ins)
    session.commit()
    session.close()


def add_data_in_loc(engine, data):
    Session = sessionmaker(bind=engine)
    session = Session()
    for index, row in data.iterrows():
        IMO_number = row['IMO number']
        latitude = row['latitude']
        longitude = row['longitude']
        timestamp_string = row['timestamp']
        timestamp = parser.parse(timestamp_string)
        ins = locations.insert().values(id=uuid.uuid4(), IMO_number=IMO_number, latitude=latitude, longitude=longitude,
                                    timestamp=timestamp)
        session.execute(ins)
    session.commit()
    session.close()


def add_data():
    engine = create_engine_postgress()
    dic_for_ships = {
        9632179: "Mathilde Maersk",
        9247455: "Australian Spirit",
        9595321: "MSC Preziosa"
    }
    data = pd.read_csv("./data.csv")
    add_data_in_ships(engine, dic_for_ships)
    add_data_in_loc(engine, data)


if __name__=="__main__":
    create_table()
    add_data()