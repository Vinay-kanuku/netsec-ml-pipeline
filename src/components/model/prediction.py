
import joblib
import numpy as np

from src.constant.training_pipeline import FINAL_MODEL_PATH


def predict(data):
    """Main function for command line usage"""
    # model = pickle.load(open(FINAL_MODEL_PATH, "rb"))
    model = joblib.load(FINAL_MODEL_PATH)
    features = list(data)
    data = np.array(features, dtype=np.float64).reshape(1, 30)
    op = model.predict(data)
    return op[0]
if __name__ == "__main__":
    predict()
