from PyQt6.QtWidgets import (QListWidget,QTextEdit,
    QApplication, QWidget, QLabel, QPushButton, QSlider, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame,
    QSpacerItem, QSizePolicy, QScrollArea
)
from forms_database import dict_of_fields as forms_db
import flattened_list


class FillForms(QWidget):
    def __init__(self, items):
        super().__init__()
        self.items = items

        # Get required list of fields for each form
        self.list_of_fields = flattened_list.get_list(self.items)
        self.initUI()

    def initUI(self):

        # Tworzenie głównego układu dla okna
        main_layout = QVBoxLayout(self)

        # Tworzenie scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Tworzenie widgetu w scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # Create one QFrame for one chosen form
        for form in self.items.keys():

            # Create QFrame to separate each form
            frame_for_each_form = QFrame()
            frame_for_each_form.setFrameShape(QFrame.Shape.Box)
            frame_for_each_form.setStyleSheet("QFrame {border: 2px solid blue;}")
            frame_layout = QVBoxLayout(frame_for_each_form)

            # Create first label as a form title
            title_label = QLabel(f'{forms_db[form]["description"]}')
            frame_layout.addWidget(title_label)

            # Add labels for scroll example
            for _ in range(10):
                # Create vertical layout for widgets
                one_line_field_layout = QHBoxLayout()

                # Create widgets
                label = QLabel("testowy label")
                label.setStyleSheet("border: 1px none;")
                line_edit = QLineEdit()

                label2 = QLabel("testowy label")
                label2.setStyleSheet("border: 1px none;")
                line_edit2 = QLineEdit()

                # Add widgets to horizontal layout
                one_line_field_layout.addWidget(label)
                one_line_field_layout.addWidget(line_edit)
                one_line_field_layout.addWidget(label2)
                one_line_field_layout.addWidget(line_edit2)

                # Add horizontal layout to frame layout
                frame_layout.addLayout(one_line_field_layout)

            # Add frames to scroll layout
            scroll_layout.addWidget(frame_for_each_form)

        # Add scroll wdiget to scroll area
        scroll_area.setWidget(scroll_widget)

        # Add scroll area to main layout
        main_layout.addWidget(scroll_area)
