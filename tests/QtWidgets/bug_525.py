import unittest
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMenu

class M2(QMenu):
    def __init__(self,parent=None):
        super(M2,self).__init__(parent)
        self.setTitle(self.tr("M2"))

class TestMenuDerivedClass(unittest.TestCase):
    def aboutToShowHandler(self):
        pass

    def testConnectSignal(self):
        app = QApplication([])
        m2 = M2()
        # Test if the aboutToShow signal was translated to correct type
        m2.aboutToShow.connect(self.aboutToShowHandler)

if __name__ == '__main__':
    unittest.main()
