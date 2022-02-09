import db_tools


def main():
    local_db = '../db/management_requests.db'
    temp_element = ('macOS', 'libs', 'apps')
    new_db = db_tools.DB(local_db)
    new_db.WriteOnce(temp_element)


if __name__ == '__main__':
    main()
