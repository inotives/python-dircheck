'''
Created on Sep 3, 2013

@author: t_tonit
'''
from PyQt4 import QtGui, QtCore, uic
import sys
    
def load_main_ui(uicomponent):
    uicomponent = QtGui.QWidget()
    uic.loadUi('ui/main.ui', uicomponent)
    uicomponent.show()
    
if __name__ == '__main__':
    #show UI
    app = QtGui.QApplication(sys.argv)
    load_main_ui(app)
    sys.exit(app.exec_())