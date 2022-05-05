#main_menu.py
#Rhiannon MacCreadie
#04/05/2022
#  Main Window example

import sys
from PySide6 import QtWidgets

app = QtWidgets.QApplication()

window = QtWidgets.QMainWindow()
window.setWindowTitle('Qmainmenu')
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


window.show()


app.exec_()