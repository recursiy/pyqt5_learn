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
        super().__init__(parent, 8, 10)  #CHANGE SIZE HERE
        self.direction = 'down'
        
    def onCellClicked(self, x, y):
        self.field[x, y] = not self.field[x, y]
        self.repaint()
        
    def onTimer(self):
        if self.direction == 'down':
            for x in range(self.width):
                for y in range(self.height-1, 0, -1):
                    self.field[x, y] = self.field[x, y-1]
                    
            for x in range(self.width):
                self.field[x, 0] = False
                
        elif self.direction == 'up':
            for x in range(self.width):
                for y in range(self.height-1):
                    self.field[x, y] = self.field[x, y+1]
                    
            for x in range(self.width):
                self.field[x, self.height-1] = False
                
        elif self.direction == 'left':
            for x in range(self.width-1):
                for y in range(self.height):
                    self.field[x, y] = self.field[x+1, y]
                    
            for y in range(self.height):
                self.field[self.width-1, y] = False
                
        elif self.direction == 'right':
            for x in range(self.width-1, 0, -1):
                for y in range(self.height):
                    self.field[x, y] = self.field[x-1, y]
                    
            for y in range(self.height):
                self.field[0, y] = False
            
        self.repaint()
        
    def onKeyPressed(self, key):
        if key == Qt.Key_Left:
            self.direction = 'left'
        elif key == Qt.Key_Right:
            self.direction = 'right'
        elif key == Qt.Key_Up:
            self.direction = 'up'
        elif key == Qt.Key_Down:
            self.direction = 'down'
        
if __name__ == '__main__':

    app = QApplication([])
    game = Game(MyField)
    sys.exit(app.exec_())