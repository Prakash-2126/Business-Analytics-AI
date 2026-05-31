import joblib
import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

from sklearn.metrics import (
    r2_score,
    accuracy_score
)


class PredictiveAnalysis:

    @staticmethod
    def train(df, target):

        data = df.copy()

        data = pd.get_dummies(data)

        X = data.drop(
            columns=[
                col for col in data.columns
                if target in col
            ]
        )

        y = df[target]

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        if y.dtype == "object":

            model = RandomForestClassifier(
                n_estimators=200
            )

            model.fit(X_train, y_train)

            preds = model.predict(X_test)

            score = accuracy_score(
                y_test,
                preds
            )

            model_path = (
                f"models/{target}_classifier.pkl"
            )

        else:

            model = RandomForestRegressor(
                n_estimators=200
            )

            model.fit(X_train, y_train)

            preds = model.predict(X_test)

            score = r2_score(
                y_test,
                preds
            )

            model_path = (
                f"models/{target}_regressor.pkl"
            )

        joblib.dump(
            model,
            model_path
        )

        return score, model_path