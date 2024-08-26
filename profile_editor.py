from PyQt6.QtWidgets import (
    QDialog, QLabel, QPushButton, QTextEdit, QVBoxLayout, QMessageBox
)


class ProfileEditor(QDialog):
    def __init__(self, parent, profile=None, new=True):
        super().__init__(parent)
        self.setWindowTitle("Edytor Profilu" if not new else "Nowy Profil")
        self.setGeometry(100, 100, 400, 300)
        self.parent = parent
        self.new = new

        # Profile fields
        self.fields = {
            'stopien_imie_nazwisko': QTextEdit(self),
            'przelozony': QTextEdit(self),
            'jednostka': QTextEdit(self),
            'miejscowosc': QTextEdit(self),
            'miejscowosc2': QTextEdit(self)
        }

        # Layout
        layout = QVBoxLayout(self)

        # Add field with QLabel and QTextEdit for each field
        for label_text, field in self.fields.items():
            label = QLabel(label_text.replace('_', ' ').capitalize(), self)
            layout.addWidget(label)
            layout.addWidget(field)

        # If editing, fill fields with current profile data
        if profile:
            for key, value in profile.items():
                self.fields[key].setText(value)

        # Save button
        self.save_button = QPushButton("Zapisz", self)
        self.save_button.clicked.connect(self.save_profile)
        layout.addWidget(self.save_button)

    def save_profile(self):
        """Zapisuje nowy lub edytowany profil"""
        profile_data = {key: field.toPlainText() for key, field in self.fields.items()}

        # Validacja czy wszystkie pola są wypełnione
        if all(profile_data.values()):
            if self.new:
                # Dodaj nowy profil
                self.parent.profiles[profile_data['stopien_imie_nazwisko']] = profile_data
            else:
                # Zaktualizuj istniejący profil
                current_profile = self.parent.profile_dropdown.currentText()
                self.parent.profiles[current_profile] = profile_data

            self.parent.save_profiles()
            self.parent.update_dropdown()
            self.close()
            QMessageBox.information(self, "Sukces", "Profil został zapisany.")
        else:
            QMessageBox.warning(self, "Błąd", "Wszystkie pola muszą być wypełnione.")
