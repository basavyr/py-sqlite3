import db_tools


def main():
    local_db = '../db/management_requests.db'
    new_db = db_tools.DB(local_db)
    local_element = (1, 'macOS', 'lib_tools', 'apps')
    new_db.WriteOnce(local_element)


if __name__ == '__main__':
    main()
