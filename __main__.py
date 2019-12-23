from config import Config
from file_processor import ProcessPlugin
from file_downloader import DownloadPlugins

if __name__ == "__main__":
	config = Config()

	plugin_downloader = DownloadPlugins()
	#plugin_processor = ProcessPlugin(config.files_path, config.substrings)