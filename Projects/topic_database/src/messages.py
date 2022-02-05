
from datetime import datetime


class Message:
    def __init__(self, data):
        """
        - initialize the class with a list of random arrays
        - argument data is representing the list of random arrays
        """
        self.rd_data = data

    @staticmethod
    def stringifyDM(dm):
        """
        - transform every element within a list of messages to a string
        - the `dm` argument represents a list of elements
        - each element will be stringified, then appended to a new list
        - the newly obtained list will be printed
        """
        str_dm = tuple(map(str, dm))
        return str_dm

    @staticmethod
    def CreateMessageStatic(rd_array):
        """
        - the static version of CreateMessage class method
        """
        rd_arr_avg = round(float(sum(rd_array) / len(rd_array)), 3)
        rd_arr_size = len(rd_array)
        # https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format
        # store the datetime object as a string
        # storing the datetime as a string will prevent the different output when manipulating the message list
        rd_arr_timestamp = str(datetime.utcnow())

        # the message must be a TUPLE and not a list
        msg = (rd_array, rd_arr_size, rd_arr_avg, rd_arr_timestamp)

        return msg

    def CreateMessage(self, rd_array):
        """
        - returns a list of objects containing:
            * an array of random elements
            * the size of the array 
            * the average value of the array
            * a timestamp representing the time at which the message was generated
            * entire collection of objects defined above are embedded in a so-called MESSAGE
        """
        rd_arr_avg = round(float(sum(rd_array) / len(rd_array)), 3)
        rd_arr_size = len(rd_array)
        # https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format
        # store the datetime object as a string
        # storing the datetime as a string will prevent the different output when manipulating the message list
        rd_arr_timestamp = str(datetime.utcnow())

        # the message must be a TUPLE and not a list
        msg = (rd_array, rd_arr_size, rd_arr_avg, rd_arr_timestamp)

        return msg

    def CreateMessages(self):
        """
        - the method takes a list of arrays that are randomly generated (via another class) and embeds them into messages that are saved in memory
        - the messages are composed of several objects, and each message that is generated from its corresponding array is stored in the `msgs` object => representing the resulting list of messages
        - the method does not take any arguments since it will take the data that was provided at class initialization
        """
        # the list in which every individual message is stored
        messages = []

        for rd_array in self.rd_data:
            msg = self.CreateMessage(rd_array)
            messages.append(msg)
        return messages
