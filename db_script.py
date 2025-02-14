import mysql.connector
from mysql.connector import Error

def execute_sql_script(script_path):
    try:
        # database parameters
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='db1'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read the SQL script from file
            with open(script_path, 'r') as sql_file:
                sql_script = sql_file.read()
            
            # Execute the script
            cursor.execute(sql_script)
            # submit transaction
            connection.commit()
            print(f"SQL script executed successfully!")

    except Error as e:
        print(f"Database Error: {e}")
    except IOError as e:
        print(f"Error reading SQL file: {e}")
    finally:
        # close connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    execute_sql_script("create_table_projects.sql")
