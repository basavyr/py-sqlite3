from datetime import datetime

from random import randrange

import random

lib_maker = lambda n: [f'lib{idx+1}' for idx in range(n)]
app_maker = lambda n: [f'app{idx+1}' for idx in range(n)]


data_maker = lambda n: [Message.GenerateTemplateRequest()
                        for _ in range(n)]
"""
- lambda that generates a list of N template requests
- each template request contains the necessary parameteres that need to be inserted in the database
"""


def stringify(message):
    stringed_dm = str(message)
    return stringed_dm


class Message:
    @staticmethod
    def GenerateTemplateRequest():
        """
        - generate a message tupe of the form (OS,[LIBS],[APPS],time_stamp)
        """
        os_list = ['macOS', 'linux', 'Windows']
        os = random.choice(os_list)
        n_libs = randrange(1, 10)
        n_apps = randrange(1, 10)
        lib_tools = lib_maker(n_libs)
        apps = app_maker(n_apps)
        timestamp = str(datetime.utcnow())

        return (os, lib_tools, apps, timestamp)

    @staticmethod
    def ShowDataContent(data):
        for data_element in data:
            print(
                f'New template request made by user with the following parameters\nReq-> {data_element}')
