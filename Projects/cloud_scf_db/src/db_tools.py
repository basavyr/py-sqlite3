import sqlite3


class DB:
    def __init__(self, db_file):
        self.dbFile = db_file

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

    def CreateFullResource(self):
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
        cursor.execute('''CREATE TABLE mngmtRequests
                            (req_id int primary_key, os text, lib_tools text, apps text)''')
        # ********************************************************
        # ********************************************************

        # commit/save the changes made withitn the new database/table
        connection.commit()

        # close the connection to the database
        connection.close()
