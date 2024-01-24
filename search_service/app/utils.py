import os 
import psycopg2
from psycopg2.extras import RealDictCursor

db_vars = [
    "DB_DOCKER_HOST",
    "DB_DOCKER_NAME",
    "DB_DOCKER_USER",
    "DB_DOCKER_PASS",
    "DB_DOCKER_PORT",
]

db_vars_dict = {v:os.environ[v] for v in db_vars}


def get_database_schema(db_name):
    """
    Connects to a PostgreSQL database and retrieves the schema information, 
    including tables and their column details.

    Parameters:
    db_name (str): Name of the database to connect to.

    Returns:
    dict: A dictionary containing the database name and a list of tables with their columns.
          Each table is represented as a dictionary with 'table_name' and 'columns' keys.
          Returns None if an error occurs during database operations.
    """

    conn = None
    try:
        conn = psycopg2.connect(
            host = db_vars_dict["DB_DOCKER_HOST"],
            database =  db_vars_dict["DB_DOCKER_NAME"],
            user = db_vars_dict["DB_DOCKER_USER"],
            password = db_vars_dict["DB_DOCKER_PASS"],
            port = db_vars_dict["DB_DOCKER_PORT"]
        )

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()

            for table in tables:
                cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table['table_name']}'")
                table['columns'] = cursor.fetchall()

            schema_data = {
                'database_name': db_name,
                'tables': tables
            }

            return schema_data

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn is not None:
            conn.close()

def search_table_in_database(db_name, table_name):
    """
    Searches for a specific table within a PostgreSQL database and returns basic information 
    about it if found.

    Parameters:
    db_name (str): Name of the database to connect to.
    table_name (str): Name of the table to search for.

    Returns:
    dict: A dictionary containing the table name if found. 
          Returns None if the table is not found or an error occurs.
    """

    conn = None
    try:
        conn = psycopg2.connect(
            host = db_vars_dict["DB_DOCKER_HOST"],
            database =  db_vars_dict["DB_DOCKER_NAME"],
            user = db_vars_dict["DB_DOCKER_USER"],
            password = db_vars_dict["DB_DOCKER_PASS"],
            port = db_vars_dict["DB_DOCKER_PORT"]
        )

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = %s", (table_name,))
            result = cursor.fetchone()
            return result

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn is not None:
            conn.close()
