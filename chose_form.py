from PyQt6.QtWidgets import (
    # QApplication,
    QWidget, QLabel, QCheckBox, QHBoxLayout, QSpinBox, QMessageBox, QVBoxLayout
)
from forms_database import dict_of_fields as forms_db
# import sys


class ChoseForms(QWidget):
    def __init__(self):
        super().__init__()

        # Checkboxes and other elements
        self.form_checkboxes = {}
        self.form_spinners = {}

        self.chose_frm_layout = QVBoxLayout()

        for form_name in forms_db.keys():
            # Add forms layout
            self.row_layout = QHBoxLayout()

            # Add space on the left
            self.row_layout.addStretch(1)

            # checkbox
            checkbox = QCheckBox()
            checkbox.setObjectName(f"{form_name}_chbx")
            # added
            self.form_checkboxes[form_name] = checkbox

            self.row_layout.addWidget(checkbox)

            # Label
            self.form_title = QLabel(f"{forms_db[form_name]['description']}", self)
            #self.form_title.setObjectName(f"{form_name}_title")
            self.form_title.setFixedHeight(30)
            self.row_layout.addWidget(self.form_title)

            # Add space between label and spinbox
            self.row_layout.addStretch(1)

            # Spinbox
            spinbox = QSpinBox(self)
            spinbox.setFixedSize(60, 30)
            spinbox.setValue(1)
            spinbox.setRange(1, 10)
            # added
            self.form_spinners[form_name] = spinbox
            self.row_layout.addWidget(spinbox)

            # Add space on the right
            self.row_layout.addStretch(1)
            self.chose_frm_layout.addLayout(self.row_layout)

        self.setLayout(self.chose_frm_layout)

        # Reference to saved names
        # self.detain_chbx = self.findChild(QCheckBox, "detain_form_chbx")
        # self.warrant_chbx = self.findChild(QCheckBox, "warrant_form_chbx")
        # self.identity_chbx = self.findChild(QCheckBox, "identity_form_chbx")

    def get_forms_list(self):
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
            return selected_forms

# # Run the application
# app = QApplication(sys.argv)
# window = ChoseForms()
# window.show()
# sys.exit(app.exec())
