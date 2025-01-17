# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(708, 378)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 681, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.kebabLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.kebabLabel.setStyleSheet("font-weight: bold;")
        self.kebabLabel.setObjectName("kebabLabel")
        self.gridLayout.addWidget(self.kebabLabel, 1, 0, 1, 1)
        self.kremowkaSpin = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.kremowkaSpin.setMinimumSize(QtCore.QSize(150, 0))
        self.kremowkaSpin.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.kremowkaSpin.setObjectName("kremowkaSpin")
        self.gridLayout.addWidget(self.kremowkaSpin, 0, 1, 1, 1)
        self.kremowkaPrice = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kremowkaPrice.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaPrice.setObjectName("kremowkaPrice")
        self.gridLayout.addWidget(self.kremowkaPrice, 0, 2, 1, 1)
        self.kebabSpin = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.kebabSpin.setMinimumSize(QtCore.QSize(150, 0))
        self.kebabSpin.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kebabSpin.setObjectName("kebabSpin")
        self.gridLayout.addWidget(self.kebabSpin, 1, 1, 1, 1)
        self.kremowkaLabel = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.kremowkaLabel.setStyleSheet("font-weight: bold;")
        self.kremowkaLabel.setObjectName("kremowkaLabel")
        self.gridLayout.addWidget(self.kremowkaLabel, 0, 0, 1, 1)
        self.kremowkaSum = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kremowkaSum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kremowkaSum.setObjectName("kremowkaSum")
        self.gridLayout.addWidget(self.kremowkaSum, 0, 3, 1, 1)
        self.kebabPrice = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kebabPrice.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kebabPrice.setObjectName("kebabPrice")
        self.gridLayout.addWidget(self.kebabPrice, 1, 2, 1, 1)
        self.kebabSum = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.kebabSum.setMaximumSize(QtCore.QSize(150, 16777215))
        self.kebabSum.setObjectName("kebabSum")
        self.gridLayout.addWidget(self.kebabSum, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.kebabLabel.setText(_translate("Dialog", "Kula mocy"))
        self.kremowkaPrice.setPlaceholderText(_translate("Dialog", "cena za sztuke"))
        self.kremowkaLabel.setText(_translate("Dialog", "Kremówki"))
        self.kremowkaSum.setPlaceholderText(_translate("Dialog", "razem"))
        self.kebabPrice.setPlaceholderText(_translate("Dialog", "cena za kilogram"))
        self.kebabSum.setPlaceholderText(_translate("Dialog", "razem"))
