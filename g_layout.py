#g_layout.py
#Rhiannon MacCreadie
#04/05/2022
# Grid Layout example
import sys

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QGrid')
window.setGeometry(600, 600, 400, 200)

window.setCentralWidget(QtWidgets.QWidget())

layout = QtWidgets.QGridLayout()
window.centralWidget().setLayout(layout)

button1 = QtWidgets.QPushButton('Button (0, 0)')
layout.addWidget(button1, 0, 0)
button2 = QtWidgets.QPushButton('Button (0, 1)')
layout.addWidget(button2,0, 1)
button3 = QtWidgets.QPushButton('Button (0, 2)')
layout.addWidget(button3,0, 2)
button4 = QtWidgets.QPushButton('Button (1, 0)')
layout.addWidget(button4,1, 0)
button5 = QtWidgets.QPushButton('Button (1, 1)')
layout.addWidget(button5,1, 1)
button6 = QtWidgets.QPushButton('Button (1, 2)')
layout.addWidget(button6,1, 2)
button7 = QtWidgets.QPushButton('Button (2, 0)')
layout.addWidget(button7,2, 0)
button8 = QtWidgets.QPushButton('Button (2, 1) + 2 Columns Span')
layout.addWidget(button8,2,1,1,2)


window.setLayout(layout)

window.show()
button1.show()
button2.show()
button3.show()
button4.show()
button5.show()
button6.show()
button7.show()
button8.show()

app.exec_()