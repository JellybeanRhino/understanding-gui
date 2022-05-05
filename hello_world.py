#hello_world.py
#Rhiannon MacCreadie
#04.05.2022
#A basic PyQt application that shows the phrase 'Hello World!' 

# Import System
import sys\
# Imort 'QApplication' and all the required wdigets
from PySide6 import QtWidgets

# Create an instance of QApplication 
app = QtWidgets.QApplication()

# Create an instance of yoru application's GUi
# Create window shell
window = QtWidgets.QMainWindow()
# Add a Title to the application title
window.setWindowTitle('PyQt6 App')
# Define size of window format position x, y size width, height
window.setGeometry(100,100,270,80)
# Place coordinate
window.move(60,15)
# Write phrase
helloMsg = QtWidgets.QLabel('<h1>Hello World!</h1>', parent = window)
# Set dimensions
helloMsg.setMinimumWidth(270)
# Place message in coordiante
helloMsg.move(60,15)




# Show application
window.show()

# Run as a event Loop
app.exec_()
