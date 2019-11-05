import pickle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout,
        QWidget)

from SI import index,query



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
        terms = self.nameLine2.text()
        result = query.search(terms)
        print(result)
        text = ''
        for x in result:
            text = text + str(x) + '\n '
        self.addressText.setText(text)

        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)


    def myload(self):
        file = QFileDialog.getExistingDirectory(self)

        self.nameLine.setText(file)
        index.index(file)
        #self.updateInterface(self.NavigationMode)




if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())