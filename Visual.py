import pickle
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox,
        QWidget)

from SI import index, query , helpers



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
        addressLabel.setOpenExternalLinks(True)

        self.dialog = FindDialog()

        self.addButton = QPushButton("&Run")
        self.addButton.show()

        self.pButton = QPushButton("&Precision")
        self.pButton.hide()
        self.rButton = QPushButton("&Recall")
        self.rButton.hide()
        self.FButton = QPushButton("&F-Media")
        self.FButton.hide()
        self.rpButton = QPushButton("&R-Precision")
        self.rpButton.hide()


        self.loadButton = QPushButton("&Load...")
        self.loadButton.setToolTip("Load dir from a file")

        self.addButton.clicked.connect(self.addContact)
        self.loadButton.clicked.connect(self.myload)
        self.pButton.clicked.connect(self.precision)
        self.rButton.clicked.connect(self.recall)
        self.FButton.clicked.connect(self.fmedia)
        self.rpButton.clicked.connect(self.rprecision)




        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.loadButton)
        buttonLayout1.addWidget(self.addButton, Qt.AlignTop)
        buttonLayout1.addWidget(self.pButton)
        buttonLayout1.addWidget(self.rButton)
        buttonLayout1.addWidget(self.FButton)
        buttonLayout1.addWidget(self.rpButton)

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
        text = ''
        for x in result:
            text = text + str(x) + '\n '
        self.addressText.setText(text)
        self.nameLine.setFocus(Qt.OtherFocusReason)
        self.addressText.setReadOnly(False)

        self.pButton.show()
        self.rButton.show()
        self.rpButton.show()
        self.FButton.show()

        return len(result)

    def myload(self):
        file = QFileDialog.getExistingDirectory(self)

        self.nameLine.setText(file)
        index.index(file)

        #self.updateInterface(self.NavigationMode)

    def precision(self):
        total = len(os.listdir(self.nameLine.text()))

        terms = self.nameLine2.text()
        result = query.search(terms)
        relevan = len(result)

        QMessageBox.information(self, "Precision",
                    "\"%s\""  % 'Value: ' + str(relevan/total))

        self.pButton.hide()



    def recall(self):
        total = len(os.listdir(self.nameLine.text()))

        terms = self.nameLine2.text()
        result = query.search(terms)
        relevan = len(result)

        QMessageBox.information(self, "Recall",
                    "\"%s\""  % 'Value: ' + str(total/relevan))

        self.rButton.hide()



    def fmedia(self):
        total = len(os.listdir(self.nameLine.text()))

        terms = self.nameLine2.text()
        result = query.search(terms)
        relevan = len(result)

        pre = relevan/total
        rec = total/relevan

        QMessageBox.information(self, "F-Media",
                                "\"%s\"" % 'Value: ' + str(2*((pre*rec) / (pre+rec))))
        self.FButton.hide()

    def rprecision(self):

        self.dialog.show()

        if self.dialog.exec_() == QDialog.Accepted:
            data = self.dialog.getFindText()

        terms = self.nameLine2.text()
        result = query.search(terms)
        relevan = len(result)

        QMessageBox.information(self, "R-Precision",
                                "\"%s\"" % 'Value: ' + str(int(data) / relevan))

        self.rpButton.hide()

class FindDialog(QDialog):
    def __init__(self, parent=None):
        super(FindDialog, self).__init__(parent)

        findLabel = QLabel("Enter the value un r precision")
        self.lineEdit = QLineEdit()

        self.findButton = QPushButton("&OK")

        self.findText = ''

        layout = QHBoxLayout()
        layout.addWidget(findLabel)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.findButton)

        self.setLayout(layout)
        self.setWindowTitle("Value R-Precision")

        self.findButton.clicked.connect(self.findClicked)
        self.findButton.clicked.connect(self.accept)

    def findClicked(self):
        text = self.lineEdit.text()

        if not text:
            QMessageBox.information(self, "Empty Field",
                    "Please enter a name.")
            return
        else:
            self.findText = text
            self.lineEdit.clear()
            self.hide()

    def getFindText(self):
        return self.findText
if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())