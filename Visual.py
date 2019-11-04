import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout,
        QWidget)

from SI import index


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

        self.loadButton = QPushButton("&Load...")
        self.loadButton.setToolTip("Load dir from a file")

        self.addButton.clicked.connect(self.addContact)
        self.loadButton.clicked.connect(self.myload)

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.loadButton)
        buttonLayout1.addWidget(self.addButton, Qt.AlignTop)
        buttonLayout1.addStretch()

        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLabel2, 1, 0)
        mainLayout.addWidget(self.nameLine, 0, 1)
        mainLayout.addWidget(self.nameLine2, 1, 1)
        mainLayout.addWidget(addressLabel, 2, 0, Qt.AlignTop)
        mainLayout.addWidget(self.addressText, 2, 1)
        mainLayout.addLayout(buttonLayout1, 2, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Information Retrieval")

    def addContact(self):

        self.nameLine.clear()
        self.addressText.clear()

        self.nameLine.setReadOnly(False)
        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)


    def myload(self):
        file = QFileDialog.getExistingDirectory(self)
        print(file)

        #self.updateInterface(self.NavigationMode)

    def loadFromFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Address Book",
                                                  '', "Address Book (*.abk);;All Files (*)")


        if not fileName:
            return

        try:
            in_file = open(str(fileName), 'rb')
        except IOError:
            QMessageBox.information(self, "Unable to open file",
                                    "There was an error opening \"%s\"" % fileName)
            return

        self.contacts = pickle.load(in_file)
        in_file.close()

        if len(self.contacts) == 0:
            QMessageBox.information(self, "No contacts in file",
                                    "The file you are attempting to open contains no "
                                    "contacts.")
        else:
            for name, address in self.contacts:
                self.nameLine.setText(name)
                self.addressText.setText(address)

        self.updateInterface(self.NavigationMode)


if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())