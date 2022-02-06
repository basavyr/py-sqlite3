import sqlite3


class DB:
    DB_STORAGE_PATH = '../src/'

    def CreateConnection(self, database):
        try:
            conn = sqlite3.connect(f'{self.DB_STORAGE_PATH}{database}')
        except sqlite3.Error as err:
            print(
                f'Issue with creating a connection to the database {database}')
            return -1
        else:
            return conn

    def CreateConnectedCursor(self, database):
        """
        - returns a tuple containing the connection object to the database
        - the second element is the cursor object 
        """
        conn = self.CreateConnection(database)
        if(conn == -1):
            return -1
        cursor = conn.cursor()

        return [conn, cursor]

    def GetDBSize(self, database, table):
        """
        - returns the number of items within the db
        """
        conn, cursor = self.CreateConnectedCursor(database)

        content = cursor.execute(f'SELECT * FROM {table}')

        all_data = content.fetchall()
        db_size = len(all_data)

        return db_size

    def CreateTable(self, database, table):
        conn_tuple = self.CreateConnectedCursor(database)

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table}
                            (temp_id int, temp float,timestamp str, topic str)''')

        # commit creation table
        conn.commit()

        print(f'connection -> {conn}')
        print(f'cursor -> {cursor}')

        # close the connection
        conn.close()
