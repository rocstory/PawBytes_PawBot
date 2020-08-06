class Error(Exception):
    pass


# Twitter Bot execptions 
class NoTagNamesError(Error):
    def __init__(self, value="Paw Pal dictionary is empty."):
        self.value = value
    
    def __str__(self):
        return(repr(self.value))