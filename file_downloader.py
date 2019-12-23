from ftplib import FTP
import os

class DownloadPlugins:
	def __init__(self, config):
		self.config = config
		self.server = None
		self.connected = False
		self.host = self.config.ftp["host"]
		self.user = self.config.ftp["user"]
		self.password = self.config.ftp["pass"]

		self.connect()
		self.server.cwd(self.config.plugins_directory)
		self.download()

	def connect(self):
		""" Connects to FTP """
		print("------ Connecting ------")

		self.connected = False

		try:
			self.server = FTP(self.host, user = self.user, passwd = self.password)

			print(f"Connected successfully!\n")

			self.connected = True
		
		except ftplib.error_reply:
			print("Unexpected reply received from the server.")

		except ftplib.error_temp:
			print("Error code signifying a temporary error was received.")

		except ftplib.error_perm:
			print("Error code signifying a permanent error was received.")

		except ftplib.error_proto:
			print("Reply wass received from the server that does not fit the response specifications of the File Transfer Protocol")

	def download(self):
		file_names = self.server.nlst()
		download_path = self.config.plugins_download_path
		original_path = self.config.files_path
		download_percent = 0.0
		file_index = 0

		if not os.path.exists(download_path):
			os.mkdir(download_path)

		os.chdir(download_path)

		for name in file_names:
			file_index += 1
			
			if len(file_names):
				download_percent = (file_index / len(file_names)) * 100.0

			os.system("cls")
			print("Downloading: [%0.1f %%] [%i / %i] [%s]" %(download_percent, file_index, len(file_names), name))

			with open(name, "wb") as file:
				self.server.retrbinary(f"RETR {name}", file.write)

				file.close()

		os.chdir(original_path)