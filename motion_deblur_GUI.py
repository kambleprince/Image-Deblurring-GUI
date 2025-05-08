import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QSlider, QFileDialog, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap

def unsharp_mask(image, sigma=1.5, strength=3.0):
    blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=sigma, sigmaY=sigma)
    sharpened = cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)
    return sharpened

class DeblurApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Deblurring Tool")
        self.setGeometry(100, 100, 800, 600)

        # Layouts
        self.layout = QVBoxLayout()
        self.controls_layout = QVBoxLayout()
        self.image_layout = QHBoxLayout()

        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)

        # Load Image Button
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.open_file)

        # Preset Dropdown
        self.preset_label = QLabel("Select Preset Parameters:")
        self.preset_combo = QComboBox()
        self.preset_combo.addItem("Default (Sigma 3, Strength 3)")
        self.preset_combo.addItem("Sharp Boost (Sigma 2, Strength 6)")
        self.preset_combo.addItem("Mild Sharpen (Sigma 4, Strength 2)")
        self.preset_combo.currentIndexChanged.connect(self.apply_preset)

        # Sigma Slider
        self.sigma_label = QLabel("Sigma: 3")
        self.sigma_slider = QSlider(Qt.Horizontal)
        self.sigma_slider.setRange(1, 10)
        self.sigma_slider.setValue(3)
        self.sigma_slider.setTickPosition(QSlider.TicksBelow)
        self.sigma_slider.setTickInterval(1)
        self.sigma_slider.valueChanged.connect(self.update_sigma_label)

        # Strength Slider
        self.strength_label = QLabel("Strength: 3")
        self.strength_slider = QSlider(Qt.Horizontal)
        self.strength_slider.setRange(1, 10)
        self.strength_slider.setValue(3)
        self.strength_slider.setTickPosition(QSlider.TicksBelow)
        self.strength_slider.setTickInterval(1)
        self.strength_slider.valueChanged.connect(self.update_strength_label)

        # Deblur Button
        self.deblur_button = QPushButton("Deblur")
        self.deblur_button.clicked.connect(self.apply_deblur)

        # Add widgets to layout
        self.controls_layout.addWidget(self.load_button)
        self.controls_layout.addWidget(self.preset_label)
        self.controls_layout.addWidget(self.preset_combo)
        self.controls_layout.addWidget(self.sigma_label)
        self.controls_layout.addWidget(self.sigma_slider)
        self.controls_layout.addWidget(self.strength_label)
        self.controls_layout.addWidget(self.strength_slider)
        self.controls_layout.addWidget(self.deblur_button)

        self.image_layout.addWidget(self.image_label)
        self.layout.addLayout(self.controls_layout)
        self.layout.addLayout(self.image_layout)
        self.setLayout(self.layout)

        self.image = None
        self.deblurred_image = None

    def update_sigma_label(self, value):
        self.sigma_label.setText(f"Sigma: {value}")

    def update_strength_label(self, value):
        self.strength_label.setText(f"Strength: {value}")

    def apply_preset(self, index):
        if index == 0:  # Default
            self.sigma_slider.setValue(3)
            self.strength_slider.setValue(3)
        elif index == 1:  # Sharp Boost
            self.sigma_slider.setValue(2)
            self.strength_slider.setValue(6)
        elif index == 2:  # Mild Sharpen
            self.sigma_slider.setValue(4)
            self.strength_slider.setValue(2)

    def load_image(self, path):
        self.image = cv2.imread(path)
        if self.image is not None:
            self.show_image(self.image)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")
        if file_name:
            self.load_image(file_name)

    def apply_deblur(self):
        if self.image is None:
            return

        sigma = self.sigma_slider.value()
        strength = self.strength_slider.value()

        denoised = cv2.fastNlMeansDenoisingColored(self.image, None, h=1, hColor=10, templateWindowSize=7, searchWindowSize=21)
        self.deblurred_image = unsharp_mask(denoised, sigma=sigma, strength=strength)
        self.show_image(self.deblurred_image)

    def show_image(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytes_per_line = 3 * width
        q_image = QImage(image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeblurApp()
    window.show()
    sys.exit(app.exec_())
