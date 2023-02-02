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

# Function to Execute Statements, including with args
def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as e:
        print("Syntax error in your SQL statement: ", e)
    except mariadb.IntegrityError as e:
        print("The statement failed to execute due to integrity error, ", e)
    except mariadb.DataError as e:
        print("DATA ERROR: ", e)
    except Exception as e:
        print("Unexpected error ", e)