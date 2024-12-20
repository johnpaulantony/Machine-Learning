# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\opencv\ui\Gujarathi_lang_recognition\demo2.ui'
# Generated by PyQt5 UI code generator
# WARNING: Any manual changes made to this file may be overwritten if the UI file is regenerated.

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
# Importing necessary layers for building a Convolutional Neural Network
from keras.layers import Conv2D, MaxPooling2D, Flatten, BatchNormalization, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # For augmenting and preprocessing images

# Define the main window and its functionality
class Ui_MainWindow(object):
    # Sets up the user interface layout and initializes widgets
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Create a central widget for the main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Button to browse and load an image
        self.BrowseImage = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseImage.setGeometry(QtCore.QRect(160, 370, 151, 51))
        self.BrowseImage.setObjectName("BrowseImage")

        # Label to display the loaded image
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(200, 80, 361, 261))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")

        # Title label for the application
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 621, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Button to classify the loaded image
        self.Classify = QtWidgets.QPushButton(self.centralwidget)
        self.Classify.setGeometry(QtCore.QRect(160, 450, 151, 51))
        self.Classify.setObjectName("Classify")

        # Label to show the classification result
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 370, 111, 16))
        self.label.setObjectName("label")

        # Button to start training a new model
        self.Training = QtWidgets.QPushButton(self.centralwidget)
        self.Training.setGeometry(QtCore.QRect(400, 450, 151, 51))
        self.Training.setObjectName("Training")

        # Text area to display the classification result or training status
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 390, 211, 51))
        self.textEdit.setObjectName("textEdit")

        # Configure the central widget, menu bar, and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Translate UI elements and connect buttons to their respective functions
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.BrowseImage.clicked.connect(self.loadImage)  # Connect Browse button to loadImage function
        self.Classify.clicked.connect(self.classifyFunction)  # Connect Classify button to classifyFunction
        self.Training.clicked.connect(self.trainingFunction)  # Connect Training button to trainingFunction

    # Set text for UI elements
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowseImage.setText(_translate("MainWindow", "Browse Image"))
        self.label_2.setText(_translate("MainWindow", "            COVID-19 DETECTION"))
        self.Classify.setText(_translate("MainWindow", "Classify"))
        self.label.setText(_translate("MainWindow", "Recognized Class"))
        self.Training.setText(_translate("MainWindow", "Training"))

    # Function to load and display an image in the UI
    def loadImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)")
        if fileName:  # If the user selects a file
            print(fileName)  # Debug: Print the file path
            self.file = fileName
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)  # Scale the image
            self.imageLbl.setPixmap(pixmap)  # Display the image in the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    # Function to classify the loaded image using a pre-trained model
    def classifyFunction(self):
        # Load the pre-trained model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model.weights.h5")  # Load model weights
        print("Loaded model from disk")

        # Define labels for classification
        label = ["Covid", "Normal"]

        # Preprocess the loaded image
        path2 = self.file
        test_image = image.load_img(path2, target_size=(128, 128))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make a prediction
        result = loaded_model.predict(test_image)
        print("Result", result)
        label2 = label[result.argmax()]  # Determine the predicted label
        print("Label", label2)
        self.textEdit.setText(label2)  # Display the result in the text area

    # Function to train a new CNN model and save it
    def trainingFunction(self):
        self.textEdit.setText("Training under process...")
        # Define a CNN model
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(128, 128, 3)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(2, activation='softmax'))

        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Define data generators for training and testing datasets
        train_datagen = ImageDataGenerator(rescale=1.0/255.0, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
        test_datagen = ImageDataGenerator(rescale=1.0/255.0)

        # Load training and testing datasets
        training_set = train_datagen.flow_from_directory(r'C:\Users\JOHNJESUS\OneDrive\Desktop\ML\Covid-19_Detection\TrainingDataset', target_size=(128, 128), batch_size=8, class_mode='categorical')
        test_set = test_datagen.flow_from_directory(r'C:\Users\JOHNJESUS\OneDrive\Desktop\ML\Covid-19_Detection\TestingDataset', target_size=(128, 128), batch_size=8, class_mode='categorical')

        # Train the model
        model.fit(training_set, steps_per_epoch=100, epochs=10, validation_data=test_set, validation_steps=125)

        # Save the model to disk
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        model.save_weights("model.weights.h5")
        self.textEdit.setText("Saved model to disk")

# Entry point of the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())