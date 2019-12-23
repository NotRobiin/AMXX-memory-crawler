from ftplib import FTP

class DownloadPlugins:
	def __init__(self, config):
		self.config = config
		self.server = None
		self.host = self.config.ftp["host"]
		self.user = self.config.ftp["user"]
		self.password = self.config.ftp["pass"]

		self.connect()
		self.server.cwd(self.config.plugins_directory)
		self.server.retrlines("LIST")

	def connect(self):
		""" Connects to FTP """
		print(f"Connecting to server:\
				\n\tHost: {self.host}\
				\n\tUser: {self.user}\
				\n\tPassword: {self.password}")

		self.server = FTP(self.host, user = self.user, passwd = self.password)

		print(f"Connected successfully!")