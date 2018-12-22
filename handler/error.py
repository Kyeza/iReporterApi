"""docstring for Error module"""


class InvalidApiUsage(Exception):
    """docstring for InvalidApiUsage"""
    status_code = 400

    def __init__(self, message, status_code=None):
        """constructor for initializing the InvalidApiUsage class"""
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """return dictionary of error message and status"""
        response = dict()
        response['status'] = self.status_code
        response['error'] = self.message
        return response
