import db_tools


def main():
    local_db = '../db/management_requests.db'
    new_db = db_tools.DB(local_db)


if __name__ == '__main__':
    main()
