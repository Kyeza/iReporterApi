class Incident(object):
	"""docstring for Incident"""

	id = 0

	def __init__(self, **kwargs):
		"""initializer for Incident"""
		super().__init__()

		# defaults
		self.__createdon = None
		self.__createdby = None
		self.__type = None
		self.__location = None
		self.__status = None
		self.__images = None
		self.__videos = None
		self.__comment = None

		# initializing instance variables
		self.created_on = kwargs['createdon']
		self.created_by = kwargs['createdby']
		self.type = kwargs['type']
		self.location = kwargs['location']
		self.status = kwargs['status']
		self.images = kwargs['Images']
		self.videos = kwargs['Videos']
		self.comment = kwargs['comment']

	@property
	def created_on(self):
		"""

        :return:
        """
		return self.__created_on

	@created_on.setter
	def created_on(self, value):
		"""

        :return:
        """
		self.__created_on = value
	
	@property
	def created_by(self):
		"""

        :return:
        """
		return self.__created_by

	@created_by.setter
	def created_by(self, value):
		"""

        :return:
        """
		self.__created_by = value		

	@property
    def type(self):
        """

        :return:
        """
        return self.__type

    @type.setter
    def type(self, value):
    	"""

        :return:
        """
        self.__type = value

    @property
    def location(self):
        """

        :return:
        """
        return self.__location

    @location.setter
    def location(self, value):
        self.__loaction = value

    @property
    def status(self):
        """

        :return:
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def images(self):
        """

        :return:
        """
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value

    @property
    def videos(self):
        """

        :return:
        """
        return self.__videos

    @videos.setter
    def videos(self, value):
        self.__videos = value

    @property
    def comment(self):
        """

        :return:
        """
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value
