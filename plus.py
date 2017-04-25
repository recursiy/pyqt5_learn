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
        super().__init__(parent, 4, 4)  #CHANGE SIZE HERE
        self.step = 0   #left-right-right
        self.position = np.array([1, 1])
        
        self.move = np.array([1, 0])  #moved right
        
    def onCellClicked(self, x, y):
        pass
        
    def _turn_left(self, move):
        return np.cross(np.array([self.move[0], self.move[1], 0]), np.array([0, 0, 1]))[:2]
        
    def _turn_right(self, move):
        return np.cross(np.array([self.move[0], self.move[1], 0]), np.array([0, 0, -1]))[:2]
        
    def onTimer(self):
        if self.step > 0:
            self.move = self._turn_right(self.move)
        else:
            self.move = self._turn_left(self.move)
        self.position = self.position + self.move
        self.field[self.position[0], self.position[1]] = not self.field[self.position[0], self.position[1]]
        self.step += 1
        if self.step > 2:
            self.step = 0
        self.repaint()
        
    def onKeyPressed(self, key):
        pass
        
if __name__ == '__main__':

    app = QApplication([])
    game = Game(MyField)
    sys.exit(app.exec_())