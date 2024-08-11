import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame,
    QSpacerItem, QSizePolicy, QScrollArea
)
from PyQt6.QtCore import Qt


class SecondWindow(QWidget):
    def __init__(self, selected_forms):
        super().__init__()

        # Get selected forms from previous menu
        self.selected_forms = selected_forms

        self.setWindowTitle("AWP")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowOpacity(0.85)

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

        # Horizontal layout for profile, label, slider and line edit
        upper_layout = QHBoxLayout()

        # Profile button
        profile_button = QPushButton("Profile", self)
        profile_button.setFixedSize(100, 30)
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

        # Scroll Area for data forms
        scrolling_menu = QScrollArea()


            # for _ in range(4):
            #     # Add forms layout
            #     row_layout = QHBoxLayout()
            #     # row_layout.setObjectName("tys")
            #
            #     # Add space on the left
            #     row_layout.addStretch(1)
            #
            #     # checkbox
            #     checkbox = QCheckBox("Protokół zatrzymania osoby", self)
            #     # checkbox.setObjectName("lel")
            #     row_layout.addWidget(checkbox)
            #
            #     # Add space between label and spinbox
            #     row_layout.addStretch(1)
            #
            #     spinbox = QSpinBox(self)
            #     # spinbox.setObjectName("hej")
            #     spinbox.setFixedSize(60, 30)
            #     spinbox.setValue(1)
            #     row_layout.addWidget(spinbox)
            #
            #     # Add space on the right
            #     row_layout.addStretch(1)
            #
            #     form_layout.addLayout(row_layout)

        # Add bottom vertical spacer
        form_layout.addStretch(1)

        # Layout for the buttons at the bottom
        button_layout = QHBoxLayout()

        # Add space on the left
        button_layout.addStretch(1)

        # Buttons size
        buttons_size = (245, 45)
        # "Back" button
        powrot_button = QPushButton("Wstecz", self)
        powrot_button.setFixedSize(*buttons_size)
        powrot_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(powrot_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Clear" button
        clear_button = QPushButton("Wyczyść", self)
        clear_button.setFixedSize(*buttons_size)
        clear_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(clear_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Next" button
        nastepny_button = QPushButton("Dalej", self)
        nastepny_button.setFixedSize(*buttons_size)
        nastepny_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(nastepny_button)

        # Add space on the right
        button_layout.addStretch(1)

        form_layout.addLayout(button_layout)

        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)

    def change_slider(self):
        value = self.slider.value()
        self.line_edit.setText(str(f"{value / 100:.2f}"))
        self.setWindowOpacity(float(value/100))


# Run the application
# app = QApplication(sys.argv)
# window = SecondWindow()
# window.show()
# sys.exit(app.exec())
