#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
import numpy as np

class Game(QMainWindow):
    def __init__(self, FieldConstructor):
        super().__init__()
        
        self.initUI(FieldConstructor)
        
    def initUI(self, FieldConstructor):
        self.field = FieldConstructor(self)
        self.setCentralWidget(self.field)
        self.adjustSize()
        
        self.field.onWin[str].connect(self.onWin)
        self.field.onLose[str].connect(self.onLose)
        
        self.center()
        self.show()
        
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)
            
    def _showMsg(self, title, msg):
        box = QMessageBox()
        box.setWindowTitle(title)
        box.setText(msg)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()
            
    def onWin(self, msg):
        self._showMsg('Win!', msg)
        
    def onLose(self, msg):
        self._showMsg('Louse!', msg)

class Field(QFrame):
    CELL_WIDTH = 30 #px
    CELL_HEIGHT = 30 #px

    onWin = pyqtSignal(str)
    onLose = pyqtSignal(str)
    
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self._width = width
        self._height = height
        
        self.timer = QBasicTimer()
        self.setFixedSize(self.width * self.CELL_WIDTH, self.height * self.CELL_HEIGHT)
        
        self.setFocusPolicy(Qt.StrongFocus)
        self.restart()
        
    def restart(self):
        self.clear_field()
        self.timer.start(500, self)
        
    def clear_field(self):
        self.field = np.zeros((self.width, self.height), bool)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()
        
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        #show width-1 horizontal lines
        for i in range(1, self.width):
            painter.drawLine(i*self.CELL_WIDTH, 0, i*self.CELL_WIDTH, self.height*self.CELL_HEIGHT)
        
        #show height-1 vertical lines
        for i in range(1, self.height):
            painter.drawLine(0, i*self.CELL_HEIGHT, self.width*self.CELL_WIDTH, i*self.CELL_HEIGHT)
        
        painter.setFont(QFont('Decorative', 20))
        #for every cell
        for x in range(self.width):
            for y in range(self.height):
                if self.field[x, y]:
                    painter.drawText(QRect(x*self.CELL_WIDTH, y*self.CELL_HEIGHT, self.CELL_WIDTH, self.CELL_HEIGHT), Qt.AlignCenter, "*")

    def mousePressEvent(self, event):
        coordX = event.x()
        coordY = event.y()
        x = int(coordX / self.CELL_WIDTH)
        y = int(coordY / self.CELL_HEIGHT)
        self.onCellClicked(x, y)
        
    def timerEvent(self, event):
        self.onTimer()
        
    def keyPressEvent(self, event):
        self.onKeyPressed(event.key())
        
    def win(self, message):
        self.onWin.emit(message)
        
    def lose(self, message):
        self.onLose.emit(message)
                    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
        
