from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout.addWidget(self.loadButton)

        self.contrastCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.contrastCheckBox.setObjectName("contrastCheckBox")
        self.verticalLayout.addWidget(self.contrastCheckBox)

        self.contrastSlider = QtWidgets.QSlider(self.centralwidget)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.setValue(50)
        self.verticalLayout.addWidget(self.contrastSlider)

        self.brightnessCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.brightnessCheckBox.setObjectName("brightnessCheckBox")
        self.verticalLayout.addWidget(self.brightnessCheckBox)

        self.brightnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setValue(50)
        self.verticalLayout.addWidget(self.brightnessSlider)

        self.denoiseCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.denoiseCheckBox.setObjectName("denoiseCheckBox")
        self.verticalLayout.addWidget(self.denoiseCheckBox)

        self.sharpenCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sharpenCheckBox.setObjectName("sharpenCheckBox")
        self.verticalLayout.addWidget(self.sharpenCheckBox)

        self.resolutionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.resolutionCheckBox.setObjectName("resolutionCheckBox")
        self.verticalLayout.addWidget(self.resolutionCheckBox)

        self.enhanceButton = QtWidgets.QPushButton(self.centralwidget)
        self.enhanceButton.setObjectName("enhanceButton")
        self.verticalLayout.addWidget(self.enhanceButton)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)  # Added saveButton
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.imageLabel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Enhancer"))
        self.loadButton.setText(_translate("MainWindow", "Load Image"))
        self.contrastCheckBox.setText(_translate("MainWindow", "Enhance Contrast"))
        self.brightnessCheckBox.setText(_translate("MainWindow", "Enhance Brightness"))
        self.denoiseCheckBox.setText(_translate("MainWindow", "Reduce Noise"))
        self.sharpenCheckBox.setText(_translate("MainWindow", "Sharpen Image"))
        self.resolutionCheckBox.setText(_translate("MainWindow", "Increase Resolution"))
        self.enhanceButton.setText(_translate("MainWindow", "Enhance Image"))
        self.saveButton.setText(_translate("MainWindow", "Save Image"))  # Added saveButton
        self.imageLabel.setText(_translate("MainWindow", "Image will appear here"))
