import sqlite3
from contextlib import closing


class DB():
    def __init__(self, db_file, tables):
        """
        - Require (at init) the path to the database
        - Second argument is a list of tables that need to be created at init time
        - If there is only one table, that means only one table will be created via the corresponding method
        """
        self.db = db_file
        self.tables = tables
        self.onlyTable = None
        if(len(tables) == 1):
            self.onlyTable = tables[0]

    def CheckOneTable(self):
        if(self.onlyTable is None):
            # print('no bueno | more than one element within the table array')
            # print(self.onlyTable)
            return -1
        else:
            # print('bueno -> only one element within the table array ')
            # print(self.onlyTable)
            return 1

    def CreateDBConnection(self):
        """
        Establish a connection to a database
        If the connection works, returns a tuple containing the connection object and a cursor that allows queries within the database
        """
        try:
            connection = sqlite3.connect(self.db)
        except sqlite3.Error as err:
            print(
                f'There was an issue while trying to connect to the database\n{err}')
            return [-1, -1]
        else:
            return [connection, connection.cursor()]

    def GetDBSize(self, table_id):
        # get all the content within a table
        conn_tuple = self.CreateDBConnection()

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        full_data = cursor.execute(
            f'SELECT * FROM {self.tables[table_id]}').fetchall()

        print(len(full_data))

    def CreateTable(self):
        conn_tuple = self.CreateDBConnection()

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        # if(self.CheckOneTable() == 1):
        #     temp_table = self.onlyTable
        # else:
        #     temp_table = self.tables[0]

        # print(temp_table)

        # create the initial structure of the table
        # ********************************************
        # ************* Table Structure **************
        # ********************************************
        for temp_table in self.tables:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {temp_table}
                                (temp_id int primary_key, temp float, timestamp text, topic text)''')
        # ********************************************
        # ********************************************
        # ********************************************

        # commit/save the table creation process
        conn.commit()

        # close the connection
        conn.close()

    def DBRead(self):
        conn_tuple = self.CreateDBConnection()

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        tables_extractor = []

        for table in self.tables:
            selector = cursor.execute(f'SELECT * FROM {table}')
            extracted_data = selector.fetchall()
            tables_extractor.append(extracted_data)

        print(tables_extractor)

    def DBWrite(self, table_id, data):
        conn_tuple = self.CreateDBConnection()

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        for data_element in data:
            current_values = (1, data_element, 'timestamp',
                              f'{self.tables[table_id]}/')
            cursor.execute(
                f'INSERT INTO {self.tables[table_id]} VALUES (?,?,?,?)', current_values)

        conn.commit()

        conn.close()

    def DBReadSelected(self, table_id, col_id):
        with closing(sqlite3.connect(self.db)) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute(
                    f'SELECT * FROM {self.tables[table_id]} WHERE {col_id}>20 ORDER BY TEMP').fetchall()
                # print(rows)
                for row in rows:
                    print(row)
