#works on picture dataset and gives updated gui
import cv2
import numpy as np
import joblib
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

image_size = 64

clf = joblib.load("asl_rf_model.pkl")
reverse_label_mapping = joblib.load("reverse_label_mapping.pkl")

braille_dict = {
    'A': '\u2801', 'B': '\u2803', 'C': '\u2809', 'D': '\u2819', 'E': '\u2811',
    'F': '\u280B', 'G': '\u281B', 'H': '\u2813', 'I': '\u280A', 'J': '\u281A',
    'K': '\u2805', 'L': '\u2807', 'M': '\u280D', 'N': '\u281D', 'O': '\u2815',
    'P': '\u280F', 'Q': '\u281F', 'R': '\u2817', 'S': '\u280E', 'T': '\u281E',
    'U': '\u2825', 'V': '\u2827', 'W': '\u283A', 'X': '\u282D', 'Y': '\u283D', 'Z': '\u2835'
}

def upload_and_predict():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return

    img_pil = Image.open(file_path).resize((250, 250))
    img_tk = ImageTk.PhotoImage(img_pil)
    image_label.config(image=img_tk, text="")
    image_label.image = img_tk

    img_cv = cv2.imread(file_path)
    img_resized = cv2.resize(img_cv, (image_size, image_size))
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    img_flat = img_gray.flatten().reshape(1, -1)

    pred_idx = clf.predict(img_flat)[0]
    pred_letter = reverse_label_mapping[pred_idx]
    braille_symbol = braille_dict.get(pred_letter, "?")

    result_var.set(f"Predicted Letter: {pred_letter}\nBraille: {braille_symbol}")

def clear_image():
    image_label.config(image=None, text="(No Image)", bg="#ddd")
    image_label.image = None
    result_var.set("")

root = tk.Tk()
root.title("ASL Alphabet to Braille Converter")
root.geometry("400x600")
root.resizable(False,False)

title = tk.Label(root, text="ASL Alphabet to Braille Converter", font=("Arial", 16, "bold"))
title.pack(anchor=tk.W,padx=10,pady=10)

instr = tk.Label(root, text="Upload an image to predict the letter and Braille.", font=("Arial", 12), wraplength=380)
instr.pack(anchor=tk.W,padx=10,pady=5)

image_label = tk.Label(root, bg="#ddd", text="(No Image)")
image_label.pack(anchor=tk.W,padx=10,pady=15)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue", wraplength=380, justify="center")
result_label.pack(anchor=tk.W,padx=10,pady=10)

upload_button = tk.Button(root, text="Upload Image", font=("Arial", 12), width=20, command=upload_and_predict)
upload_button.pack(anchor=tk.W,padx=10,pady=5)

clear_button = tk.Button(root, text="Clear", font=("Arial", 12), width=20, command=clear_image)
clear_button.pack(anchor=tk.W,padx=10,pady=5)

footer = tk.Label(root, text="Developed by MK", font=("Arial", 10), fg="#555")
footer.pack(anchor=tk.W,padx=10,side="bottom", pady=10)

root.mainloop()

