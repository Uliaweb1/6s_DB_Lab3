import pandas as pd
import sqlalchemy
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker
# import psycopg2
# import MySQLdb

class Base(DeclarativeBase):
    pass

class MyWeatherRecord(Base):
    __tablename__ = 'weather'

    id = mapped_column(sqlalchemy.Integer, primary_key=True)
    country = mapped_column(sqlalchemy.Text) # Text
    wind_mph = mapped_column(sqlalchemy.DECIMAL)
    wind_kph = mapped_column(sqlalchemy.DECIMAL) # floating point number
    wind_degree = mapped_column(sqlalchemy.Integer) # Integer
    wind_direction = mapped_column(sqlalchemy.Enum('SSE', 'NW', 'W', 'NE', 'SE', 'WNW', 'N', 'NNW', 'E', 'WSW', 'NNE', 'ENE', 'SW', 'S', 'SSW', 'ESE', name = "direction", create_type=False)) # enumeration
    last_updated = mapped_column(sqlalchemy.DateTime) # Date
    sunrise = mapped_column(sqlalchemy.Time) # Time

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', None)
    df = pd.read_csv("GlobalWeatherRepository.csv")
    num_rows, num_columns = df.shape
    print(f"\nCSV entry count: {num_rows}")
    print(f"CSV number of columns: {num_columns}")
    print(f"SQLAlchemy: {sqlalchemy.__version__}")

    column_types = df.dtypes.to_dict()
    # for column, dtype in column_types.items():
    #     print(f"\t{column}: {dtype}")

    column_list = []
    column_list.append("country") # Text
    # column_list.append("wind_degree") # Integer
    # column_list.append("wind_kph") # floating point number
    # column_list.append("wind_direction") # enumeration
    column_list.append("last_updated") # Date
    column_list.append("sunrise") # Time
    # wind fields
    column_list.extend(["wind_mph", "wind_kph", "wind_degree", "wind_direction"])
    df_slice = df[column_list]

    # print(df_slice.head(5))
    # for i, row in df_slice.head(5).iterrows():
    #     print(row)

    # Uncomment to get all directions
    # directions = {"N"}
    # for i, row in df_slice.iterrows():
    #         directions.add(row["wind_direction"])
    # print(directions)

    # Uncomment to print the SQL query for creationg the PostgreSQL table
    # print(CreateTable(MyWeatherRecord.__table__).compile(dialect=postgresql.dialect()))

    engine = sqlalchemy.create_engine('postgresql://Kolomiets:123a1@localhost:5432/S6_DB_Lab3')
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # MyWeatherRecord.__table__.drop(engine, checkfirst=True)
    # Base.metadata.create_all(engine)
    # for i, row in df_slice.iterrows():
    #     # print(row)
    #     new_instance = MyWeatherRecord(
    #         country = row["country"],
    #         wind_mph = row["wind_mph"],
    #         wind_kph = row["wind_kph"],
    #         wind_degree = row["wind_degree"],
    #         wind_direction = row["wind_direction"],
    #         last_updated = row["last_updated"],
    #         sunrise = row["sunrise"]
    #     )
    #     session.add(new_instance)
    session.commit()
    session.close()


