import pandas as pd
import sqlalchemy
import psycopg2

if __name__ == '__main__':
    df = pd.read_csv("GlobalWeatherRepository.csv")
    num_rows, num_columns = df.shape
    print(f"\nCSV entry count: {num_rows}")
    print(f"CSV number of columns: {num_columns}")
    print(f"SQLAlchemy: {sqlalchemy.__version__}")


