class DataPreprocessing:
    # Corpus as a List of Strings
    # Better Data is Better than Better Models
    data: list[str]

    def __init__(self, data_dir: str):
        self.data = self.load_data(data_dir)

    @staticmethod
    def load_data(data_dir: str) -> list[str]:
        with open(data_dir) as file:
            return file.readlines()

    @staticmethod
    def train_test_split(data: list[str], test_size=0.8):
        # Split the data into test- and training-sets with a default-ratio of 80%/20%
        split_index: int = int(test_size * len(data))
        train_data: list[str] = data[0:split_index]
        test_data: list[str] = data[split_index:]
        return train_data, test_data

    @staticmethod
    def label_conversion(data: list):
        # encode labels: spam = 1, ham = 0
        encode_dict = {}
        for line in data:
            if line[0] == 'ham':
                encode_dict[' '.join(line[1:])] = 0
            elif line[0] == 'spam':
                encode_dict[' '.join(line[1:])] = 1
            else:
                print("Error")
        values = list(encode_dict.keys())
        labels = list(encode_dict.values())
        return values, labels

    def get_data(self):
        return self.data
