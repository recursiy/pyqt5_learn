#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
import numpy as np
from field import Field, Game

class MyField(Field):
    XMatrix = np.array([
        [True, False, False, False, True],
        [False, True, False, True, False],
        [False, False, True, False, False],
        [False, True, False, True, False],
        [True, False, False, False, True]
    ], bool)

    def __init__(self, parent):
        super().__init__(parent, 5, 5)  #CHANGE SIZE HERE
        
    def onCellClicked(self, x, y):
        self.field[x, y] = not self.field[x, y]
        if np.array_equal(self.field, self.XMatrix):
            self.win('Yeap!')
            
        self.repaint()
        
    def onTimer(self):
        pass
        
    def onKeyPressed(self, key):
        pass
        
if __name__ == '__main__':

    app = QApplication([])
    game = Game(MyField)
    sys.exit(app.exec_())