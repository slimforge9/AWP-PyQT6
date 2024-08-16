import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QCheckBox, QHBoxLayout, QVBoxLayout, QFrame,
    QSpinBox, QSpacerItem, QSizePolicy, QMessageBox
)
from PyQt6.QtCore import Qt
from forms_database import dict_of_fields as forms_db
from fill_forms import SecondWindow


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AWP")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowOpacity(0.85)

        # Holder for forms that user chosen.
        self.chosen_forms = []
        self.no_forms = len(forms_db.keys())

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

        #signature
        signature = QLabel("by Bartłomiej Krupiński KP II Gliwice", self)
        signature.setStyleSheet("background-color: blue; color: yellow; font-size: 14px;")
        signature.setAlignment(Qt.AlignmentFlag.AlignRight)
        #signature.setFixedHeight(int(self.height() * 0.2))
        main_layout.addWidget(signature)

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

        # Checkboxes and other elements
        self.form_checkboxes = {}
        self.form_spinners = {}
        for form_name in forms_db.keys():
            # Add forms layout
            row_layout = QHBoxLayout()

            # Add space on the left
            row_layout.addStretch(1)

            # checkbox
            checkbox = QCheckBox()
            checkbox.setObjectName(f"{form_name}_chbx")
            # added
            self.form_checkboxes[form_name] = checkbox

            row_layout.addWidget(checkbox)

            # Label
            form_title = QLabel(f"{forms_db[form_name]['description']}", self)
            form_title.setObjectName(f"{form_name}_title")
            form_title.setFixedHeight(30)
            row_layout.addWidget(form_title)

            # Add space between label and spinbox
            row_layout.addStretch(1)

            # Spinbox
            spinbox = QSpinBox(self)
            spinbox.setFixedSize(60, 30)
            spinbox.setValue(1)
            spinbox.setRange(1, 10)
            # added
            self.form_spinners[form_name] = spinbox
            row_layout.addWidget(spinbox)

            # Add space on the right
            row_layout.addStretch(1)

            form_layout.addLayout(row_layout)

        # Reference to saved names
        # self.detain_chbx = self.findChild(QCheckBox, "detain_form_chbx")
        # self.warrant_chbx = self.findChild(QCheckBox, "warrant_form_chbx")
        # self.identity_chbx = self.findChild(QCheckBox, "identity_form_chbx")


        # Add bottom vertical spacer
        form_layout.addStretch(1)

        # Layout for the buttons at the bottom
        button_layout = QHBoxLayout()

        # Add space on the left
        button_layout.addStretch(1)

        # Buttons size
        buttons_size = (245, 45)
        # "Back" button
        powrot_button = QPushButton("Menu", self)
        powrot_button.setFixedSize(*buttons_size)
        powrot_button.setStyleSheet("background-color: blue; color: white;")
        powrot_button.clicked.connect(self.menu_btn_clicked)
        button_layout.addWidget(powrot_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Clear" button
        clear_button = QPushButton("Wyczyść", self)
        clear_button.setFixedSize(*buttons_size)
        clear_button.setStyleSheet("background-color: blue; color: white;")
        clear_button.clicked.connect(self.clear_checkboxes)
        button_layout.addWidget(clear_button)

        # Spacer between buttons
        button_layout.addSpacerItem(QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        # "Next" button
        nastepny_button = QPushButton("Dalej", self)
        nastepny_button.setFixedSize(*buttons_size)
        nastepny_button.setStyleSheet("background-color: blue; color: white;")
        nastepny_button.clicked.connect(self.openNextWindow)
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


    def openNextWindow(self):
        # This func is game changer and this line under
        selected_forms = {form: spinner.value() for form, checkbox, spinner in
                          zip(self.form_checkboxes.keys(), self.form_checkboxes.values(), self.form_spinners.values())
                          if checkbox.isChecked() and spinner.value() > 0}

        if not selected_forms:
            QMessageBox.warning(self, "Brak wybranych formularzy",
                                "Proszę wybrać przynajmniej jeden dokument\n"
                                " oraz określić ilość kopii")
            return
        else:
            print(selected_forms)


        self.next_window = SecondWindow(selected_forms)
        self.next_window.show()
        self.close()

    def menu_btn_clicked(self):
        pass

    def clear_checkboxes(self):
        # Odznacz wszystkie checkboxy
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)
        self.chosen_forms.clear()


# Run the application
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
