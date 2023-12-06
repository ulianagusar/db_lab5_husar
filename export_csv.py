import os
import psycopg2
import pandas as pd

username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'


current_directory = os.getcwd()

conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=host,
    port=port
)


def export_table_to_csv(table_name, conn, output_directory):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    output_path = os.path.join(output_directory, f'{table_name}.csv')
    df.to_csv(output_path, index=False)


tables = ['Episodes', 'Houses', 'Characters', 'Deaths']

for table in tables:
    export_table_to_csv(table, conn, current_directory)

conn.close()
