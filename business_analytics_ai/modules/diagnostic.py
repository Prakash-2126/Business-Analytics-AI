class DiagnosticAnalysis:

    @staticmethod
    def correlation(df):

        numeric = df.select_dtypes(
            include=["int64", "float64"]
        )

        return numeric.corr()