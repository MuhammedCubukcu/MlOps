import pandas as pd
import numpy as np
import joblib
from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline,load_dataset

calassification_pipeline = load_pipeline(config.MODEL_NAME)

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = calassification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred==1,'Y','N')
    return output


if __name__ == '__main__':
    generate_predictions()