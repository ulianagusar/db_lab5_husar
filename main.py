import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '2006Uliana'
database = 'game'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


create_method_view = """
create or replace view method_view as
select method, count(*) as death_count
from deaths
group by method
order by death_count desc;
"""

create_location_view = """
create or replace view location_view as
select location, count(*) as death_count
from deaths
group by location;
"""

create_house_view = """
create or replace view house_view as
select c.house_name, count(*) as death_count
from characters c
join deaths d on c.name = d.killed_name
group by c.house_name
order by death_count desc;
"""

with conn:
    cur = conn.cursor()
    cur.execute(create_method_view)
    cur.execute(create_location_view)
    cur.execute(create_house_view)


query_methods = "select * from method_view;"
query_locations = "select * from location_view;"
query_houses = "select * from house_view;"


with conn:
    cur = conn.cursor()

    cur.execute(query_methods)
    method_data = cur.fetchall()

    cur.execute(query_locations)
    location_data = cur.fetchall()

    cur.execute(query_houses)
    house_data = cur.fetchall()


    methods, method_counts = zip(*method_data)
    locations, location_counts = zip(*location_data)
    houses, house_counts = zip(*house_data)


    fig, ax = plt.subplots(1, 3, figsize=(15, 5))


    ax[0].bar(methods, method_counts, color='skyblue')
    ax[0].set_title('Number of Deaths by Method')
    ax[0].set_xlabel('Method')
    ax[0].set_ylabel('Number of Deaths')
    ax[0].tick_params(axis='x', rotation=45)


    ax[1].pie(location_counts, labels=locations, autopct='%1.1f%%', startangle=140)
    ax[1].set_title('Distribution of Deaths by Location')

    ax[2].plot(houses, house_counts, color='skyblue', marker='o')
    ax[2].set_title('Number of Deaths by House')
    ax[2].set_xlabel('House')
    ax[2].set_ylabel('Number of Deaths')
    ax[2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()