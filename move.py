#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
import numpy as np
from field import Field, Game

class MyField(Field):
    def __init__(self, parent):
        super().__init__(parent, 10, 10)  #CHANGE SIZE HERE
        self.position = (0, 0)
        self.field[self.position[0], self.position[1]] = True
        self.repaint()
        
    def onCellClicked(self, x, y):
        pass
        
    def onTimer(self):
        pass
        
    def onKeyPressed(self, key):
        #затереть предыдущее
        self.field[self.position[0], self.position[1]] = False
        #вычислить новую позицию
        if key == Qt.Key_Left:
            if self.position[0] > 0:
                self.position = (self.position[0] - 1, self.position[1])
            else:
                pass    #do nothing
        elif key == Qt.Key_Right:
            if self.position[0] < self.width - 1:
                self.position = (self.position[0] + 1, self.position[1])
        elif key == Qt.Key_Up:
            if self.position[1] > 0:
                self.position = (self.position[0], self.position[1] - 1)
        elif key == Qt.Key_Down:
            if self.position[1] < self.height - 1:
                self.position = (self.position[0], self.position[1] + 1)
        
        #показать на новой позиции
        self.field[self.position[0], self.position[1]] = True
        self.repaint()
        
        if self.position == (9, 9):
            self.win('You win!')
        
if __name__ == '__main__':

    app = QApplication([])
    game = Game(MyField)
    sys.exit(app.exec_())