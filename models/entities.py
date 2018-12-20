"""docstring for Entity module"""

# pylint: disable=useless-object-inheritance
class Incident(object):
    """docstring for Incident"""

    # pylint: disable=too-many-instance-attributes
    # 16 is reasonable in this case.

    obj_id = 0

    def __init__(self, **kwargs):
        """initializer for Incident"""
        super().__init__()

        # increment id on creation of a new instance
        Incident.obj_id += 1

        #  defaults
        defaults = {
            'createdOn' : None,  
            'createdBy' : None, 
            'type' : None,       
            'location' : None,   
            'status' : None,     
            'Images' : None, 
            'Videos' : None,
            'comment' : None
        }

        try:
            for k,w in kwargs.items():
                if k in defaults:
                    defaults[k] = w
                else:
                    raise TypeError(f'No such key({k})')
        except TypeError:
            pass

        # initializing instance variables
        self.created_on = defaults['createdOn']
        self.created_by = defaults['createdBy']
        self.type = defaults['type']
        self.location = defaults['location']
        self.status = defaults['status']
        self.images = defaults['Images']
        self.videos = defaults['Videos']
        self.comment = defaults['comment']

        self.incident = defaults


    @property
    def created_on(self):
        """getter returns """
        return self.__created_on

    @created_on.setter
    def created_on(self, value):
        """setter for """
        self.__created_on = value

    @property
    def created_by(self):
        """getter returns """
        return self.__created_by

    @created_by.setter
    def created_by(self, value):
        """setter for """
        self.__created_by = value

    @property
    def type(self):
        """getter returns """
        return self.__type

    @type.setter
    def type(self, value):
        """setter for """
        self.__type = value

    @property
    def location(self):
        """getter returns """
        return self.__location

    @location.setter
    def location(self, value):
        """setter for """
        self.__location = value

    @property
    def status(self):
        """getter returns """
        return self.__status

    @status.setter
    def status(self, value):
        """setter for """
        self.__status = value

    @property
    def images(self):
        """getter returns """
        return self.__images

    @images.setter
    def images(self, value):
        """setter for """
        self.__images = value

    @property
    def videos(self):
        """getter returns """
        return self.__videos

    @videos.setter
    def videos(self, value):
        """setter for """
        self.__videos = value

    @property
    def comment(self):
        """getter returns """
        return self.__comment

    @comment.setter
    def comment(self, value):
        """setter for """
        self.__comment = value

    @property
    def incident(self):
        """getter for """
        return self.__incident

    @incident.setter
    def incident(self, value):
        """setter for """
        self.__incident = value