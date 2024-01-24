# db_healthcheck.py
import psycopg2
import os 
import time

connected = False

db_vars = [
    "DB_DOCKER_HOST",
    "DB_DOCKER_NAME",
    "DB_DOCKER_USER",
    "DB_DOCKER_PASS",
    "DB_DOCKER_PORT",
]

db_vars_dict = {v:os.environ[v] for v in db_vars}

while not connected:
    print(f"Connecting to the PostgreSQL host: {db_vars_dict['DB_DOCKER_HOST']} db: {db_vars_dict['DB_DOCKER_NAME']} user: {db_vars_dict['DB_DOCKER_USER']} port: {db_vars_dict['DB_DOCKER_PORT']}", flush=True)

    try:
        conn = psycopg2.connect(
            host = db_vars_dict["DB_DOCKER_HOST"],
            database =  db_vars_dict["DB_DOCKER_NAME"],
            user = db_vars_dict["DB_DOCKER_USER"],
            password = db_vars_dict["DB_DOCKER_PASS"],
            port = db_vars_dict["DB_DOCKER_PORT"]
            )
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION()')
        version = cursor.fetchone()

        print(f'[SUCCESS] PostgreSQL database version: {version}')

        connected = True

    except Exception as e:
        print("Error:", e, flush=True)
        print(f".. Retrying connection to the PostgreSQL host: {db_vars_dict['DB_DOCKER_HOST']} db: {db_vars_dict['DB_DOCKER_NAME']} user: {db_vars_dict['DB_DOCKER_USER']} port: {db_vars_dict['DB_DOCKER_PORT']}", flush=True)
        time.sleep(5)
