import sys
import download
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QVBoxLayout, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QWidget, 
    QPushButton
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("YouTube Downloader")

        layout = QVBoxLayout()

        self.label = QLabel()
        self.input = QLineEdit()
        self.button = QPushButton()

        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)


        widget = QWidget()

        widget.setLayout(layout)
        #widget.setMaxLength(10)
        self.input.setPlaceholderText("Встав посилання на відео")

        #widget.setReadOnly(True) # раскомментируйте, чтобы сделать доступным только для чтения

        self.input.returnPressed.connect(self.return_pressed)
        self.input.selectionChanged.connect(self.selection_changed)
        self.input.textChanged.connect(self.text_changed)
        self.input.textEdited.connect(self.text_edited)
        self.button = QPushButton("Download")
        self.setCentralWidget(widget)

    link = ''
    
    def return_pressed(self):
        print('Boom')
        self.label.setText(download.info_video(self.link))
        
        

    def selection_changed(self):
        print("Selection changed")
        print(self.input.selectedText())

    def text_changed(self, s):
        self.link = s
        

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()