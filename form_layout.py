#form_layout.py
#Rhiannon MacCreadie
#04/05/2022
# Form Layout example

import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QForm')
window.setGeometry(600, 600, 400, 200)

window.setCentralWidget(QtWidgets.QWidget())

layout = QtWidgets.QFormLayout()
window.centralWidget().setLayout(layout)

layout.addRow('Name', QtWidgets.QLineEdit())
layout.addRow("age", QtWidgets.QLineEdit())
layout.addRow("height", QtWidgets.QLineEdit())
layout.addRow("weight", QtWidgets.QLineEdit())


window.setLayout(layout)

window.show()



app.exec_()