import data as data

from datetime import datetime


class Message:
    def __init__(self, data):
        self.rd_data = data

    @staticmethod
    def stringifyDM(dm):
        return str(dm)

    @staticmethod
    def destringifyDM(dm):
        return dm

    @staticmethod
    def CreateMessageStatic(rd_array):
        msg = rd_array
        msg_avg = round(float(sum(rd_array) / len(rd_array)), 3)
        msg_size = len(rd_array)
        # https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format
        timestamp = str(datetime.utcnow())

        return [msg, msg_size, msg_avg, timestamp]

    def CreateMessage(self, rd_array):
        msg = rd_array
        msg_avg = round(float(sum(rd_array) / len(rd_array)), 3)
        msg_size = len(rd_array)
        # https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format
        # store the datetime object as a string
        # storing the datetime as a string will prevent the different output when manipulating the message list
        timestamp = str(datetime.utcnow())

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

    dms = Message(rd_arrays)
    msgs = dms.CreateMessages()
    for msg in msgs:
        print(msg)


if __name__ == '__main__':
    main()
