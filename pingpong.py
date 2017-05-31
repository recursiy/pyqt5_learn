#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
import numpy as np
from field import Field, Game


class MyField(Field):
    def __init__(self, parent):
        super().__init__(parent, 4, 4)  # CHANGE SIZE HERE
        self.position = np.array([0, 2])
        self.field[self.position[0], self.position[1]] = True
        self.move = np.array([-1, 0])  #moved right
        
    def _reverse(self, vector):
        #returns vector with changed direction up to 180 degrees
        return -vector
        
    def onTimer(self):
        #clear current position
        self.field[self.position[0], self.position[1]] = False
        
        #calculate next move vector
        if self.position[0] == 0 or self.position[0] == self.width-1:
            #we arrived to left border, next move must be to the left
            #or we arrived to right border
            self.move = self._reverse(self.move)
            
        #calculate new position
        self.position += self.move
        
        #draw * at new position
        self.field[self.position[0], self.position[1]] = True
        self.repaint()

if __name__ == '__main__':
    app = QApplication([])
    game = Game(MyField)
    sys.exit(app.exec_())