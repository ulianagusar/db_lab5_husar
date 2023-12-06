import psycopg2
import pandas as pd


username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'


csv_file = 'data.csv'


conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

data = pd.read_csv(csv_file)


unique_houses = set(data['allegiance'].dropna().unique().tolist() + data['killers_house'].dropna().unique().tolist())
for house in unique_houses:
    house = house.strip()
    cur.execute("SELECT * FROM Houses WHERE house_name = %s", (house,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO Houses (house_name) VALUES (%s)", (house,))

data = data.dropna()
last_50_rows = data.tail(50)

for index, row in last_50_rows.iterrows():

    episode_id = int(row['season']) * 100 + int(row['episode'])


    cur.execute("SELECT * FROM Episodes WHERE episode_id = %s", (episode_id,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO Episodes (episode_id, season, episode) VALUES (%s, %s, %s)", 
                    (episode_id, row['season'], row['episode']))

    name = row['name'].strip()
    allegiance = row['allegiance'].strip()
    cur.execute("SELECT * FROM Characters WHERE name = %s", (name,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO Characters (name, house_name) VALUES (%s, %s)", 
                    (name, allegiance))

    killer = row['killer'].strip()
    killers_house = row['killers_house'].strip() if pd.notna(row['killers_house']) else ''
    cur.execute("SELECT * FROM Characters WHERE name = %s", (killer,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO Characters (name, house_name) VALUES (%s, %s)", 
                    (killer, killers_house))

    cur.execute("INSERT INTO Deaths (death_no, location, method, episode_id, killed_name, killer_name) VALUES (%s, %s, %s, %s, %s, %s)", 
                (row['death_no'], row['location'], row['method'], episode_id, name, killer))

conn.commit()
cur.close()
conn.close()
