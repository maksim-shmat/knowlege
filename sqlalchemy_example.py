from sqlalchemy import create_engine, select, MetaData, Table, Column,\
        Integer, String, Float
from sqlalchemy.orm import sessionmaker
dbPath = 'datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
weather = Table('weather', metadata,
               Column('id', Integer, primary_key=True),
               Column("state", String),
               Column("year_text", String),
               Column("year_code", String),
               Column("avg_max_temp", Float),
               Column("max_temp_count", Integer),
               Column("max_temp_low", Float),
               Column("max_temp_high", Float),
               Column("avg_min_temp", Float),
               Column("min_temp_count", Integer),
               Column("min_temp_low", Float),
               Column("min_temp_high", Float),
               Column("heat_index", Float),
               Column("heat_index_count", Integer),
               Column("heat_index_low", Float),
               Column("heat_index_high", Float),
               Column("heat_index_coverage", String)
               )
Session = sessionmaker(bind=engine)
session = Session()
result = session.execute(select([weather]))
for row in result:
    print(row)
