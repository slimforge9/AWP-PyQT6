from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QComboBox, QLabel, QTextEdit, QMessageBox, QFileDialog
)
from profile_editor import ProfileEditor
import os


class ProfileWindow(QDialog):
    """
    This pop-up window adds option to change profiles where are stored const values like police_station_name,
    officer_name or city where document is created
    """
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("Profile Management")
        self.WIDTH = 300
        self.HEIGHT = 200
        self.POS_X = parent.POS_X + int(self.WIDTH/2)
        self.POS_Y = parent.POS_Y + int(self.HEIGHT/2)

        self.setGeometry(self.POS_X, self.POS_Y, self.WIDTH, self.HEIGHT)
        self.profiles = {}  # Przechowuje profile w formie słownika
        self.load_profiles()  # Wczytanie zapisanych profili z pliku

        # Layout
        layout = QVBoxLayout(self)

        # Dropdown (ComboBox) na profile
        self.profile_dropdown = QComboBox(self)
        self.update_dropdown()
        layout.addWidget(self.profile_dropdown)

        # Przycisk "Nowy"
        self.new_button = QPushButton("Nowy", self)
        self.new_button.clicked.connect(self.create_new_profile)
        layout.addWidget(self.new_button)

        # Przycisk "Edytuj"
        self.edit_button = QPushButton("Edytuj", self)
        self.edit_button.clicked.connect(self.edit_profile)
        layout.addWidget(self.edit_button)

        # Przycisk "Usuń"
        self.delete_button = QPushButton("Usuń", self)
        self.delete_button.clicked.connect(self.delete_profile)
        layout.addWidget(self.delete_button)

    def get_loaded_profiles(self):
        return self.profiles

    def load_profiles(self):
        """Wczytuje profile z pliku"""
        if os.path.exists('profiles.txt'):
            with open('profiles.txt', 'r') as file:
                for line in file:
                    name, supervisor, unit, location = line.strip().split(',')
                    self.profiles[name] = {
                        'stopien_imie_nazwisko': name,
                        'przelozony': supervisor,
                        'jednostka': unit,
                        'miejscowosc': location
                    }
        print(self.profiles)

    def save_profiles(self):
        """Zapisuje profile do pliku"""
        with open('profiles.txt', 'w') as file:
            for profile, data in self.profiles.items():
                file.write(f"{data['stopien_imie_nazwisko']},{data['przelozony']},{data['jednostka']},{data['miejscowosc']}\n")

    def update_dropdown(self):
        """Aktualizuje rozwijane menu profili"""
        self.profile_dropdown.clear()
        self.profile_dropdown.addItems(self.profiles.keys())

    def create_new_profile(self):
        """Otwiera okno tworzenia nowego profilu"""
        self.profile_editor = ProfileEditor(self, new=True)
        self.profile_editor.show()

    def edit_profile(self):
        """Otwiera okno edycji istniejącego profilu"""
        current_profile = self.profile_dropdown.currentText()
        if current_profile:
            self.profile_editor = ProfileEditor(self, profile=self.profiles[current_profile], new=False)
            self.profile_editor.show()

    def delete_profile(self):
        """Usuwa wybrany profil"""
        current_profile = self.profile_dropdown.currentText()
        if current_profile:
            del self.profiles[current_profile]
            self.save_profiles()
            self.update_dropdown()
            QMessageBox.information(self, "Sukces", "Profil został usunięty.")
