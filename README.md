# asl_to_braille_converter
A machine learning project to convert ASL alphabets into Braille using image classification.
This project is a Machine Learning-based application that detects American Sign Language (ASL) alphabets from images and converts them into corresponding Braille symbols.



## 🔧 Project Structure

- `model_training.py`: Trains a Random Forest classifier using image data and saves the model.
- `gui_app.py`: GUI application using Tkinter to upload and predict ASL hand signs and display Braille.
- `asl_rf_model.pkl`: Trained Random Forest model file.
- `reverse_label_mapping.pkl`: Mapping from predicted labels to ASL alphabets.
- `dataset_samples/`: Sample input images (optional).
- `README.md`: This file.

---

## 📁 Dataset

- ASL alphabet image dataset downloaded from [Kaggle](https://www.kaggle.com/).
- CSV and image-based datasets were used.
- Images were preprocessed to 64x64 grayscale.

---

## 🛠️ Tools & Libraries

- Python
- NumPy, Pandas
- Scikit-learn
- OpenCV
- Tkinter
- Pillow (PIL)
- Joblib

---

## 💡 Features

- Upload image of ASL sign ➡️ Get predicted letter ➡️ See Braille symbol.
- Braille display uses Unicode Braille Patterns.
- Model trained using Random Forest with 92% validation accuracy.
- GUI built with Tkinter.

---

## ⚠️ Limitation

This model works best when the uploaded image is **similar to the dataset used in training**. Random or real-time camera images may give inaccurate results.

---

## 👤 Developer

**Muskan Kaur**  
B.Tech CSE – Punjabi University Patiala  
Summer Training Project – 2025

---

## 🔗 Project Link

[Click here to view the full project](https://github.com/Muskan-kaur133/asl_to_braille_converter) 
