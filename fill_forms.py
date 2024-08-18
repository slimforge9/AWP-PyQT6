import sys
from PyQt6.QtWidgets import ( QListWidget,QTextEdit,
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame,
    QSpacerItem, QSizePolicy, QScrollArea
)
from PyQt6.QtCore import Qt


class FillForms(QWidget):
    def __init__(self, items):
        super().__init__()
        self.items = items

        self.initUI()

# Trzeba najpierw zrobic scrollView
# Dodac QFrame dla kazdego formularza, kolor ramki
# zrobic petle ktora przy tworzeniu QFrame dla formularza
# stworzy QLabel i QTextEdit dla kazdego itema w formularzu
# pobrane z forms_database
# scroll viev musi miec
    def initUI(self):
        # stash
        self.item = ["Python", "Python 2.7", "Python 2.9", "Python 3.5", "Python 3.7", "National", "Zebra",
                "Apple", "X Ray", "Boat", "Tiger", "Item001", "Item002", "Item003", "Item004", "Item005",
                "001Item", "002Item", "003Item", "004Item", "005Item", "Ball", "Cat", "Dog", "Fish",
                "Gold Fish", "Star Fish"]

        # Main layout
        main_layout = QVBoxLayout()
        scroll_area = QScrollArea()
        inside_layout = QHBoxLayout()
        inside_widget = QWidget()

        scroll_area.setWidgetResizable(True)

        for item, copies in self.items.items():
            label = QLabel(item)
            text_edit = QTextEdit("chędożyć")
            inside_layout.addWidget(label)
            inside_layout.addWidget(text_edit)

        inside_widget.setLayout(inside_layout)

        scroll_area.setWidget(inside_widget)

        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)



        # scroll_area.setWidget()