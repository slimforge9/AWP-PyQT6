from PyQt6.QtWidgets import QApplication, QSizePolicy, QFormLayout, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(360, 80, 800, 700)
        self.setWindowTitle("Apka Wsparcia Patrolowca")

        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName("main_layout")

        self.setLayout(self.main_layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
