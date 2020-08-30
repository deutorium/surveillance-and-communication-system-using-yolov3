import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import client_gui, clientSetup
from networking import client
import threading
import random

class main(QtWidgets.QMainWindow, client_gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.setupWidget = QtWidgets.QWidget(self)
        self.config = clientSetup.Ui_Form()
        self.config.setupUi(self.setupWidget)
        self.show()

       
        self.centralwidget.setHidden(True)

        
        self.hostname = "127.0.0.1"
        self.port = 8080
        self.nickname = "User " + str(random.randint(1, 1000))      

        # connect the slot method "self.start" to its signals
        self.config.hostnameField.returnPressed.connect(self.start)     
        self.config.portNoField.returnPressed.connect(self.start)       
        self.config.nicknameField.returnPressed.connect(self.start)    
        self.config.connectButton.clicked.connect(self.start)          

    def start(self):
       
        if self.config.hostnameField.text() != "":
          
            self.hostname = self.config.hostnameField.text()
        if self.config.portNoField.text() != "":
            
            self.port = self.config.portNoField.text()
        if self.config.nicknameField.text() != "":
            
            self.nickname = self.config.nicknameField.text()

        self.setWindowTitle(self.nickname + "'s chat")      
        self.receivedMessages.append("Department " + self.nickname)       

        print("Department ----:", self.nickname)    
        print("Hostname: ---:", self.hostname)      
        print("Port number -:", self.port)          

        
        self.client = client.Client(self.hostname, self.port, self.sendBtn, self.nickname, self.messageEdit, self.receivedMessages)
        self.client.start()     # call method inherited from QThread to thread run method in client

 
        self.setupWidget.setHidden(True)
       
        self.centralwidget.setVisible(True)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main()        
    sys.exit(app.exec())        
