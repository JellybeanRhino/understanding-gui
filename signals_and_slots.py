#signals_and_slots.py
#Rhiannon MacCreadie
#04/05/2022
#  Main Window example

import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
# Menu
window = QtWidgets.QMainWindow()
window.setWindowTitle('signals and slots')
window.setGeometry(600, 600, 400, 200)

window.setCentralWidget(QtWidgets.QWidget())

menuBar = window.menuBar()
menu = QtWidgets.QMenu("Main Menu", window)
menuBar.addMenu(menu)

toolbar = QtWidgets.QToolBar()
window.addToolBar(toolbar)
toolbar.addAction('Exit', window.close)

status = QtWidgets.QStatusBar()
status.showMessage("Here is the status bar")
window.setStatusBar(status)

#Signals and Slots
def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
        
    else:
        msg.setText("Hello World!")
    
    msg.show()

layout = QtWidgets.QVBoxLayout()
window.centralWidget().setLayout(layout)

btn = QtWidgets.QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()
msg = QtWidgets.QLabel('')
layout.addWidget(btn)
layout.addWidget(msg)


window.setLayout(layout)

window.show()
btn.show()


app.exec_()