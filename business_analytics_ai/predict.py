import joblib
import pandas as pd

model = joblib.load(
    "models/Sales_regressor.pkl"
)

new_data = pd.DataFrame({
    "Marketing": [2500],
    "Employees": [25],
    "Profit": [5000]
})

prediction = model.predict(
    new_data
)

print(
    f"Predicted Sales: {prediction[0]}"
)