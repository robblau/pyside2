#!/usr/bin/python
import unittest, os
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtSvg import *

class QSvgWidgetTest(unittest.TestCase):

    def testLoad(self):
        tigerPath = os.path.join(os.path.dirname(__file__), 'tiger.svg')

        app = QApplication([])
        fromFile = QSvgWidget()
        fromFile.load(tigerPath)
        self.assertTrue(fromFile.renderer().isValid())

        tigerFile = QFile(tigerPath)
        tigerFile.open(QFile.ReadOnly)
        tigerData = tigerFile.readAll()
        fromContents = QSvgWidget()
        fromContents.load(tigerData)
        self.assertTrue(fromContents.renderer().isValid())

if __name__ == '__main__':
    unittest.main()

