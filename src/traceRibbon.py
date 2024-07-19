# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'traceRibbon2gelsXo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_ribbonContainer(object):
    def setupUi(self, ribbonContainer):
        if ribbonContainer.objectName():
            ribbonContainer.setObjectName(u"ribbonContainer")
        ribbonContainer.resize(202, 759)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ribbonContainer.sizePolicy().hasHeightForWidth())
        ribbonContainer.setSizePolicy(sizePolicy)
        ribbonContainer.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(ribbonContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.traceRibbonSubContainer = QWidget(ribbonContainer)
        self.traceRibbonSubContainer.setObjectName(u"traceRibbonSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.traceRibbonSubContainer.sizePolicy().hasHeightForWidth())
        self.traceRibbonSubContainer.setSizePolicy(sizePolicy1)
        self.traceRibbonSubContainer.setStyleSheet(u"*{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"QComboBox {\n"
"    /* Add your custom styles here */\n"
"    padding-top: 0px;\n"
"    padding-bottom: 0px;\n"
"	padding-left: 10px;\n"
"	height:25;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    width: 30;\n"
"	height:25;\n"
"	 max-height: 25px;/* Adjust the value to set the desired width */\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"	text-align: right; \n"
"}\n"
"\n"
"QFrame {\n"
"    spacing: calc(max(10px, (height * 0.1))); /* adjust spacing based on window height */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #343a3c    ; /* replace with your desired color */\n"
"}\n"
"QPushButton {\n"
"text-align: left;\n"
"vertical-align: middle;\n"
"max-height: 30px;\n"
"padding-left: 10px; \n"
"height: 30px;\n"
"}\n"
"\n"
"    QFrame {\n"
"	height:30;\n"
"     /*   max-height: 30px; /* Adjust the value to set the desired minimum height */\n"
"    }\n"
"\n"
"QLabel {\n"
""
                        "        padding-left: 8px; /* Adjust the value to set the desired padding */\n"
"    }")
        self.verticalLayout = QVBoxLayout(self.traceRibbonSubContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.startingTransactionsBtn = QPushButton(self.traceRibbonSubContainer)
        self.startingTransactionsBtn.setObjectName(u"startingTransactionsBtn")
        sizePolicy1.setHeightForWidth(self.startingTransactionsBtn.sizePolicy().hasHeightForWidth())
        self.startingTransactionsBtn.setSizePolicy(sizePolicy1)
        self.startingTransactionsBtn.setMinimumSize(QSize(0, 0))
        self.startingTransactionsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startingTransactionsBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.startingTransactionsBtn)

        self.lifoBtn = QPushButton(self.traceRibbonSubContainer)
        self.lifoBtn.setObjectName(u"lifoBtn")
        sizePolicy.setHeightForWidth(self.lifoBtn.sizePolicy().hasHeightForWidth())
        self.lifoBtn.setSizePolicy(sizePolicy)
        self.lifoBtn.setMinimumSize(QSize(0, 0))
        self.lifoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lifoBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.lifoBtn)

        self.fifoBtn = QPushButton(self.traceRibbonSubContainer)
        self.fifoBtn.setObjectName(u"fifoBtn")
        sizePolicy.setHeightForWidth(self.fifoBtn.sizePolicy().hasHeightForWidth())
        self.fifoBtn.setSizePolicy(sizePolicy)
        self.fifoBtn.setMinimumSize(QSize(0, 0))
        self.fifoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fifoBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.fifoBtn)

        self.librNRBtn = QPushButton(self.traceRibbonSubContainer)
        self.librNRBtn.setObjectName(u"librNRBtn")
        sizePolicy.setHeightForWidth(self.librNRBtn.sizePolicy().hasHeightForWidth())
        self.librNRBtn.setSizePolicy(sizePolicy)
        self.librNRBtn.setMinimumSize(QSize(0, 0))
        self.librNRBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.librNRBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.librNRBtn)

        self.librRBtn = QPushButton(self.traceRibbonSubContainer)
        self.librRBtn.setObjectName(u"librRBtn")
        sizePolicy.setHeightForWidth(self.librRBtn.sizePolicy().hasHeightForWidth())
        self.librRBtn.setSizePolicy(sizePolicy)
        self.librRBtn.setMinimumSize(QSize(0, 0))
        self.librRBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.librRBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.librRBtn)

        self.poisonChaliceBtn = QPushButton(self.traceRibbonSubContainer)
        self.poisonChaliceBtn.setObjectName(u"poisonChaliceBtn")

        self.verticalLayout.addWidget(self.poisonChaliceBtn)

        self.runTracingBtn = QPushButton(self.traceRibbonSubContainer)
        self.runTracingBtn.setObjectName(u"runTracingBtn")

        self.verticalLayout.addWidget(self.runTracingBtn)

        self.startingTransactionsComboBox = QComboBox(self.traceRibbonSubContainer)
        self.startingTransactionsComboBox.setObjectName(u"startingTransactionsComboBox")
        sizePolicy1.setHeightForWidth(self.startingTransactionsComboBox.sizePolicy().hasHeightForWidth())
        self.startingTransactionsComboBox.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.startingTransactionsComboBox)

        self.showTraceLabelsBtn = QPushButton(self.traceRibbonSubContainer)
        self.showTraceLabelsBtn.setObjectName(u"showTraceLabelsBtn")

        self.verticalLayout.addWidget(self.showTraceLabelsBtn)

        self.searchTraceBtn = QPushButton(self.traceRibbonSubContainer)
        self.searchTraceBtn.setObjectName(u"searchTraceBtn")

        self.verticalLayout.addWidget(self.searchTraceBtn)

        self.applicationOfFundsBtn = QPushButton(self.traceRibbonSubContainer)
        self.applicationOfFundsBtn.setObjectName(u"applicationOfFundsBtn")

        self.verticalLayout.addWidget(self.applicationOfFundsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.uploadTraceToDBBtn = QPushButton(self.traceRibbonSubContainer)
        self.uploadTraceToDBBtn.setObjectName(u"uploadTraceToDBBtn")
        self.uploadTraceToDBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uploadTraceToDBBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.uploadTraceToDBBtn)

        self.exportTraceButton = QPushButton(self.traceRibbonSubContainer)
        self.exportTraceButton.setObjectName(u"exportTraceButton")
        self.exportTraceButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportTraceButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.exportTraceButton)


        self.horizontalLayout.addWidget(self.traceRibbonSubContainer)


        self.retranslateUi(ribbonContainer)

        QMetaObject.connectSlotsByName(ribbonContainer)
    # setupUi

    def retranslateUi(self, ribbonContainer):
        ribbonContainer.setWindowTitle(QCoreApplication.translate("ribbonContainer", u"Form", None))
        self.startingTransactionsBtn.setText(QCoreApplication.translate("ribbonContainer", u"Starting Transactions", None))
        self.lifoBtn.setText(QCoreApplication.translate("ribbonContainer", u"Last-In, First-Out", None))
        self.fifoBtn.setText(QCoreApplication.translate("ribbonContainer", u"First-In, First-Out", None))
        self.librNRBtn.setText(QCoreApplication.translate("ribbonContainer", u"LIBR (No Replenishment)", None))
        self.librRBtn.setText(QCoreApplication.translate("ribbonContainer", u"LIBR (Replenishment)", None))
        self.poisonChaliceBtn.setText(QCoreApplication.translate("ribbonContainer", u"Poisoned Chalice", None))
        self.runTracingBtn.setText(QCoreApplication.translate("ribbonContainer", u"Run Tracing", None))
        self.showTraceLabelsBtn.setText(QCoreApplication.translate("ribbonContainer", u"Show Labels", None))
        self.searchTraceBtn.setText(QCoreApplication.translate("ribbonContainer", u"Search Transaction in Trace", None))
        self.applicationOfFundsBtn.setText(QCoreApplication.translate("ribbonContainer", u"Application of Funds", None))
        self.uploadTraceToDBBtn.setText(QCoreApplication.translate("ribbonContainer", u"Upload to Database", None))
        self.exportTraceButton.setText(QCoreApplication.translate("ribbonContainer", u"Export", None))
    # retranslateUi

