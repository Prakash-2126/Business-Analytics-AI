import pandas as pd

from modules.predictive import (
    PredictiveAnalysis
)

# Load dataset
df = pd.read_csv(
    "data/sales.csv"
)

# Target column
target = "Sales"

# Train model
score, model_path = (
    PredictiveAnalysis.train(
        df,
        target
    )
)

print("\nTraining Complete")
print(f"Score: {score:.4f}")
print(f"Model Saved To: {model_path}")