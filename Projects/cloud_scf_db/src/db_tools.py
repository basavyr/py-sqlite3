import sqlite3

from contextlib import closing


class DB:
    def __init__(self, db_file):
        self.dbFile = db_file
        self.CreateTableRequest = 1
        """
        - if this is true, then the table will be created. otherwise it will skip the table creation 
        """

    def CreateConnection(self):
        try:
            connection = sqlite3.connect(self.dbFile)
        except sqlite3.Error as err:
            return [-1, -1]
            print(f'Issue while connecting to the database')
        else:
            pass
        cursor = connection.cursor()

        conn_tuple = [connection, cursor]
        return conn_tuple

    def DropTable(self):
        conn_tuple = self.CreateConnection()

        connection = conn_tuple[0]
        cursor = conn_tuple[1]

        cursor.execute('DROP TABLE IF EXISTS mngmtRequests')

        connection.commit()

        connection.close()

    def CreateFullRequest(self):
        conn_tuple = self.CreateConnection()

        conn = conn_tuple[0]
        cursor = conn_tuple[1]

        # ********** the table name is `resources` ***********
        # ****************************************************
        cursor.execute('''CREATE TABLE IF NOT EXISTS resources
                            (res_id int primary_key, lib_tools text, soft_tools text, languages text, vm_template text, os text, ssd_storage float, n_cores int, ram float, cpu_hours int''')
        # ****************************************************
        # ****************************************************

        conn.commit()
        conn.close()

    def CreateTemplateRequest(self):
        conn_tuple = self.CreateConnection()

        connection = conn_tuple[0]
        cursor = conn_tuple[1]

        # create the database that corresponds to the template request page
        # within the project documentation, it is the Fig.2

        # *************** database/table structure ***************
        # ********************************************************
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS mngmtRequests (req_id int primary_key, os text, lib_tools text, apps text)''')
        # ********************************************************
        # ********************************************************

        # commit/save the changes made withitn the new database/table
        connection.commit()

        # close the connection to the database
        connection.close()

    def WriteOnce(self, data_element):
        with closing(sqlite3.connect(self.dbFile)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    'INSERT INTO mngmtRequests VALUES (?,?,?,?)', data_element)
                connection.commit()

    def WriteData(self, data, write_mode):
        with closing(sqlite3.connect(self.dbFile)) as connection:
            with closing(connection.cursor()) as cursor:
                if(write_mode == 'clean'):
                    self.DropTable()
                self.CreateTemplateRequest()
                for data_element in data:
                    self.WriteOnce(data_element)
