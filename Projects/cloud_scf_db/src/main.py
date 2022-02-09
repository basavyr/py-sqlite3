import db_tools

import message


def main():
    local_db = '../db/management_requests.db'
    temp_element = message.Message.GenerateTemplateRequest()
    data = [temp_element for _ in range(10)]
    new_db = db_tools.DB(local_db)
    new_db.WriteData(data, write_mode='clean')


if __name__ == '__main__':
    main()
