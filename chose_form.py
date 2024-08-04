import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QVBoxLayout, QFrame,
    QSpinBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AWP")
        self.setGeometry(100, 100, 800, 600)

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
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setFixedSize(85, 20)
        slider.setRange(50, 100)
        slider.setValue(85)
        upper_layout.addWidget(slider)

        # Line edit
        line_edit = QLineEdit(self)
        line_edit.setFixedSize(50, 20)
        line_edit.setText("0.85")
        upper_layout.addWidget(line_edit)

        # Connect slider and line edit
        slider.valueChanged.connect(lambda value: line_edit.setText(f"{value / 100:.2f}"))
        line_edit.textChanged.connect(lambda text: slider.setValue(int(float(text) * 100)))

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

        for i in range(6):
            row_layout = QHBoxLayout()

            # Add space on the left
            row_layout.addStretch(1)

            # Checkbox
            checkbox = QCheckBox(self)
            checkbox.setFixedSize(20, 20)
            row_layout.addWidget(checkbox)

            # Label
            label = QLabel(f"Label {i + 1}", self)
            label.setFixedHeight(30)
            row_layout.addWidget(label)

            # Add space between label and spinbox
            row_layout.addStretch(1)

            # Spinbox
            spinbox = QSpinBox(self)
            spinbox.setFixedSize(60, 30)
            spinbox.setValue(1)
            row_layout.addWidget(spinbox)

            # Add space on the right
            row_layout.addStretch(1)

            form_layout.addLayout(row_layout)

        # Add bottom vertical spacer
        form_layout.addStretch(1)

        # Layout for the buttons at the bottom
        button_layout = QHBoxLayout()

        # Add space on the left
        button_layout.addStretch(1)

        # "Powrot" button
        powrot_button = QPushButton("Powrót", self)
        powrot_button.setFixedSize(300, 50)
        powrot_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(powrot_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Clear" button
        clear_button = QPushButton("Clear", self)
        clear_button.setFixedSize(300, 50)
        clear_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(clear_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Nastepny" button
        nastepny_button = QPushButton("Następny", self)
        nastepny_button.setFixedSize(300, 50)
        nastepny_button.setStyleSheet("background-color: blue; color: white;")
        button_layout.addWidget(nastepny_button)

        # Add space on the right
        button_layout.addStretch(1)

        form_layout.addLayout(button_layout)

        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)


# Run the application
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
