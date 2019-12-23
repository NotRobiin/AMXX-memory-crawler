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
		try:
			self.server = FTP(self.host, user = self.user, passwd = self.password)

			print(f"Connected successfully!")
		
		except ftplib.error_reply:
			print("Unexpected reply received from the server.")

		except ftplib.error_temp:
			print("Error code signifying a temporary error was received.")

		except ftplib.error_perm:
			print("Error code signifying a permanent error was received.")

		except ftplib.error_proto:
			print("Reply wass received from the server that does not fit the response specifications of the File Transfer Protocol")