import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore
import cv2
import numpy as np
from main_windows import Ui_MainWindow


class ImageEnhancer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadButton.clicked.connect(self.load_image)
        self.enhanceButton.clicked.connect(self.enhance_image)
        self.saveButton.clicked.connect(self.save_image)
        self.image_path = None
        self.enhanced_image = None

    def load_image(self):
        try:
            options = QFileDialog.Options()
            self.image_path, _ = QFileDialog.getOpenFileName(self, "Load Image", "",
                                                             "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
            if self.image_path:
                pixmap = QPixmap(self.image_path)
                pixmap = pixmap.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
                self.imageLabel.setPixmap(pixmap)
        except Exception as e:
            self.show_error_message(f"Error loading image: {e}")

    def enhance_image(self):
        try:
            if self.image_path:
                # Load image
                image = cv2.imread(self.image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # Apply enhancements based on user selection
                if self.contrastCheckBox.isChecked():
                    factor = self.contrastSlider.value() / 50.0  # Normalize to range [0.0, 2.0]
                    image = self.adjust_contrast(image, factor)
                if self.brightnessCheckBox.isChecked():
                    factor = self.brightnessSlider.value() / 50.0  # Normalize to range [0.0, 2.0]
                    image = self.adjust_brightness(image, factor)
                if self.denoiseCheckBox.isChecked():
                    image = self.reduce_noise(image)
                if self.sharpenCheckBox.isChecked():
                    image = self.sharpen_image(image)
                if self.resolutionCheckBox.isChecked():
                    image = self.increase_resolution(image)

                # Convert back to QImage and display
                self.enhanced_image = image
                height, width, channel = image.shape
                bytes_per_line = 3 * width
                q_img = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)
                pixmap = pixmap.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio,
                                       QtCore.Qt.SmoothTransformation)
                self.imageLabel.setPixmap(pixmap)
        except Exception as e:
            self.show_error_message(f"Error enhancing image: {e}")

    def save_image(self):
        try:
            if self.enhanced_image is not None:
                options = QFileDialog.Options()
                save_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.jpeg *.bmp)",
                                                           options=options)
                if save_path:
                    cv2.imwrite(save_path, cv2.cvtColor(self.enhanced_image, cv2.COLOR_RGB2BGR))
            else:
                self.show_error_message("No enhanced image to save.")
        except Exception as e:
            self.show_error_message(f"Error saving image: {e}")

    def adjust_contrast(self, image, factor):
        return cv2.convertScaleAbs(image, alpha=factor, beta=0)

    def adjust_brightness(self, image, factor):
        return cv2.convertScaleAbs(image, alpha=1.0, beta=(factor - 1.0) * 100)

    def reduce_noise(self, image):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    def sharpen_image(self, image):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    def increase_resolution(self, image):
        scale_percent = 150  # Example: increase resolution by 150%
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEnhancer()
    window.show()
    sys.exit(app.exec_())
