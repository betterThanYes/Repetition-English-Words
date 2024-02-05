# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from model import WordsModel


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Word Manager")
        self.resize(550*2, 250*2)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.wordsModel = WordsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.wordsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteWord)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearWords)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.wordsModel.addWord(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteWord(self):
        """Delete the selected contact from the database."""

        selectedIdx = self.table.selectedIndexes()

        # if row < 0:
        #     return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            list_row = []
            for index in selectedIdx:
                row = index.row()
                list_row.append(row)
                print("sdf " ,row)
            rows = list(set(list_row))
            rows = sorted(rows)
            print("rows : ", len(rows))
            for row in rows : 
                print("delete, ", row)
                id_row = rows.index(row)
                self.wordsModel.deleteWord(row-id_row)


    def clearWords(self):
        """Remove all contacts from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.wordsModel.clearWords()


class AddDialog(QDialog):
    """Add Contact dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Word")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI."""
        # Create line edits for data fields
        self.definitionField = QLineEdit()
        self.definitionField.setObjectName("definition")
        self.wordField = QLineEdit()
        self.wordField.setObjectName("word")
        self.phoneticField = QLineEdit()
        self.phoneticField.setObjectName("spelling")
        self.levelField = QLineEdit()
        self.levelField.setObjectName("http_audio")
        self.exampleField = QLineEdit()
        self.exampleField.setObjectName("example")
        

        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Word:", self.wordField)
        layout.addRow("Definition:", self.definitionField)
        layout.addRow("Phonetic:", self.phoneticField)
        layout.addRow("Level:",self.levelField)
        layout.addRow("Example:",self.exampleField)
        self.layout.addLayout(layout)

        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.wordField, self.definitionField, self.phoneticField, self.levelField , self.exampleField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        super().accept()
