import pandas as pd


class DataPreprocessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):

        self.data = pd.read_csv(self.file_path)

        return self.data

    def check_missing_values(self):

        return self.data.isnull().sum()

    def remove_duplicates(self):

        self.data = self.data.drop_duplicates()

        return self.data

    def feature_target_split(self):

        X = self.data.drop("label", axis=1)

        y = self.data["label"]

        return X, y

    def dataset_info(self):

        print("Dataset Shape:")
        print(self.data.shape)

        print("Column Names:")
        print(self.data.columns)

        print("First 5 Rows:")
        print(self.data.head())