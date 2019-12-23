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
        files = []

        print("------ Processing ------")

        # Add proper files to list
        for file in os.listdir(self.path):
            if not os.path.isfile(os.path.join(self.path, file)):
                continue

            for extension in self.config.file_types:
                if not extension in file:
                    continue

                files.append(file)
                
                break

        # Open file
        for file_name in files:
            full_path = self.path + file_name

            with open(full_path) as file:
                # Read it line by line
                for line in file:
                    line_number += 1

                    # Skip the line if theres noting on it
                    if not len(line):
                        continue

                    # Look for every substring in the line
                    for substring in self.substrings:
                        if not substring in line:
                            continue

                        try:
                            found_data = self.occurences[substring]
                            found_data.append([line_number, file_name])

                            self.occurences[substring] = found_data

                        except KeyError:
                            self.occurences[substring] = [(line_number, file_name)]

        print("Processed successfully\n")

    def print_results(self):
        """ Prints found results if there are any. """
        if not len(self.occurences):
            print("No results were found.")

        # Print found results for every searched substring
        for search_key in self.occurences.keys():
            print(f"Results for substring \"{search_key}\":")

            for line, file in self.occurences[search_key]:
                print(f"\tLine {line} in {file}")