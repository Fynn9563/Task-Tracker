from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Set the application icon
        self.setWindowIcon(QIcon("favicon.ico"))

        # Set up the web view widget
        self.web_view = QWebEngineView()

        # Load a website into the web view
        self.web_view.load(QUrl("http://127.0.0.1:5000"))

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        # Set the window title
        self.setWindowTitle("Task Tracker")

if __name__ == "__main__":
    app = QApplication([])
    browser = Browser()
    browser.show()
    app.exec_()
