

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
