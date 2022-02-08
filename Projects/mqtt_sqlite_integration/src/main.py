import db_tools


table_generator = lambda n: [f'Table{idx}' for idx in range(n)]


def main():
    db_file = '../db/database_file.db'
    tables = table_generator(3)
    new_db = db_tools.DB(db_file, tables)
    new_db.DBWrite(0, [1321312, 32, 1, 42, 14, 21, 3, 2,
                   13, 24, 21, 4, 312, 3, 1, 2, 312, 312])
    new_db.GetDBSize(0)
    new_db.DBReadSelected(0, 'temp')


if __name__ == '__main__':
    main()
