#!/usr/bin/python
# -*- coding: utf-8 -*-

# Test case for PySide bug 814
# http://bugs.pyside.org/show_bug.cgi?id=814
# archive:
# https://srinikom.github.io/pyside-bz-archive/814.html
# 2011-04-08 Thomas Perl <m@thp.io>
# Released under the same terms as PySide itself

import unittest

from helper import adjust_filename, TimedQApplication

from PySide2.QtCore import QUrl, QAbstractListModel, QModelIndex
from PySide2.QtQuick import QQuickView

class ListModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.setRoleNames({0: 'pysideModelData'})

    def rowCount(self, parent=QModelIndex()):
        return 3

    def data(self, index, role):
        if index.isValid() and role == 0:
            return 'blubb'
        return None

class TestBug814(TimedQApplication):
    def testAbstractItemModelTransferToQML(self):
        view = QQuickView()
        view.setSource(QUrl.fromLocalFile(adjust_filename('bug_814.qml', __file__)))
        root = view.rootObject()
        model = ListModel()
        root.setProperty('model', model)
        view.show()

if __name__ == '__main__':
    unittest.main()

