class Error(Exception):
    """docstring for Error"""
    pass
        

class InvalidApiUsage(Error):
    """docstring for InvalidApiUsage"""
    status_code = 400

    def __init__(self, message, status_code=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['status'] = self.status_code
        rv['error'] = self.message
        return rv