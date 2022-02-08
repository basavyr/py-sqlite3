import db_tools


def main():
    db = db_tools.DB('db_file', ['r1', 'r2'])
    db.CheckOneTable()


if __name__ == '__main__':
    main()
