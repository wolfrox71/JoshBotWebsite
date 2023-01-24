class status:
	DEFAULT_STATUS = "RUNNING"
	AVALABLE_STATUSES = ["RUNNING", "STOPPED"]
	def __init__(self, filename):
		self.filename = filename

	def get_status(self):
		with open(self.filename, "r+") as f:
			file_status = f.readline()
			if (file_status in status.AVALABLE_STATUSES):
				return file_status
		self.update_status()
		return self.DEFAULT_STATUS

	def update_status(self, update_status = DEFAULT_STATUS):
		with open(self.filename, "w+") as f:
			f.write(update_status)	

	def other(self, value):
		return self.AVALABLE_STATUSES[self.AVALABLE_STATUSES.index(value) -1 % (len(self.AVALABLE_STATUSES))]