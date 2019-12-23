from config.config import Config
from src.file_processor import ProcessPlugin
from src.file_downloader import DownloadPlugins
from src.file_converter import ConvertPlugins

if __name__ == "__main__":
	config = Config()

	plugin_downloader = DownloadPlugins(config)
	plugin_converter = ConvertPlugins(config)
	#plugin_processor = ProcessPlugin(config)