class DescriptiveAnalysis:

    @staticmethod
    def generate(df):

        numeric = df.select_dtypes(
            include=["int64", "float64"]
        )

        return {
            "summary":
                numeric.describe().to_dict()
        }