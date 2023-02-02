# This is all done with Mark in Class - its correct

import mariadb
import dbcreds

# Connect DB is Ready to go and be re-used for projects!
def connect_db():
    try:
        conn = mariadb.connect(
        user = dbcreds.user,
        password = dbcreds.password,
        host = dbcreds.host,
        port = dbcreds.port,
        database = dbcreds.database,
        autocommit = True
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as e:
        print("OPERATIONAL ERROR: ", e)
    except Exception as e:
        print("UNEXPECTED ERROR: ", e)

# Function to Close Cursor/Connection
def disconnect_db(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as e:
        print("OPERATIONAL ERROR: ", e)
    except mariadb.InternalError as e:
        print("INTERNAL ERROR: ", e)
    except Exception as e:
        print("UNEXPECTED ERROR:", e)