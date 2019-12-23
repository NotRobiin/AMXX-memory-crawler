from os.path import isfile, join
import os
import time

class ConvertPlugins:
	def __init__(self, config):
		self.config = config
		self.paths = []

		self.get_paths()
		self.convert()

	def get_paths(self):
		path = self.config.plugins_download_path
		self.paths = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

	def convert(self):
		print("------ Converting ------")

		for file in self.paths:
			command = f"cmd /c {self.config.uncompresser_path} {file}"

			print(f"Executing command {command}")
			os.system(command)

		print("Converted successfully\n")