from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenu, QMenuBar, QFileDialog, QMessageBox
import file as f

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.fname = None

        # Creating MenuBar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Open", self.menu_action_clicked)

        self.setWindowTitle('Python')
        v_layout = QVBoxLayout()
        self.btn1 = QtWidgets.QPushButton('Words')
        self.btn1.setStyleSheet("background-color: rgb(150,150,150);")
        self.btn2 = QtWidgets.QPushButton('Letters')
        self.btn2.setStyleSheet("background-color: rgb(150,150,150);")
        self.btn3 = QtWidgets.QPushButton('Sentences')
        self.btn3.setStyleSheet("background-color: rgb(150,150,150);")
        self.btn4 = QtWidgets.QPushButton('maxWord')
        self.btn4.setStyleSheet("background-color: rgb(150,150,150);")
        self.btn5 = QtWidgets.QPushButton('maxLetter')
        self.btn5.setStyleSheet("background-color: rgb(150,150,150);")
        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.btn2)
        v_layout.addWidget(self.btn3)
        v_layout.addWidget(self.btn4)
        v_layout.addWidget(self.btn5)
        
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)
        self.btn1.clicked.connect(self.clickedWords)
        self.btn2.clicked.connect(self.clickedLetters)
        self.btn3.clicked.connect(self.clickedSentences)
        self.btn4.clicked.connect(self.clickedMaxWord)
        self.btn5.clicked.connect(self.clickedMaxLetter)
        

        # Error box
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setText("File will be ended for .txt: ")
        self.error.setIcon(QMessageBox.Warning)
        
    @QtCore.pyqtSlot()
    def menu_action_clicked(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        if ".txt" not in self.fname:
            self.error.exec_()


    def clickedWords(self):
        if self.fname == "" or self.fname == None:
            self.error.setText("Not valid File!    ")
            self.error.setInformativeText("File does not given!   ")
            self.error.exec_()
        else:
            message = f"Count of Words is {self.words()}"
            QMessageBox.about(self, "", message) 

    def clickedLetters(self):   
        if self.fname == "" or self.fname == None:
            self.error.setText("Not valid File!    ")
            self.error.setInformativeText("File does not given!   ")
            self.error.exec_()
        else:
            message = f"Count of Letters is {self.letters()}"
            QMessageBox.about(self, "", message)

    def clickedSentences(self):
        if self.fname == "" or self.fname == None:
            self.error.setText("Not valid File!    ")
            self.error.setInformativeText("File does not given!   ")
            self.error.exec_()
        else:
            message = f"Count of Sentences is {self.sentences()}"
            QMessageBox.about(self, "", message)

    def clickedMaxWord(self):
        if self.fname == "" or self.fname == None:
            self.error.setText("Not valid File!    ")
            self.error.setInformativeText("File does not given!   ")
            self.error.exec_()
        else:
            message = f"Maximum word is {self.maxWord()}"
            QMessageBox.about(self, "", message)

    def clickedMaxLetter(self):
        if self.fname == "" or self.fname == None:
            self.error.setText("Not valid File!    ")
            self.error.setInformativeText("File does not given!   ")
            self.error.exec_()
        else:
            message = f"Max letter is {self.maxLetter()}"
            QMessageBox.about(self, "", message)                                    

    def words(self):
        return f.countOfWords(self.fname)
               
    def letters(self):
        return f.countOfLetters(self.fname)

    def sentences(self):
        return f.countOfSentences(self.fname)    

    def maxLetter(self):
        return f.maxLetter(self.fname)

    def maxWord(self):
        return f.maxWord(self.fname)       

app = QApplication([])
window = Window()
window.show()
app.exec_()