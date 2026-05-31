class PrescriptiveAnalysis:

    @staticmethod
    def recommendations(df):

        recommendations = []

        numeric = df.select_dtypes(
            include=["int64", "float64"]
        )

        for col in numeric.columns:

            avg = numeric[col].mean()

            recommendations.append(
                f"{col}: Average = {avg:.2f}"
            )

        return recommendations