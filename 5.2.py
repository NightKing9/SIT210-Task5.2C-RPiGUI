import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import RPi.GPIO as GPIO

red = 18
green = 24
blue = 8

def setupCircuit():
    print(red, green, blue)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(blue, GPIO.OUT)
    
def ledOn(command):
    if command == "red":
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
            
    elif command == "green":
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(blue, GPIO.LOW)
            
    elif command == "blue":
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.HIGH)
            
    else:
        print("All LEDs are off")
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
    
def gpioClear():
    GPIO.cleanup()

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = '5.2C RPi - LEDs Lights Controller'
        self.x = 800
        self.y = 400
        self.width = 500
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        
        self.createAppLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        
        buttonExit = QPushButton('Exit', self)
        buttonExit.clicked.connect(self.exit_click)
        windowLayout.addWidget(buttonExit)
        
        self.setLayout(windowLayout)
        
        self.show()
    
    def createAppLayout(self):
        self.horizontalGroupBox = QGroupBox("Which LED light would you like to turn on?")
        layout = QHBoxLayout()
        
        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(self.red_on_click)
        layout.addWidget(buttonRed)
        
        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(self.green_on_click)
        layout.addWidget(buttonGreen)
        
        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(self.blue_on_click)
        layout.addWidget(buttonBlue)
        
        self.horizontalGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def red_on_click(self):
        print("Red LED is ON!")
        ledOn("red")
        
    def green_on_click(self):
        print("Green LED is ON!")
        ledOn("green")
        
    def blue_on_click(self):
        print("Blue LED is ON!")
        ledOn("blue")
    
    def exit_click(self):
        ledOn("off")
        print("Exiting GUI . . . ")
        gpioClear()
        self.close()
    
if __name__ == '__main__':
    setupCircuit()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())