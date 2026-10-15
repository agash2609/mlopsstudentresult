import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():
    rng = np.random.default_rng(42)
    hours = rng.uniform(0, 10, 1000)
    attendance = rng.uniform(40, 100, 1000)
    marks = rng.uniform(0, 100, 1000)
    features = np.column_stack((hours, attendance, marks))
    labels = ((hours >= 3) & (attendance >= 75) & (marks >= 40)).astype(int)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(features, labels)

    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    print("Model trained and saved to model.pkl")

if __name__ == "__main__":
    main()
