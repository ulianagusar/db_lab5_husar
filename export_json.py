import psycopg2
import json

username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=host,
    port=port
)

def export_all_tables_to_json(conn, output_filename):
    cursor = conn.cursor()
    tables = ['Episodes', 'Houses', 'Characters', 'Deaths']
    data = {}

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        table_data = []


        column_names = [desc[0] for desc in cursor.description]

        for row in rows:
            table_data.append(dict(zip(column_names, row)))

        data[table] = table_data


    cursor.close()
    conn.close()

    with open(output_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

export_all_tables_to_json(conn, 'database_data.json')
