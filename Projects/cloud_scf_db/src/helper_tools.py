

class Types:
    @staticmethod
    def isVarType(var, type):
        instance_type = isinstance(var, type)
        try:
            assert instance_type is True
        except AssertionError as err:
            return -1
        else:
            return 1


class File:
    @staticmethod
    def WriteToFile(file, data):
        try:
            assert len(data) > 0
        except AssertionError as err:
            print(f'cannot write to file an empty array of data')
            return -1
        else:
            with open(file, 'w+') as writer:
                for data_element in data:
                    writer.write(str(data_element))
                    writer.write('\n')

    @staticmethod
    def ReadFile(file):
        with open(file, 'r') as reader:
            data = reader.readlines()
            for data_element in data:
                print(data_element.strip())
