from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget


class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)

        nameLabel = QLabel("Path:")
        self.nameLine = QLineEdit()
        self.nameLine.setReadOnly(True)

        nameLabel2 = QLabel("Query:")
        self.nameLine2 = QLineEdit()

        addressLabel = QLabel("Result:")
        self.addressText = QTextEdit()


        self.addButton = QPushButton("&Run")
        self.addButton.show()

        self.addButton.clicked.connect(self.addContact)

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.addButton, Qt.AlignTop)
        buttonLayout1.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLabel2, 1, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(self.nameLine2, 1, 1)
        mainLayout.addWidget(addressLabel, 2, 0, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 2, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Information Retrieval")

    def addContact(self):

        self.nameLine.clear()
        self.addressText.clear()

        self.nameLine.setReadOnly(False)
        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)



if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())