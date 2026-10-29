# import cv2
# import numpy as np
#
# def day_to_realistic_night(image):
#     """Convert a day image to a realistic night version."""
#     img = image.astype(np.float32) / 255.0
#
#     # Darken image
#     img = img * 0.25  # darker tone
#
#     # Add blue tint (moonlight effect)
#     blue_filter = np.array([0.8, 0.9, 1.2])
#     img = img * blue_filter
#     img = np.clip(img, 0, 1)
#
#     # Add vignette (dark edges)
#     rows, cols = img.shape[:2]
#     X_kernel = cv2.getGaussianKernel(cols, 200)
#     Y_kernel = cv2.getGaussianKernel(rows, 200)
#     kernel = Y_kernel * X_kernel.T
#     mask = kernel / kernel.max()
#     vignette = img * mask[:, :, np.newaxis]
#
#     # Soft blur
#     night_img = cv2.GaussianBlur(vignette, (3, 3), 0)
#     night_img = (night_img * 255).astype(np.uint8)
#
#     return night_img
#
#
# # ----------- MANUAL IMAGE INPUT -------------
# image_path = input("Enter the path of the image you want to convert: ").strip()
#
# # Read the image
# img = cv2.imread(image_path)
# if img is None:
#     print("❌ Error: Could not read image. Please check the path.")
#     exit()
#
# # Convert to night version
# night_img = day_to_realistic_night(img)
#
# # Resize both to same height
# height = 400
# aspect_day = img.shape[1] / img.shape[0]
# aspect_night = night_img.shape[1] / night_img.shape[0]
#
# day_resized = cv2.resize(img, (int(height * aspect_day), height))
# night_resized = cv2.resize(night_img, (int(height * aspect_night), height))
#
# # Create a white canvas for arrow and text
# arrow_space = 200
# canvas = np.ones((height, arrow_space, 3), dtype=np.uint8) * 255
#
# # Draw arrow (left to right)
# center_y = height // 2
# start_point = (40, center_y)
# end_point = (arrow_space - 40, center_y)
# cv2.arrowedLine(canvas, start_point, end_point, (0, 0, 0), 3, tipLength=0.2)
#
# # Add text above arrow
# cv2.putText(canvas, "CycleGAN Conversion", (15, center_y - 30),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
#
# # Combine horizontally: Night | Arrow | Day
# combined = np.hstack((night_resized, canvas, day_resized))
#
# # Display the combined image
# cv2.imshow("Night → Day Comparison", combined)
#
# print("✅ Displaying Night (left) → Day (right) conversion.")
# print("Press any key to close the window...")
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
import cv2
import numpy as np

def convert_to_night(img):
    """Simulate day → night by darkening and adding blue tone."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[..., 2] = hsv[..., 2] * 0.4  # Darken (reduce brightness)
    night_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    night_img[:, :, 0] = cv2.add(night_img[:, :, 0], 30)  # Add blue tint
    return night_img

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if not file_path:
        return

    # Read original image
    img = cv2.imread(file_path)
    img = cv2.resize(img, (400, 400))

    # Convert to night
    night_img = convert_to_night(img)

    # Convert BGR to RGB for display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    night_rgb = cv2.cvtColor(night_img, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image for Tkinter
    day_pil = Image.fromarray(img_rgb)
    night_pil = Image.fromarray(night_rgb)

    # Combine side by side
    combined = Image.new("RGB", (800, 400))
    combined.paste(night_pil, (0, 0))
    combined.paste(day_pil, (400, 0))

    # Display in Tkinter window
    tk_img = ImageTk.PhotoImage(combined)
    panel.config(image=tk_img)
    panel.image = tk_img

# GUI setup
root = tk.Tk()
root.title("Day ↔ Night Image Converter")
root.geometry("820x500")
root.configure(bg="#202020")

title = tk.Label(root, text="🌙 Night → Day / Day → Night Converter",
                 font=("Arial", 18, "bold"), fg="white", bg="#202020")
title.pack(pady=15)

upload_btn = tk.Button(root, text="📁 Upload Image",
                       command=upload_image, font=("Arial", 14),
                       bg="#1E90FF", fg="white", padx=20, pady=10)
upload_btn.pack(pady=10)

panel = tk.Label(root, bg="#202020")
panel.pack(pady=20)

root.mainloop()
