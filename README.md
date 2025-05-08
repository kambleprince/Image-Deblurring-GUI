🖼️ Image Deblurring GUI using PyQt5 & OpenCV
This project is a Python-based GUI application that enables users to load an image and apply deblurring and sharpening techniques using unsharp masking. The application supports dynamic control over sharpening parameters (sigma and strength) and includes preset configurations for user convenience.

--

**🧠 Features**
 - Load and display images in GUI
 - Apply unsharp masking for deblurring
 - Denoising using OpenCV's fastNlMeansDenoisingColored
 - Adjustable sharpening intensity via sliders
 - Preset options for quick parameter tuning
 - Real-time image update in GUI
 - Built with PyQt5 and OpenCV

--

**🖥️ GUI Controls**
 - Load Image: Opens a file picker to select the image
 - Sigma Slider: Controls the standard deviation of Gaussian blur
 - Strength Slider: Controls how strongly sharpening is applied
 - Presets:
   -> Default: Sigma 3, Strength 3
   -> Sharp Boost: Sigma 2, Strength 6
   -> Mild Sharpen: Sigma 4, Strength 2
 - Deblur: Applies denoising and unsharp masking

-- 

**📂 Folder Structure**
pgsql
Copy
Edit
├── motion_deblur_GUI.py       # Main Python script for GUI
├── README.md                  # Project documentation
└── requirements.txt           # (You can generate this using pip freeze)

**🛠️ Installation**
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/image-deblurring-gui.git
cd image-deblurring-gui
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install PyQt5 opencv-python numpy
Run the app:

bash
Copy
Edit
python motion_deblur_GUI.py
🧪 Techniques Used (Based on Practical Exam)
Grayscale conversion

Histogram plotting

Image enhancement:

Log transformation

Gamma correction

Histogram equalization

📷 Sample Image Enhancements from Lab Work
The project can be extended with:

Histogram plotting

Log & gamma corrected versions of images

Auto-enhancement toggle using histogram equalization


📌 Future Improvements
-Batch processing of images

Export deblurred images

Integration of enhancement techniques from practical (log, gamma)

Add histogram view of current image
