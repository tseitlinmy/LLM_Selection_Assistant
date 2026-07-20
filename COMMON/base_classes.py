import tempfile

# Output value class
class OutVal:
    def __init__(self):
        self.val = None

# class B(A):
#    def __init__(self, param):
#        super().__init__(param)
class BaseProvider:
    def __init__(self, name: str, isSupported: bool = False):
        self.name = name
        self.isSupported = isSupported
        self.apiKey = "" # Not defined

class WorkArea: #(WA)
    def __init__(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = self.temp_dir.name 
        self.eds_path = None # Evaluation Dataset path