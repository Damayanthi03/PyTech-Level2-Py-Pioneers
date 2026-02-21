import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def load_data(filepath):
    if not os.path.exists(filepath):
        print("Dataset file not found")
        return None
    return pd.read_csv(filepath)
def main():
    df = load_data("data/students.csv")
    if df is None:
        return
    df["average_score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
    ) / 3
    df["result"] = df["average_score"].apply(
        lambda x: 1 if x >= 40 else 0
    )

    X = df[["math score", "reading score", "writing score"]]
    y = df["result"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    os.makedirs("output", exist_ok=True)
    with open("output/accuracy.txt", "w") as f:
        f.write(f"Model Accuracy: {accuracy*100:.2f}%")
    print(f"Model Accuracy: {accuracy*100:.2f}%")
    math = float(input("Enter Math score: "))
    reading = float(input("Enter Reading score: "))
    writing = float(input("Enter Writing score: "))
    new = pd.DataFrame(
        [[math, reading, writing]],
        columns=["math score", "reading score", "writing score"]
    )
    prediction = model.predict(new)
    if prediction[0] == 1:
        print("Prediction: PASS")
    else:
        print("Prediction: FAIL")