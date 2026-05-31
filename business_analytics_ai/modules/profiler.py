class DataProfiler:

    @staticmethod
    def profile(df):

        return {
            "Rows": len(df),
            "Columns": len(df.columns),
            "Missing Values":
                int(df.isnull().sum().sum()),
            "Duplicates":
                int(df.duplicated().sum()),
            "Column Names":
                list(df.columns)
        }