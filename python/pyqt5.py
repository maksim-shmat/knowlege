""" PyQt5 first steps."""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QlineEdit

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(10, 10, 400, 140)
        # Make a textbox
        self.textbox = QLineEdit(self)  # Make text imput
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        # Make a button in window
        self.button = QPushButton('Show', self)
        self.button.move(20, 80)
        # Connect the button to on_click functoion
        self.button.clicked.connect(self.on_click)
        self.show()
    
    def on_click(self):
        text = self.textbox()  # Get a text
        print("Text : ", text)  # Print it
        self.textbox.setText("") # Clear text

app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
