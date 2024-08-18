import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame,
    QSpacerItem, QSizePolicy, QScrollArea
)
from PyQt6.QtCore import Qt


class FillForms(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        main_layout = QVBoxLayout()
