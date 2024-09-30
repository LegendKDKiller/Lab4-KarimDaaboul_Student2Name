import sys

from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My PyQt App')  # Setting the window title
        
        # Creating a central widget and setting layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Adding a label widget
        label = QLabel('Hello, PyQt!')  # Creating a label
        layout.addWidget(label)  # Adding label to layout

        
        self.setCentralWidget(central_widget)