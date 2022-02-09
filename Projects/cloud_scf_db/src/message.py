from datetime import datetime


class Message:
    @staticmethod
    def GenerateTemplateRequest():
        os = 'macOS'
        lib_tools = ['lib1', 'lib2', 'lib3']
        apps = ['app1', 'app2', 'app3']
        timestamp = str(datetime.utcnow())

        return (os, lib_tools, apps, timestamp)
