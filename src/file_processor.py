import os

class ProcessPlugin:
    def __init__(self, config):
        self.config = config
        self.path = self.config.files_path
        self.substrings = self.config.substrings

        if not len(self.substrings):
            print("No search substrings were given. Exiting.")

            exit()

        self.check_path()
        self.process()
        self.print_results()

    def check_path(self):
        """ Checks whether given path is valid. """
        if not os.path.exists(self.path):
            print(f"Given path \"{self.path}\" does not exist.")

            quit()

    def process(self):
        """ Processes given file by looking for substrings. """
        print("------ Processing ------")

        self.occurences = {}
        line_number = 0
        files = [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]

        # Open file
        for file_name in files:
            full_path = self.config.files_path + file_name

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
                            self.occurences[substring] = [[line_number, file_name]]

        print("Processed successfully\n")

    def print_results(self):
        """ Prints found results if there are any. """
        if not len(self.occurences):
            print("No results were found.")

        # Print found results for every searched substring
        for substring in self.occurences.keys():
            print(f"Results for substring \"{substring}\":")

            for line, file in self.occurences[substring]:
                print(f"\tLine {line} in {file}")