from config import Config
from file_processor import ProcessPlugin
from file_downloader import DownloadPlugins
from file_converter import ConvertPlugins

if __name__ == "__main__":
	config = Config()

	plugin_downloader = DownloadPlugins(config)
	plugin_converter = ConvertPlugins(config)
	#plugin_processor = ProcessPlugin(config)