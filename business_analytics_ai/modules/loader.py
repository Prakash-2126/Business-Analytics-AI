import pandas as pd

class DataLoader:

    @staticmethod
    def load(file):

        if file.name.endswith(".csv"):
            return pd.read_csv(file)

        elif file.name.endswith(".xlsx"):
            return pd.read_excel(file)

        elif file.name.endswith(".json"):
            return pd.read_json(file)

        else:
            raise Exception(
                "Unsupported file format"
            )