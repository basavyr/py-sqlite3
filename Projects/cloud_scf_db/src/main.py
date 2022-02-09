import db_tools

import message


def main():
    local_db = '../db/management_requests.db'
    dump_file = '../db/exported_db.dat'
    temp_element = message.Message.GenerateTemplateRequest()
    data = [temp_element for _ in range(10)]
    new_db = db_tools.DB(local_db)
    new_db.WriteData(data, write_mode='clean')
    new_db.ReadDB(dump_file, to_file=1)


if __name__ == '__main__':
    main()
