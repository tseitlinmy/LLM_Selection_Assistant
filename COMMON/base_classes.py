# class B(A):
#    def __init__(self, param):
#        super().__init__(param)
class BaseProvider:
    def __init__(self, name: str, isSupported: bool = False):
        self.name = name
        self.isSupported = isSupported
        self.apiKey = "" # Not defined