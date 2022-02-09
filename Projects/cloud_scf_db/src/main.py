import db_tools


def main():
    local_db = '../db/management_requests.db'
    new_db = db_tools.DB(local_db)
    data = [(1, 'macOS', 'lib_tools', 'apps'), (2, 'macOS', 'lib_tools', 'apps'),
            (3, 'macOS', 'lib_tools', 'apps'), (4, 'macOS', 'lib_tools', 'apps')]
    new_db.WriteData(data, write_mode='clean')


if __name__ == '__main__':
    main()
