import ftplib as ftp
import os
import time

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

        # Try connecting
        try:
            self.server = ftp.FTP(self.host, user = self.user, passwd = self.password)

            print(f"Connected successfully!\n")

            self.connected = True
        
        # Handle errors
        except ftp.error_reply:
            print("Unexpected reply received from the server.")

        except ftp.error_temp:
            print("Error code signifying a temporary error was received.")

        except ftp.error_perm:
            print("Error code signifying a permanent error was received.")

        except ftp.error_proto:
            print("Reply was received from the server that does not fit the response specifications of the File Transfer Protocol")

        # Connecting failed?
        if self.server == None:
            print("Connection attempt failed. Closing program.")

            time.sleep(3)

            exit()

    def download(self):
        file_names = self.server.nlst()
        download_path = self.config.plugins_download_path
        original_path = self.config.files_path
        download_progress = 0.0
        file_number = 0

        if not os.path.exists(download_path):
            os.mkdir(download_path)

        os.chdir(download_path)

        for name in file_names:
            file_number += 1
            
            if len(file_names):
                download_progress = (file_number / len(file_names)) * 100.0

            os.system("cls")

            print("Downloading: [%0.1f %%] [%i / %i] [%s]" %(download_progress, file_number, len(file_names), name))

            with open(name, "wb") as file:
                self.server.retrbinary(f"RETR {name}", file.write)

                file.close()

        os.chdir(original_path)