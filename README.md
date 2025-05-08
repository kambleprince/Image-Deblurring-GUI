# 🖼️ Image Deblurring GUI

Image Deblurring GUI is a simple, production-ready desktop application for enhancing and deblurring images using unsharp masking and denoising techniques. It provides an intuitive GUI to load, tune, and sharpen blurred images interactively.

---

## 🧩 Core Capabilities:
- **Image Loading:** Import and preview common image formats (.png, .jpg, .bmp).
- **Unsharp Masking:** Enhance image sharpness with tunable parameters.
- **Noise Reduction:** Apply pre-processing denoising to remove color artifacts.
- **Dynamic Parameter Control:** Adjust sigma and strength via sliders in real-time.
- **Preset Options:** Choose from predefined enhancement levels for quick results.

---

##✨ Key Features
### 🖼️ Image Enhancement Tools
 - **📤 Load Image:** Easily upload and preview images for enhancement.
 - **🔧 Sigma & Strength Sliders:** Control Gaussian blur intensity and sharpening strength.
 - **📦 Preset Configurations:**
     -> Default (Sigma 3, Strength 3)
     -> Sharp Boost (Sigma 2, Strength 6)
     -> Mild Sharpen (Sigma 4, Strength 2)
 - **🧽 Denoising:** Removes color and texture noise before deblurring.
 - **🔍 Live Preview:** See real-time changes after applying filters.

---

## 🧰 Tech Stack
**🔧 Core Technologies**
 - Python + PyQt5: GUI design and event handling.
 - OpenCV: Image processing, enhancement, and color conversion.
 - NumPy: Matrix operations and pixel manipulation.
## 📦 Dependencies
 - PyQt5
 - opencv-python
 - numpy

---

## 🚀 Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/image-deblurring-gui.git
    cd image-deblurring-gui
    ```

2. Create and activate a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Run the application:
    ```bash
    python motion_deblur_GUI.py
    ```

---


## 📂 Project Structure

```
image-deblurring-gui/
|
|├── motion_deblur_GUI.py      
|├── requirements.txt           
|└── README.md                  
```

---

## 🤝 Contribution Guidelines

Contributions are welcome!
If you'd like to propose a new feature or enhancement, open an issue or submit a pull request.

---

## 📜 License

Licensed under the MIT License.

---

Image Deblurring GUI – Simplifying Image Enhancement for Everyone ✨
