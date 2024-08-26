<<<<<<< HEAD
print("Hello world")
print("git test")
=======
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame,
    QSpacerItem, QSizePolicy, QStackedWidget
)
from PyQt6.QtCore import Qt
from chose_form import ChoseForms
from fill_forms import FillForms
from profile_window import ProfileWindow


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.POS_X = 100
        self.POS_Y = 100
        self.WIDTH = 800
        self.HEIGHT = 600

        self.setWindowTitle("AWP")
        self.setGeometry(self.POS_X, self.POS_Y, self.WIDTH, self.HEIGHT)
        self.setWindowOpacity(0.85)
        self.chose_forms_menu = ChoseForms()

        # Buttons size
        self.BUTTONS_SIZE = (245, 45)

        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Logo label
        logo_label = QLabel("Apka Wsparcia Patrolowca", self)
        logo_label.setStyleSheet("background-color: blue; color: white; font-size: 54px;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setFixedHeight(int(self.height() * 0.2))
        main_layout.addWidget(logo_label)

        # signature
        signature = QLabel("by Bartłomiej Krupiński KP II Gliwice", self)
        signature.setStyleSheet("background-color: blue; color: yellow; font-size: 14px;")
        signature.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(signature)

        # Horizontal layout for profile, label, slider and line edit
        upper_layout = QHBoxLayout()

        # Profile button
        profile_button = QPushButton("Profil", self)
        profile_button.setFixedSize(100, 30)
        profile_button.clicked.connect(self.open_profile_window)
        upper_layout.addWidget(profile_button)

        # Name label
        name_label = QLabel("sierż. szt. Chujnicki Arystoteles, ID: 684561", self)
        name_label.setFixedHeight(30)
        upper_layout.addWidget(name_label)

        # Add space
        upper_layout.addStretch(1)

        # Slider
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setFixedSize(85, 20)
        self.slider.setRange(50, 100)
        self.slider.setValue(85)
        upper_layout.addWidget(self.slider)

        # Line edit
        self.line_edit = QLineEdit(self)
        self.line_edit.setFixedSize(50, 20)
        self.line_edit.setText("0.85")
        upper_layout.addWidget(self.line_edit)

        # Connect slider and line edit
        self.slider.valueChanged.connect(self.change_slider)
        self.line_edit.setEnabled(False)
        # self.line_edit.editingFinished.connect(lambda text: self.slider.setValue(int(float(text) * 100)))
        # lambda value: line_edit.setText(f"{value / 100:.2f}")

        main_layout.addLayout(upper_layout)

        # Separator line
        separator = QFrame(self)
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(separator)

        # Layout for the 70% of the window
        form_layout = QVBoxLayout()

        # Add top vertical spacer
        form_layout.addStretch(1)

        # Menu management
        self.stack = QStackedWidget()
        self.stack.addWidget(self.chose_forms_menu)
        self.stack.setCurrentIndex(0)
        form_layout.addWidget(self.stack)

        # Add bottom vertical spacer
        form_layout.addStretch(1)

        # Layout for the buttons at the bottom
        button_layout = QHBoxLayout()

        # Add space on the left
        button_layout.addStretch(1)

        # "Back" button
        self.back_button = QPushButton("Menu", self)
        self.back_button.setFixedSize(*self.BUTTONS_SIZE)
        self.back_button.setStyleSheet("background-color: blue; color: white;")
        self.back_button.clicked.connect(self.menu_btn_clicked)
        button_layout.addWidget(self.back_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Clear" button
        self.clear_button = QPushButton("Wyczyść", self)
        self.clear_button.setFixedSize(*self.BUTTONS_SIZE)
        self.clear_button.setStyleSheet("background-color: blue; color: white;")
        self.clear_button.clicked.connect(self.clear_checkboxes)
        button_layout.addWidget(self.clear_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Next" button
        self.nastepny_button = QPushButton("Dalej", self)
        self.nastepny_button.setFixedSize(*self.BUTTONS_SIZE)
        self.nastepny_button.setStyleSheet("background-color: blue; color: white;")
        self.nastepny_button.clicked.connect(self.openFillFormMenu)
        button_layout.addWidget(self.nastepny_button)

        # Add space on the right
        button_layout.addStretch(1)

        form_layout.addLayout(button_layout)
        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def openFillFormMenu(self):
        # Get forms list(dict)
        chosen_forms = self.chose_forms_menu.get_forms_list()
        print(chosen_forms)

        # Set next menu
        self.fill_forms_menu = FillForms(chosen_forms)
        self.stack.addWidget(self.fill_forms_menu)
        self.stack.setCurrentIndex(1)
        self.back_button.setText("Powrót")

    def open_profile_window(self):
        """Opens manage profile window"""
        self.profile_window = ProfileWindow(self)
        self.profile_window.exec()

    def change_slider(self):
        value = self.slider.value()
        self.line_edit.setText(str(f"{value / 100:.2f}"))
        self.setWindowOpacity(float(value/100))

    def menu_btn_clicked(self):
        pass

    def clear_checkboxes(self):
        # Odznacz wszystkie checkboxy
        print(self.chose_forms_menu.clear_checkboxes())


# Run the application
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
>>>>>>> change_pages
