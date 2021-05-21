import os
import time
import secrets
import sqlalchemy
from dotenv import load_dotenv

def create_db():
    load_dotenv()

    while (True):
        try:
            print("Connecting ...")
            database_uri = str(os.getenv('SQLALCHEMY_DATABASE_URI')) + str(os.getenv('STANDARD_DATABASE'))
            new_database = str(os.getenv('DATABASE_NAME'))

            engine = sqlalchemy.create_engine(database_uri)
            conn = engine.connect()
            conn.execute("commit")
            conn.execute("create database " + new_database)
            conn.close()
            break
        except Exception as e:
            print('Retry Connection to DB')
            time.sleep(5)

def remove_db():
    print("Deleting ...")
    database_uri = str(os.getenv('SQLALCHEMY_DATABASE_URI')) + str(os.getenv('STANDARD_DATABASE'))
    new_database = str(os.getenv('DATABASE_NAME'))

    engine = sqlalchemy.create_engine(database_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute(f"SELECT pg_terminate_backend (pid) FROM pg_stat_activity WHERE	pg_stat_activity.datname = '{new_database}';")
    conn.execute("drop database " + new_database)
    conn.close()
