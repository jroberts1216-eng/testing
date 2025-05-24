from models.model import train_model, predict
from utils.data_loader import load_data
from utils.visualizer import plot_feature_importance

if __name__ == "__main__":
    print("Loading data...")
    X_train, X_test, y_train, y_test = load_data()

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Generating predictions...")
    predict(model, X_test, y_test)

    print("Plotting feature importances...")
    plot_feature_importance(model, X_train.columns)
