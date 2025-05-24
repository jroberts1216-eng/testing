import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def load_data():
    # Generate synthetic classification dataset
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)
    columns = [f"feature_{i}" for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=columns)
    df["target"] = y

    X = df.drop("target", axis=1)
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=1)
