import sys
import os

# FORCE ADD PROJECT ROOT TO PYTHON PATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from problems.linear_regression.linear_models import LinearRegressionClosedForm
from problems.linear_regression.selection import train_test_split
from problems.linear_regression.metrics import mse, r2_score
import numpy as np

def test_linear_regression_closed_form():
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    model = LinearRegressionClosedForm()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    assert pred.shape == y_test.shape
    assert mse(y_test, pred) < 1e-6
