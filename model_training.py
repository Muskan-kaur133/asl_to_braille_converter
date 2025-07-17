#training randomforestclassifier
import os
import cv2
import numpy as np
import pandas as pd
import string
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

dataset_path = "asl_alphabet_train"   # Change this to your dataset folder
image_size = 64


label_mapping = {letter: idx for idx, letter in enumerate(string.ascii_uppercase)}
reverse_label_mapping = {v: k for k, v in label_mapping.items()}

X_list = []
y_list = []

print("Loading images...")


for label_letter in sorted(os.listdir(dataset_path)):
    label_path = os.path.join(dataset_path, label_letter)

    if not os.path.isdir(label_path):
        continue

    if label_letter not in label_mapping:
        continue

    print(f"Processing label: {label_letter}")

    for file in os.listdir(label_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            image_path = os.path.join(label_path, file)
            img = cv2.imread(image_path)
            img_resized = cv2.resize(img, (image_size, image_size))
            img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
            img_flat = img_gray.flatten()
            X_list.append(img_flat)
            y_list.append(label_mapping[label_letter])

print(f" Finished loading images. Total samples: {len(X_list)}")


X_df = pd.DataFrame(X_list)
y_df = pd.Series(y_list)
X_train, X_test, y_train, y_test = train_test_split(
    X_df, y_df, test_size=0.2, random_state=42)
print("Training RandomForestClassifier...")
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print(" Training complete.")
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f" Validation Accuracy: {accuracy*100:.2f}%")


joblib.dump(clf, "asl_rf_model.pkl")
joblib.dump(label_mapping, "label_mapping.pkl")
joblib.dump(reverse_label_mapping, "reverse_label_mapping.pkl")
print(" Model and mappings saved successfully.")
