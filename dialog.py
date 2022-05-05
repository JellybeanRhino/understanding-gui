#dialog.py
#Rhiannon MacCreadie
#04/05/2022
# Dialog example

import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QDialog')
window.setGeometry(600, 600, 400, 200)

window.setCentralWidget(QtWidgets.QWidget())

dlgLayout = QtWidgets.QVBoxLayout()
layout = QtWidgets.QFormLayout()
window.centralWidget().setLayout(dlgLayout)

layout.addRow('Name', QtWidgets.QLineEdit())
layout.addRow("Age", QtWidgets.QLineEdit())
layout.addRow("Height", QtWidgets.QLineEdit())
layout.addRow("Weight", QtWidgets.QLineEdit())

dlgLayout.addLayout(layout)
btns = QtWidgets.QDialogButtonBox()
btns.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
dlgLayout.addWidget(btns)



window.show()
btns.show()

app.exec_()