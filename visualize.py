import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt
import os
import numpy as np
def plot_results(y_test, y_pred):
    # ✅ Create outputs folder automatically
    os.makedirs("outputs", exist_ok=True)

    plt.figure()
    plt.plot(y_test.values, label="Actual")
    plt.plot(y_pred, label="Predicted")
    plt.legend()
    plt.title("Failure Prediction")
    plt.scatter(range(len(y_test)), y_test, label="Actual")
    plt.scatter(range(len(y_pred)), y_pred, label="Predicted")

    #save graph
    plt.savefig("outputs/prediction.png")

    plt.show()
    
    x = np.arange(len(y_test))

    plt.figure()
    plt.bar(x - 0.2, y_test, width=0.4, label="Actual", color='blue')
    plt.bar(x + 0.2, y_pred, width=0.4, label="Predicted", color='red')

    plt.xlabel("Samples")
    plt.ylabel("Failure (0 or 1)")
    plt.title("Actual vs Predicted (Bar Graph)")
    plt.legend()

    plt.savefig("outputs/prediction_bar.png")
    plt.show()