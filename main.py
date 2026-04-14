from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_results

# Step 1: Load Data
data = load_data("data/sensor_data.csv")

# Step 2: Preprocess
data = preprocess_data(data)

# Step 3: Feature Engineering
X, y = create_features(data)

# Step 4: Train Model
model, X_test, y_test, y_pred = train_model(X, y)

# Step 5: Evaluate
evaluate_model(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test.values)
# Step 6: Visualization
plot_results(y_test, y_pred)

