import sys
from PyQt5.QtWidgets import QApplication
from window import MainWindow  # Importing MainWindow class from window.py

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Creating the application
    main_window = MainWindow()  # Instantiating MainWindow
    main_window.show()  # Showing the main window
    sys.exit(app.exec_())