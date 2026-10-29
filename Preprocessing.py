
import cv2
import numpy as np
import matplotlib.pyplot as plt
import albumentations as A
import os

# ------------------------------
# Set folder path containing your images
# ------------------------------
folder_path = "D:\GANPRO\Wildlife_images"  # <-- CHANGE this to your folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# ------------------------------
# Preprocessing functions
# ------------------------------
def resize_img(img, size=(640, 640)):
    return cv2.resize(img, size)

def gamma_correction(img, gamma=1.5):
    inv = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv) * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(img, table)



def denoise(img):
    return cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

augment = A.Compose([
    A.HorizontalFlip(p=1.0),
    A.Rotate(limit=15, p=1.0)
])

# ------------------------------
# Process each image
# ------------------------------
for file in image_files:
    path = os.path.join(folder_path, file)
    original = cv2.imread(path)

    if original is None:
        print(f"Could not read {file}, skipping...")
        continue

    # Apply preprocessing
    resized = resize_img(original)
    gamma_img = gamma_correction(resized)

    denoised = denoise(gamma_img)
    augmented = augment(image=denoised)['image']

    # Display all steps
    images = [original, resized, gamma_img, denoised, augmented]
    titles = ['Original', 'Resized', 'Gamma', 'Denoised', 'Augmented']

    plt.figure(figsize=(18,6))
    for i, img in enumerate(images):
        plt.subplot(1,6,i+1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    plt.suptitle(file)
    plt.show()