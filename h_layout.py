#h_layout.py
#Rhiannon MacCreadie
#04/05/2022
# Practice horizontal Layouts

import sys

from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('QHBoxLayout')
window.setGeometry(600, 600, 500, 200)

window.setCentralWidget(QtWidgets.QWidget())

#Create a QHBoxLayout object layout
layout = QtWidgets.QHBoxLayout()
#Set layout
window.centralWidget().setLayout(layout)

#Create Button One
button1 = QtWidgets.QPushButton("Left")
#Enter Button One to layout
layout.addWidget(button1)

#Create Button Two
button2 = QtWidgets.QPushButton("Centre")
#Enter Button Two to layout
layout.addWidget(button2)

#create Button Three
button3 = QtWidgets.QPushButton("Right")
#Enter Button Three to layout
layout.addWidget(button3)


# Show window
window.show()
# Show Buttons
button1.show()
button2.show()
button3.show()


app.exec_()


