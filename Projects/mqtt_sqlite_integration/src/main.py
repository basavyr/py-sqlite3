import db_tools


table_generator = lambda n: [f'Table{idx}' for idx in range(n)]


def main():
    db_file = '../db/database_file.db'
    tables = table_generator(3)
    new_db = db_tools.DB(db_file, tables)
    new_db.CreateTable()


if __name__ == '__main__':
    main()
