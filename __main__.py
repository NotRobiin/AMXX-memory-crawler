from config import Config
from file_processor import ProcessPlugin

if __name__ == "__main__":
	config = Config()

	plugin_processor = ProcessPlugin(config.files_path, config.substrings)