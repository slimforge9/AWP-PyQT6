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

        for chbx_object in forms_db.keys():
            # Add forms layout
            self.row_layout = QHBoxLayout()

            # Add space on the left
            self.row_layout.addStretch(1)

            # Checkbox
            checkbox = QCheckBox(f"{forms_db[chbx_object]['description']}")
            checkbox.setObjectName(f"{chbx_object}_chbx")
            self.row_layout.addWidget(checkbox)

            # Add checkbox references
            self.form_checkboxes[chbx_object] = checkbox

            # Add space between label and spinbox
            self.row_layout.addStretch(1)

            # Spinbox
            spinbox = QSpinBox(self)
            spinbox.setFixedSize(60, 30)
            spinbox.setValue(1)
            spinbox.setRange(1, 10)

            if chbx_object == 'detain_form':
                spinbox.setValue(3)

            # added
            self.form_spinners[chbx_object] = spinbox
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

    def clear_checkboxes(self):
        for chbx_object in self.form_checkboxes.values():
            chbx_object.setChecked(False)

