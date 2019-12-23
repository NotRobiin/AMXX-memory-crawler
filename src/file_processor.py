import os

class ProcessPlugin:
    def __init__(self, config):
        self.config = config
        self.path = self.config.files_path
        self.substrings = self.config.substrings

        if not len(self.substrings):
            print("No search substrings were given. Exiting.")

            exit()

        if not os.path.exists(self.path):
            print(f"Given path \"{self.path}\" does not exist.")

            exit()

        self.process()
        self.print_results()

    def process(self):
        """ Processes given file by looking for substrings. """
        self.occurences = {}
        line_number = 0
        directory_files = []
        found_data = []

        print("------ Processing ------")

        # Gather names of files in given directory
        for file_name in os.listdir(self.path):
            if not os.path.isfile(os.path.join(self.path, file_name)):
                continue

            for extension in self.config.file_types:
                if not extension in file_name:
                    continue

                directory_files.append(file_name)
                
                break

        # Open file
        for file_name in directory_files:
            full_path = self.path + file_name

            with open(full_path) as file:
                # Read it line by line
                for line in file:
                    line_number += 1

                    # Skip the line if theres noting on it
                    if not len(line):
                        continue

                    # Look for every searched keyword in the line
                    for search_key in self.substrings:
                        if not search_key in line:
                            continue

                        try:
                            found_data = self.occurences[search_key]
                            found_data.append((line_number, file_name))

                        except KeyError:
                            found_data = [(line_number, file_name)]

                        self.occurences[search_key] = found_data

        print("Processed successfully\n")

    def print_results(self):
        """ Prints found results if there are any. """
        if not len(self.occurences):
            print("No results were found.")

        # Print found results for every searched key word
        for search_key in self.occurences.keys():
            print(f"Results for substring \"{search_key}\":")

            for line, file in self.occurences[search_key]:
                print(f"\tLine {line} in {file}")