class App:
    def read_all_lines(self, file):
        return file.read()

    def count_lines(self, file_path):
        with open(file_path, 'r') as file:
            file_content_list = file.readlines()
            return len(file_content_list)

    def add_phrase(self, file_path, phrase):
        with open(file_path, 'a') as file:
            file.write("\n"+phrase)

    def delete(self, file_path):
        pass
