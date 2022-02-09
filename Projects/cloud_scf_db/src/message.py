from datetime import datetime

from random import randrange

import random

lib_maker = lambda n: [f'lib{idx+1}' for idx in range(n)]
app_maker = lambda n: [f'app{idx+1}' for idx in range(n)]


data_maker = lambda n: [str(Message.GenerateTemplateRequest())
                        for _ in range(n)]


class Message:
    @staticmethod
    def GenerateTemplateRequest():
        os_list = ['macOS', 'linux', 'Windows']
        os = random.choice(os_list)
        n_libs = randrange(1, 5)
        n_apps = randrange(1, 5)
        lib_tools = lib_maker(n_libs)
        apps = app_maker(n_apps)
        timestamp = str(datetime.utcnow())

        return (os, lib_tools, apps, timestamp)
