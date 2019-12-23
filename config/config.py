class Config:
	def __init__(self):
		self.files_path = "C:/users/robertt/desktop/files/"
		self.substrings = [
			"abcdefghijklmnopqrstu",
			"set_user_flags",
			"get_user_flags"
		]
		self.file_types = [
			".memory",
			".txt"
		]

		self.ftp = {
			"host" : "w69.1shot1kill.pl",
			"user" : "srv61295",
			"pass" : "NuKAw27HwF"
		}

		self.plugins_directory = "CS_1.6/cstrike/addons/amxmodx/plugins"
		self.plugins_download_path = "C:/users/robertt/desktop/files/amxx"

		self.uncompresser_path = "C:/users/robertt/desktop/programming/decompilers/AMXX_UNCOMPRESS/amxx_uncompress.exe"