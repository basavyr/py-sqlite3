import sqlite3


class DB:

    def CreateConnection(self, database):
        try:
            conn = sqlite3.connect(database)
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

    def CreateTable(self, database, table_name):
        conn_tuple = self.CreateConnectedCursor(database)

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        print(f'connection -> {conn}')
        print(f'cursor -> {cursor}')
