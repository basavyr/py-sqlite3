import data as data

from datetime import datetime


class Message:
    def __init__(self, data):
        self.rd_data = data

    def CreateMessage(self, rd_array):
        msg = f'{rd_array}'
        msg_avg = round(float(sum(rd_array) / len(rd_array)), 3)
        msg_size = f'{len(rd_array)}'
        timestamp = datetime.utcnow()

        return [msg, msg_size, msg_avg, timestamp]

    def CreateMessages(self):
        msgs = []
        for rd_data in self.rd_data:
            msg_object = self.CreateMessage(rd_data)
            msgs.append(msg_object)
        return msgs


def main():
    rd_data = data.Data()
    rd_arrays = rd_data.GiveData()
    dm = Message(rd_arrays)
    dms = dm.CreateMessages()

    for dm in dms:
        print(dm)


if __name__ == '__main__':
    main()
