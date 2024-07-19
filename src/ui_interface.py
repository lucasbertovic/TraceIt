# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceQGdcuZ.ui'
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

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 817)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4, #frame_8, #popupNotificationSubContainer, #serverDBContainer, #startingTransactionsContainer, #manualMatchesContainer, #manualUnmatchContainer, #refTableContainer, #categoriesContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainter{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color:#1f232a; /* Change to your desired color */\n"
"    color: white; /* Change to your de"
                        "sired text color */\n"
" 	 border-top: none;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-bottom: 1px solid #8cffff; /* Only lower border */\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableView::item:focus { border: 0px; }\n"
"\n"
"QTableWidget::item:focus { border: 0px; }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tracingBtn = QPushButton(self.frame_2)
        self.tracingBtn.setObjectName(u"tracingBtn")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.tracingBtn.setFont(font)
        self.tracingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tracingBtn.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton {\n"
"   background-color: #2c313c;   ; /* replace with your desired color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2c313c    ; /* replace with your desired color */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/magnifying-glass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tracingBtn.setIcon(icon1)
        self.tracingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.tracingBtn)

        self.matchingBtn = QPushButton(self.frame_2)
        self.matchingBtn.setObjectName(u"matchingBtn")
        self.matchingBtn.setFont(font)
        self.matchingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.matchingBtn.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    background-color: #2c313c    ; /* replace with your desired color */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/link-3.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.matchingBtn.setIcon(icon2)
        self.matchingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.matchingBtn)

        self.conversionBtn = QPushButton(self.frame_2)
        self.conversionBtn.setObjectName(u"conversionBtn")
        self.conversionBtn.setFont(font)
        self.conversionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.conversionBtn.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    background-color: #2c313c    ; /* replace with your desired color */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow-convert.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.conversionBtn.setIcon(icon3)
        self.conversionBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.conversionBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 6, -1, 6)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(135, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(135, 28))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/FullLogo_Transparent_NoBuffer.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon7)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon8)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon9)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(555, 315))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.centerMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy2.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy2)
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        sizePolicy2.setHeightForWidth(self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy2)
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon13)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.centerMenuContainer)

        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        sizePolicy1.setHeightForWidth(self.mainContentsContainer.sizePolicy().hasHeightForWidth())
        self.mainContentsContainer.setSizePolicy(sizePolicy1)
        self.mainContentsContainer.setStyleSheet(u"mainContentsContainer QTableWidget::horizontalHeader::section {\n"
"	background-color: blue; /* replace with your desired color */\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.traceTable = QTableWidget(self.mainContentsContainer)
        self.traceTable.setObjectName(u"traceTable")
        self.traceTable.horizontalHeader().setStretchLastSection(True)
        self.traceTable.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.traceTable)

        self.matchTable = QTableWidget(self.mainContentsContainer)
        self.matchTable.setObjectName(u"matchTable")
        self.matchTable.horizontalHeader().setStretchLastSection(True)
        self.matchTable.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.matchTable)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 303))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon13)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_14 = QVBoxLayout(self.page_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_2)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.mainBodyContent)

        self.miscPopUpsContainer = QFrame(self.mainBodyContainer)
        self.miscPopUpsContainer.setObjectName(u"miscPopUpsContainer")
        self.miscPopUpsContainer.setFrameShape(QFrame.StyledPanel)
        self.miscPopUpsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.miscPopUpsContainer)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.serverDBContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.serverDBContainer.setObjectName(u"serverDBContainer")
        self.horizontalLayout_13 = QHBoxLayout(self.serverDBContainer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.serverDBSubContainer = QWidget(self.serverDBContainer)
        self.serverDBSubContainer.setObjectName(u"serverDBSubContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.serverDBSubContainer.sizePolicy().hasHeightForWidth())
        self.serverDBSubContainer.setSizePolicy(sizePolicy4)
        self.verticalLayout_22 = QVBoxLayout(self.serverDBSubContainer)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.closeServerDBBtn = QPushButton(self.serverDBSubContainer)
        self.closeServerDBBtn.setObjectName(u"closeServerDBBtn")
        self.closeServerDBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeServerDBBtn.setIcon(icon12)

        self.verticalLayout_22.addWidget(self.closeServerDBBtn, 0, Qt.AlignRight)

        self.findDataLabel = QLabel(self.serverDBSubContainer)
        self.findDataLabel.setObjectName(u"findDataLabel")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.findDataLabel.setFont(font3)

        self.verticalLayout_22.addWidget(self.findDataLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.serverLabel = QLabel(self.serverDBSubContainer)
        self.serverLabel.setObjectName(u"serverLabel")
        font4 = QFont()
        font4.setPointSize(10)
        self.serverLabel.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.serverLabel)

        self.serverLineEdit = QLineEdit(self.serverDBSubContainer)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setFont(font4)
        self.serverLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")
        self.serverLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serverLineEdit)

        self.databaseLabel = QLabel(self.serverDBSubContainer)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font4)
        self.databaseLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.databaseLabel)

        self.dataBaseLineEdit = QLineEdit(self.serverDBSubContainer)
        self.dataBaseLineEdit.setObjectName(u"dataBaseLineEdit")
        self.dataBaseLineEdit.setFont(font4)
        self.dataBaseLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")
        self.dataBaseLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dataBaseLineEdit)

        self.tableLabel = QLabel(self.serverDBSubContainer)
        self.tableLabel.setObjectName(u"tableLabel")
        self.tableLabel.setFont(font4)
        self.tableLabel.setStyleSheet(u"")
        self.tableLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.tableLabel)

        self.tableLineEdit = QLineEdit(self.serverDBSubContainer)
        self.tableLineEdit.setObjectName(u"tableLineEdit")
        self.tableLineEdit.setFont(font4)
        self.tableLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")
        self.tableLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.tableLineEdit)


        self.verticalLayout_22.addLayout(self.formLayout)

        self.submitTraceServerDBBtn = QPushButton(self.serverDBSubContainer)
        self.submitTraceServerDBBtn.setObjectName(u"submitTraceServerDBBtn")
        self.submitTraceServerDBBtn.setFont(font4)
        self.submitTraceServerDBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitTraceServerDBBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.verticalLayout_22.addWidget(self.submitTraceServerDBBtn)


        self.horizontalLayout_13.addWidget(self.serverDBSubContainer)


        self.horizontalLayout_14.addWidget(self.serverDBContainer)

        self.startingTransactionsContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.startingTransactionsContainer.setObjectName(u"startingTransactionsContainer")
        sizePolicy4.setHeightForWidth(self.startingTransactionsContainer.sizePolicy().hasHeightForWidth())
        self.startingTransactionsContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_15 = QHBoxLayout(self.startingTransactionsContainer)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.startingTransactionsSubContainer = QFrame(self.startingTransactionsContainer)
        self.startingTransactionsSubContainer.setObjectName(u"startingTransactionsSubContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.startingTransactionsSubContainer.sizePolicy().hasHeightForWidth())
        self.startingTransactionsSubContainer.setSizePolicy(sizePolicy5)
        self.startingTransactionsSubContainer.setStyleSheet(u"QLineEdit { background-color: #343a40; border: 1px solid #666666; border-radius: 5px; }")
        self.startingTransactionsSubContainer.setFrameShape(QFrame.StyledPanel)
        self.startingTransactionsSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.startingTransactionsSubContainer)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.closeStartingTransactionsBtn = QPushButton(self.startingTransactionsSubContainer)
        self.closeStartingTransactionsBtn.setObjectName(u"closeStartingTransactionsBtn")
        self.closeStartingTransactionsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeStartingTransactionsBtn.setIcon(icon12)

        self.verticalLayout_9.addWidget(self.closeStartingTransactionsBtn, 0, Qt.AlignRight)

        self.inputStartingTransactionsLabel = QLabel(self.startingTransactionsSubContainer)
        self.inputStartingTransactionsLabel.setObjectName(u"inputStartingTransactionsLabel")
        self.inputStartingTransactionsLabel.setFont(font3)

        self.verticalLayout_9.addWidget(self.inputStartingTransactionsLabel)

        self.startingTransactionsScrollArea = QScrollArea(self.startingTransactionsSubContainer)
        self.startingTransactionsScrollArea.setObjectName(u"startingTransactionsScrollArea")
        self.startingTransactionsScrollArea.setWidgetResizable(True)
        self.startingTransactionsScrollAreaWidgetContents = QWidget()
        self.startingTransactionsScrollAreaWidgetContents.setObjectName(u"startingTransactionsScrollAreaWidgetContents")
        self.startingTransactionsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 179, 71))
        self.verticalLayout_10 = QVBoxLayout(self.startingTransactionsScrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.startingTransactionsLineEdit = QLineEdit(self.startingTransactionsScrollAreaWidgetContents)
        self.startingTransactionsLineEdit.setObjectName(u"startingTransactionsLineEdit")
        self.startingTransactionsLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.verticalLayout_10.addWidget(self.startingTransactionsLineEdit)

        self.startingTransactionsVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.startingTransactionsVerticalSpacer)

        self.startingTransactionsScrollArea.setWidget(self.startingTransactionsScrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.startingTransactionsScrollArea)

        self.startingTransactionsButtonsContainer = QVBoxLayout()
        self.startingTransactionsButtonsContainer.setSpacing(4)
        self.startingTransactionsButtonsContainer.setObjectName(u"startingTransactionsButtonsContainer")
        self.startingTransactionsButtonsFrame = QFrame(self.startingTransactionsSubContainer)
        self.startingTransactionsButtonsFrame.setObjectName(u"startingTransactionsButtonsFrame")
        self.startingTransactionsButtonsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.startingTransactionsButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.startingTransactionsButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.startingTransactionsButtonsFrame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.addStartingTransactionsRowBtn = QPushButton(self.startingTransactionsButtonsFrame)
        self.addStartingTransactionsRowBtn.setObjectName(u"addStartingTransactionsRowBtn")
        self.addStartingTransactionsRowBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addStartingTransactionsRowBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_16.addWidget(self.addStartingTransactionsRowBtn)

        self.submitStartingTransactionsBtn = QPushButton(self.startingTransactionsButtonsFrame)
        self.submitStartingTransactionsBtn.setObjectName(u"submitStartingTransactionsBtn")
        self.submitStartingTransactionsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitStartingTransactionsBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_16.addWidget(self.submitStartingTransactionsBtn)


        self.startingTransactionsButtonsContainer.addWidget(self.startingTransactionsButtonsFrame)

        self.loadStartingTransactionsFromFileBtn = QPushButton(self.startingTransactionsSubContainer)
        self.loadStartingTransactionsFromFileBtn.setObjectName(u"loadStartingTransactionsFromFileBtn")
        self.loadStartingTransactionsFromFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadStartingTransactionsFromFileBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.startingTransactionsButtonsContainer.addWidget(self.loadStartingTransactionsFromFileBtn)


        self.verticalLayout_9.addLayout(self.startingTransactionsButtonsContainer)


        self.horizontalLayout_15.addWidget(self.startingTransactionsSubContainer)


        self.horizontalLayout_14.addWidget(self.startingTransactionsContainer)

        self.manualMatchesContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.manualMatchesContainer.setObjectName(u"manualMatchesContainer")
        sizePolicy4.setHeightForWidth(self.manualMatchesContainer.sizePolicy().hasHeightForWidth())
        self.manualMatchesContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_17 = QHBoxLayout(self.manualMatchesContainer)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.manualMatchesSubContainer = QFrame(self.manualMatchesContainer)
        self.manualMatchesSubContainer.setObjectName(u"manualMatchesSubContainer")
        sizePolicy5.setHeightForWidth(self.manualMatchesSubContainer.sizePolicy().hasHeightForWidth())
        self.manualMatchesSubContainer.setSizePolicy(sizePolicy5)
        self.manualMatchesSubContainer.setStyleSheet(u"QLineEdit { background-color: #343a40; border: 1px solid #666666; border-radius: 5px; }")
        self.manualMatchesSubContainer.setFrameShape(QFrame.StyledPanel)
        self.manualMatchesSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.manualMatchesSubContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.closeManualMatchesBtn = QPushButton(self.manualMatchesSubContainer)
        self.closeManualMatchesBtn.setObjectName(u"closeManualMatchesBtn")
        self.closeManualMatchesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeManualMatchesBtn.setIcon(icon12)

        self.verticalLayout_15.addWidget(self.closeManualMatchesBtn, 0, Qt.AlignRight)

        self.manualMatchesLabel = QLabel(self.manualMatchesSubContainer)
        self.manualMatchesLabel.setObjectName(u"manualMatchesLabel")
        self.manualMatchesLabel.setFont(font3)
        self.manualMatchesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.manualMatchesLabel)

        self.manualMatchesInputHeadersFrame = QFrame(self.manualMatchesSubContainer)
        self.manualMatchesInputHeadersFrame.setObjectName(u"manualMatchesInputHeadersFrame")
        self.manualMatchesInputHeadersFrame.setFrameShape(QFrame.StyledPanel)
        self.manualMatchesInputHeadersFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.manualMatchesInputHeadersFrame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.manualMatchesHeader1Label = QLabel(self.manualMatchesInputHeadersFrame)
        self.manualMatchesHeader1Label.setObjectName(u"manualMatchesHeader1Label")
        self.manualMatchesHeader1Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.manualMatchesHeader1Label)

        self.manualMatchesHeader2Label = QLabel(self.manualMatchesInputHeadersFrame)
        self.manualMatchesHeader2Label.setObjectName(u"manualMatchesHeader2Label")
        self.manualMatchesHeader2Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.manualMatchesHeader2Label)


        self.verticalLayout_15.addWidget(self.manualMatchesInputHeadersFrame)

        self.manualMatchesScrollArea = QScrollArea(self.manualMatchesSubContainer)
        self.manualMatchesScrollArea.setObjectName(u"manualMatchesScrollArea")
        self.manualMatchesScrollArea.setWidgetResizable(True)
        self.manualMatchesScrollAreaWidgetContents = QWidget()
        self.manualMatchesScrollAreaWidgetContents.setObjectName(u"manualMatchesScrollAreaWidgetContents")
        self.manualMatchesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 157, 71))
        self.verticalLayout_16 = QVBoxLayout(self.manualMatchesScrollAreaWidgetContents)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, -1)
        self.manualMatchesRowInputFrame = QFrame(self.manualMatchesScrollAreaWidgetContents)
        self.manualMatchesRowInputFrame.setObjectName(u"manualMatchesRowInputFrame")
        self.manualMatchesRowInputFrame.setFrameShape(QFrame.StyledPanel)
        self.manualMatchesRowInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.manualMatchesRowInputFrame)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.manualMatchesLineEdit1 = QLineEdit(self.manualMatchesRowInputFrame)
        self.manualMatchesLineEdit1.setObjectName(u"manualMatchesLineEdit1")
        self.manualMatchesLineEdit1.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_19.addWidget(self.manualMatchesLineEdit1)

        self.manualMatchesLineEdit2 = QLineEdit(self.manualMatchesRowInputFrame)
        self.manualMatchesLineEdit2.setObjectName(u"manualMatchesLineEdit2")
        self.manualMatchesLineEdit2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_19.addWidget(self.manualMatchesLineEdit2)


        self.verticalLayout_16.addWidget(self.manualMatchesRowInputFrame)

        self.manualMatchesVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.manualMatchesVerticalSpacer)

        self.manualMatchesScrollArea.setWidget(self.manualMatchesScrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.manualMatchesScrollArea)

        self.manualMatchesButtonsContainer = QVBoxLayout()
        self.manualMatchesButtonsContainer.setSpacing(4)
        self.manualMatchesButtonsContainer.setObjectName(u"manualMatchesButtonsContainer")
        self.manualMatchesButtonsFrame = QFrame(self.manualMatchesSubContainer)
        self.manualMatchesButtonsFrame.setObjectName(u"manualMatchesButtonsFrame")
        self.manualMatchesButtonsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.manualMatchesButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.manualMatchesButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.manualMatchesButtonsFrame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.addManualMatchesRowBtn = QPushButton(self.manualMatchesButtonsFrame)
        self.addManualMatchesRowBtn.setObjectName(u"addManualMatchesRowBtn")
        self.addManualMatchesRowBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addManualMatchesRowBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_18.addWidget(self.addManualMatchesRowBtn)

        self.submitManualMatchesBtn = QPushButton(self.manualMatchesButtonsFrame)
        self.submitManualMatchesBtn.setObjectName(u"submitManualMatchesBtn")
        self.submitManualMatchesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitManualMatchesBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_18.addWidget(self.submitManualMatchesBtn)


        self.manualMatchesButtonsContainer.addWidget(self.manualMatchesButtonsFrame)

        self.loadManualMatchesFromFileBtn = QPushButton(self.manualMatchesSubContainer)
        self.loadManualMatchesFromFileBtn.setObjectName(u"loadManualMatchesFromFileBtn")
        self.loadManualMatchesFromFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadManualMatchesFromFileBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.manualMatchesButtonsContainer.addWidget(self.loadManualMatchesFromFileBtn)


        self.verticalLayout_15.addLayout(self.manualMatchesButtonsContainer)


        self.horizontalLayout_17.addWidget(self.manualMatchesSubContainer)


        self.horizontalLayout_14.addWidget(self.manualMatchesContainer)

        self.manualUnmatchContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.manualUnmatchContainer.setObjectName(u"manualUnmatchContainer")
        sizePolicy4.setHeightForWidth(self.manualUnmatchContainer.sizePolicy().hasHeightForWidth())
        self.manualUnmatchContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_24 = QHBoxLayout(self.manualUnmatchContainer)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.manualUnmatchSubContainer = QFrame(self.manualUnmatchContainer)
        self.manualUnmatchSubContainer.setObjectName(u"manualUnmatchSubContainer")
        sizePolicy5.setHeightForWidth(self.manualUnmatchSubContainer.sizePolicy().hasHeightForWidth())
        self.manualUnmatchSubContainer.setSizePolicy(sizePolicy5)
        self.manualUnmatchSubContainer.setStyleSheet(u"QLineEdit { background-color: #343a40; border: 1px solid #666666; border-radius: 5px; }")
        self.manualUnmatchSubContainer.setFrameShape(QFrame.StyledPanel)
        self.manualUnmatchSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.manualUnmatchSubContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.closeManualUnmatchBtn = QPushButton(self.manualUnmatchSubContainer)
        self.closeManualUnmatchBtn.setObjectName(u"closeManualUnmatchBtn")
        self.closeManualUnmatchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeManualUnmatchBtn.setIcon(icon12)

        self.verticalLayout_21.addWidget(self.closeManualUnmatchBtn, 0, Qt.AlignRight)

        self.manualUnmatchLabel = QLabel(self.manualUnmatchSubContainer)
        self.manualUnmatchLabel.setObjectName(u"manualUnmatchLabel")
        self.manualUnmatchLabel.setFont(font3)
        self.manualUnmatchLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.manualUnmatchLabel)

        self.manualUnmatchInputHeadersFrame = QFrame(self.manualUnmatchSubContainer)
        self.manualUnmatchInputHeadersFrame.setObjectName(u"manualUnmatchInputHeadersFrame")
        self.manualUnmatchInputHeadersFrame.setFrameShape(QFrame.StyledPanel)
        self.manualUnmatchInputHeadersFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.manualUnmatchInputHeadersFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.manualUnmatchHeader1Label = QLabel(self.manualUnmatchInputHeadersFrame)
        self.manualUnmatchHeader1Label.setObjectName(u"manualUnmatchHeader1Label")
        self.manualUnmatchHeader1Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.manualUnmatchHeader1Label)

        self.manualUnmatchHeader2Label = QLabel(self.manualUnmatchInputHeadersFrame)
        self.manualUnmatchHeader2Label.setObjectName(u"manualUnmatchHeader2Label")
        self.manualUnmatchHeader2Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.manualUnmatchHeader2Label)


        self.verticalLayout_21.addWidget(self.manualUnmatchInputHeadersFrame)

        self.manualUnmatchScrollArea = QScrollArea(self.manualUnmatchSubContainer)
        self.manualUnmatchScrollArea.setObjectName(u"manualUnmatchScrollArea")
        self.manualUnmatchScrollArea.setWidgetResizable(True)
        self.manualUnmatchScrollAreaWidgetContents = QWidget()
        self.manualUnmatchScrollAreaWidgetContents.setObjectName(u"manualUnmatchScrollAreaWidgetContents")
        self.manualUnmatchScrollAreaWidgetContents.setGeometry(QRect(0, 0, 157, 76))
        self.verticalLayout_23 = QVBoxLayout(self.manualUnmatchScrollAreaWidgetContents)
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, -1)
        self.manualUnmatchRowInputFrame = QFrame(self.manualUnmatchScrollAreaWidgetContents)
        self.manualUnmatchRowInputFrame.setObjectName(u"manualUnmatchRowInputFrame")
        self.manualUnmatchRowInputFrame.setFrameShape(QFrame.StyledPanel)
        self.manualUnmatchRowInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.manualUnmatchRowInputFrame)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 3, 0, 2)
        self.manualUnmatchLineEdit1 = QLineEdit(self.manualUnmatchRowInputFrame)
        self.manualUnmatchLineEdit1.setObjectName(u"manualUnmatchLineEdit1")
        self.manualUnmatchLineEdit1.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_26.addWidget(self.manualUnmatchLineEdit1)

        self.manualUnmatchLineEdit2 = QLineEdit(self.manualUnmatchRowInputFrame)
        self.manualUnmatchLineEdit2.setObjectName(u"manualUnmatchLineEdit2")
        self.manualUnmatchLineEdit2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_26.addWidget(self.manualUnmatchLineEdit2)


        self.verticalLayout_23.addWidget(self.manualUnmatchRowInputFrame)

        self.manualUnmatchVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.manualUnmatchVerticalSpacer)

        self.manualUnmatchScrollArea.setWidget(self.manualUnmatchScrollAreaWidgetContents)

        self.verticalLayout_21.addWidget(self.manualUnmatchScrollArea)

        self.manualUnmatchButtonsContainer = QVBoxLayout()
        self.manualUnmatchButtonsContainer.setSpacing(4)
        self.manualUnmatchButtonsContainer.setObjectName(u"manualUnmatchButtonsContainer")
        self.manualUnmatchButtonsFrame = QFrame(self.manualUnmatchSubContainer)
        self.manualUnmatchButtonsFrame.setObjectName(u"manualUnmatchButtonsFrame")
        self.manualUnmatchButtonsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.manualUnmatchButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.manualUnmatchButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.manualUnmatchButtonsFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.addManualUnmatchRowBtn = QPushButton(self.manualUnmatchButtonsFrame)
        self.addManualUnmatchRowBtn.setObjectName(u"addManualUnmatchRowBtn")
        self.addManualUnmatchRowBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addManualUnmatchRowBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_27.addWidget(self.addManualUnmatchRowBtn)

        self.submitManualUnmatchBtn = QPushButton(self.manualUnmatchButtonsFrame)
        self.submitManualUnmatchBtn.setObjectName(u"submitManualUnmatchBtn")
        self.submitManualUnmatchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitManualUnmatchBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_27.addWidget(self.submitManualUnmatchBtn)


        self.manualUnmatchButtonsContainer.addWidget(self.manualUnmatchButtonsFrame)

        self.loadManualUnmatchFromFileBtn = QPushButton(self.manualUnmatchSubContainer)
        self.loadManualUnmatchFromFileBtn.setObjectName(u"loadManualUnmatchFromFileBtn")
        self.loadManualUnmatchFromFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadManualUnmatchFromFileBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.manualUnmatchButtonsContainer.addWidget(self.loadManualUnmatchFromFileBtn)


        self.verticalLayout_21.addLayout(self.manualUnmatchButtonsContainer)


        self.horizontalLayout_24.addWidget(self.manualUnmatchSubContainer)


        self.horizontalLayout_14.addWidget(self.manualUnmatchContainer)

        self.refTableContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.refTableContainer.setObjectName(u"refTableContainer")
        sizePolicy4.setHeightForWidth(self.refTableContainer.sizePolicy().hasHeightForWidth())
        self.refTableContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_28 = QHBoxLayout(self.refTableContainer)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.refTableSubContainer = QFrame(self.refTableContainer)
        self.refTableSubContainer.setObjectName(u"refTableSubContainer")
        sizePolicy5.setHeightForWidth(self.refTableSubContainer.sizePolicy().hasHeightForWidth())
        self.refTableSubContainer.setSizePolicy(sizePolicy5)
        self.refTableSubContainer.setStyleSheet(u"QLineEdit { background-color: #343a40; border: 1px solid #666666; border-radius: 5px; }")
        self.refTableSubContainer.setFrameShape(QFrame.StyledPanel)
        self.refTableSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.refTableSubContainer)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.closeRefTableBtn = QPushButton(self.refTableSubContainer)
        self.closeRefTableBtn.setObjectName(u"closeRefTableBtn")
        self.closeRefTableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeRefTableBtn.setIcon(icon12)

        self.verticalLayout_24.addWidget(self.closeRefTableBtn, 0, Qt.AlignRight)

        self.refTableLabel = QLabel(self.refTableSubContainer)
        self.refTableLabel.setObjectName(u"refTableLabel")
        self.refTableLabel.setFont(font3)
        self.refTableLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.refTableLabel)

        self.refTableInputHeadersFrame = QFrame(self.refTableSubContainer)
        self.refTableInputHeadersFrame.setObjectName(u"refTableInputHeadersFrame")
        self.refTableInputHeadersFrame.setFrameShape(QFrame.StyledPanel)
        self.refTableInputHeadersFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.refTableInputHeadersFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.refTableHeader1Label = QLabel(self.refTableInputHeadersFrame)
        self.refTableHeader1Label.setObjectName(u"refTableHeader1Label")
        self.refTableHeader1Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.refTableHeader1Label)

        self.refTableHeader2Label = QLabel(self.refTableInputHeadersFrame)
        self.refTableHeader2Label.setObjectName(u"refTableHeader2Label")
        self.refTableHeader2Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.refTableHeader2Label)


        self.verticalLayout_24.addWidget(self.refTableInputHeadersFrame)

        self.refTableScrollArea = QScrollArea(self.refTableSubContainer)
        self.refTableScrollArea.setObjectName(u"refTableScrollArea")
        self.refTableScrollArea.setWidgetResizable(True)
        self.refTableScrollAreaWidgetContents = QWidget()
        self.refTableScrollAreaWidgetContents.setObjectName(u"refTableScrollAreaWidgetContents")
        self.refTableScrollAreaWidgetContents.setGeometry(QRect(0, 0, 157, 76))
        self.verticalLayout_25 = QVBoxLayout(self.refTableScrollAreaWidgetContents)
        self.verticalLayout_25.setSpacing(4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, -1)
        self.refTableRowInputFrame = QFrame(self.refTableScrollAreaWidgetContents)
        self.refTableRowInputFrame.setObjectName(u"refTableRowInputFrame")
        self.refTableRowInputFrame.setFrameShape(QFrame.StyledPanel)
        self.refTableRowInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.refTableRowInputFrame)
        self.horizontalLayout_30.setSpacing(2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 3, 0, 2)
        self.refTableLineEdit1 = QLineEdit(self.refTableRowInputFrame)
        self.refTableLineEdit1.setObjectName(u"refTableLineEdit1")
        self.refTableLineEdit1.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_30.addWidget(self.refTableLineEdit1)

        self.refTableLineEdit2 = QLineEdit(self.refTableRowInputFrame)
        self.refTableLineEdit2.setObjectName(u"refTableLineEdit2")
        self.refTableLineEdit2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_30.addWidget(self.refTableLineEdit2)


        self.verticalLayout_25.addWidget(self.refTableRowInputFrame)

        self.refTableVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.refTableVerticalSpacer)

        self.refTableScrollArea.setWidget(self.refTableScrollAreaWidgetContents)

        self.verticalLayout_24.addWidget(self.refTableScrollArea)

        self.refTableButtonsContainer = QVBoxLayout()
        self.refTableButtonsContainer.setSpacing(4)
        self.refTableButtonsContainer.setObjectName(u"refTableButtonsContainer")
        self.refTableButtonsFrame = QFrame(self.refTableSubContainer)
        self.refTableButtonsFrame.setObjectName(u"refTableButtonsFrame")
        self.refTableButtonsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.refTableButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.refTableButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.refTableButtonsFrame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.addRefTableRowBtn = QPushButton(self.refTableButtonsFrame)
        self.addRefTableRowBtn.setObjectName(u"addRefTableRowBtn")
        self.addRefTableRowBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addRefTableRowBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_31.addWidget(self.addRefTableRowBtn)

        self.submitRefTableBtn = QPushButton(self.refTableButtonsFrame)
        self.submitRefTableBtn.setObjectName(u"submitRefTableBtn")
        self.submitRefTableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitRefTableBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_31.addWidget(self.submitRefTableBtn)


        self.refTableButtonsContainer.addWidget(self.refTableButtonsFrame)

        self.loadRefTableFromFileBtn = QPushButton(self.refTableSubContainer)
        self.loadRefTableFromFileBtn.setObjectName(u"loadRefTableFromFileBtn")
        self.loadRefTableFromFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadRefTableFromFileBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.refTableButtonsContainer.addWidget(self.loadRefTableFromFileBtn)


        self.verticalLayout_24.addLayout(self.refTableButtonsContainer)


        self.horizontalLayout_28.addWidget(self.refTableSubContainer)


        self.horizontalLayout_14.addWidget(self.refTableContainer)

        self.categoriesContainer = QCustomSlideMenu(self.miscPopUpsContainer)
        self.categoriesContainer.setObjectName(u"categoriesContainer")
        sizePolicy4.setHeightForWidth(self.categoriesContainer.sizePolicy().hasHeightForWidth())
        self.categoriesContainer.setSizePolicy(sizePolicy4)
        self.horizontalLayout_32 = QHBoxLayout(self.categoriesContainer)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.categoriesSubContainer = QFrame(self.categoriesContainer)
        self.categoriesSubContainer.setObjectName(u"categoriesSubContainer")
        sizePolicy5.setHeightForWidth(self.categoriesSubContainer.sizePolicy().hasHeightForWidth())
        self.categoriesSubContainer.setSizePolicy(sizePolicy5)
        self.categoriesSubContainer.setStyleSheet(u"QLineEdit { background-color: #343a40; border: 1px solid #666666; border-radius: 5px; }")
        self.categoriesSubContainer.setFrameShape(QFrame.StyledPanel)
        self.categoriesSubContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.categoriesSubContainer)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.closeCategoriesBtn = QPushButton(self.categoriesSubContainer)
        self.closeCategoriesBtn.setObjectName(u"closeCategoriesBtn")
        self.closeCategoriesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeCategoriesBtn.setIcon(icon12)

        self.verticalLayout_26.addWidget(self.closeCategoriesBtn, 0, Qt.AlignRight)

        self.categoriesLabel = QLabel(self.categoriesSubContainer)
        self.categoriesLabel.setObjectName(u"categoriesLabel")
        self.categoriesLabel.setFont(font3)
        self.categoriesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.categoriesLabel)

        self.categoriesInputHeadersFrame = QFrame(self.categoriesSubContainer)
        self.categoriesInputHeadersFrame.setObjectName(u"categoriesInputHeadersFrame")
        self.categoriesInputHeadersFrame.setFrameShape(QFrame.StyledPanel)
        self.categoriesInputHeadersFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.categoriesInputHeadersFrame)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.categoriesHeader1Label = QLabel(self.categoriesInputHeadersFrame)
        self.categoriesHeader1Label.setObjectName(u"categoriesHeader1Label")
        self.categoriesHeader1Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.categoriesHeader1Label)

        self.categoriesHeader2Label = QLabel(self.categoriesInputHeadersFrame)
        self.categoriesHeader2Label.setObjectName(u"categoriesHeader2Label")
        self.categoriesHeader2Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.categoriesHeader2Label)


        self.verticalLayout_26.addWidget(self.categoriesInputHeadersFrame)

        self.categoriesScrollArea = QScrollArea(self.categoriesSubContainer)
        self.categoriesScrollArea.setObjectName(u"categoriesScrollArea")
        self.categoriesScrollArea.setWidgetResizable(True)
        self.categoriesScrollAreaWidgetContents = QWidget()
        self.categoriesScrollAreaWidgetContents.setObjectName(u"categoriesScrollAreaWidgetContents")
        self.categoriesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 157, 76))
        self.verticalLayout_27 = QVBoxLayout(self.categoriesScrollAreaWidgetContents)
        self.verticalLayout_27.setSpacing(4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, -1)
        self.categoriesRowInputFrame = QFrame(self.categoriesScrollAreaWidgetContents)
        self.categoriesRowInputFrame.setObjectName(u"categoriesRowInputFrame")
        self.categoriesRowInputFrame.setFrameShape(QFrame.StyledPanel)
        self.categoriesRowInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.categoriesRowInputFrame)
        self.horizontalLayout_34.setSpacing(2)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 3, 0, 2)
        self.categoriesLineEdit1 = QLineEdit(self.categoriesRowInputFrame)
        self.categoriesLineEdit1.setObjectName(u"categoriesLineEdit1")
        self.categoriesLineEdit1.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_34.addWidget(self.categoriesLineEdit1)

        self.categoriesLineEdit2 = QLineEdit(self.categoriesRowInputFrame)
        self.categoriesLineEdit2.setObjectName(u"categoriesLineEdit2")
        self.categoriesLineEdit2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #343a40; /* or #454f55 */\n"
"	border: 1px solid #666666; /* or #808080 */\n"
"	border-radius: 5px; /* or 8px */\n"
"}")

        self.horizontalLayout_34.addWidget(self.categoriesLineEdit2)


        self.verticalLayout_27.addWidget(self.categoriesRowInputFrame)

        self.categoriesVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.categoriesVerticalSpacer)

        self.categoriesScrollArea.setWidget(self.categoriesScrollAreaWidgetContents)

        self.verticalLayout_26.addWidget(self.categoriesScrollArea)

        self.categoriesButtonsContainer = QVBoxLayout()
        self.categoriesButtonsContainer.setSpacing(4)
        self.categoriesButtonsContainer.setObjectName(u"categoriesButtonsContainer")
        self.categoriesButtonsFrame = QFrame(self.categoriesSubContainer)
        self.categoriesButtonsFrame.setObjectName(u"categoriesButtonsFrame")
        self.categoriesButtonsFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.categoriesButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.categoriesButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.categoriesButtonsFrame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.addCategoriesRowBtn = QPushButton(self.categoriesButtonsFrame)
        self.addCategoriesRowBtn.setObjectName(u"addCategoriesRowBtn")
        self.addCategoriesRowBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addCategoriesRowBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_35.addWidget(self.addCategoriesRowBtn)

        self.submitCategoriesBtn = QPushButton(self.categoriesButtonsFrame)
        self.submitCategoriesBtn.setObjectName(u"submitCategoriesBtn")
        self.submitCategoriesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitCategoriesBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.horizontalLayout_35.addWidget(self.submitCategoriesBtn)


        self.categoriesButtonsContainer.addWidget(self.categoriesButtonsFrame)

        self.loadCategoriesFromFileBtn = QPushButton(self.categoriesSubContainer)
        self.loadCategoriesFromFileBtn.setObjectName(u"loadCategoriesFromFileBtn")
        self.loadCategoriesFromFileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadCategoriesFromFileBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #2c313c; /* a dark blue-gray color */\n"
"	color: #ffffff; /* white text color for contrast */\n"
"	border: 1px solid #666666; /* dark gray border */\n"
"	border-radius: 5px; /* rounded corners */\n"
"	padding: 5px 10px; /* add some padding for a better look */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #454f55; /* a slightly lighter dark gray color on hover */\n"
"}")

        self.categoriesButtonsContainer.addWidget(self.loadCategoriesFromFileBtn)


        self.verticalLayout_26.addLayout(self.categoriesButtonsContainer)


        self.horizontalLayout_32.addWidget(self.categoriesSubContainer)


        self.horizontalLayout_14.addWidget(self.categoriesContainer)


        self.verticalLayout_7.addWidget(self.miscPopUpsContainer)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.label_14.setFont(font5)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon14)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_7.addWidget(self.popupNotificationContainer)

        self.footerContainter = QWidget(self.mainBodyContainer)
        self.footerContainter.setObjectName(u"footerContainter")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainter)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainter)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainter)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_7.addWidget(self.footerContainter)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.tracingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Transaction Tracing", None))
#endif // QT_CONFIG(tooltip)
        self.tracingBtn.setText(QCoreApplication.translate("MainWindow", u"  Tracing", None))
#if QT_CONFIG(tooltip)
        self.matchingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Transaction Matching", None))
#endif // QT_CONFIG(tooltip)
        self.matchingBtn.setText(QCoreApplication.translate("MainWindow", u"  Matching", None))
#if QT_CONFIG(tooltip)
        self.conversionBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Bank Statement Conversion", None))
#endif // QT_CONFIG(tooltip)
        self.conversionBtn.setText(QCoreApplication.translate("MainWindow", u"  Conversion", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.closeServerDBBtn.setText("")
        self.findDataLabel.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Database:", None))
        self.tableLabel.setText(QCoreApplication.translate("MainWindow", u"Table:", None))
        self.submitTraceServerDBBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.closeStartingTransactionsBtn.setText("")
        self.inputStartingTransactionsLabel.setText(QCoreApplication.translate("MainWindow", u"Input Starting Transactions", None))
        self.addStartingTransactionsRowBtn.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.submitStartingTransactionsBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loadStartingTransactionsFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.closeManualMatchesBtn.setText("")
        self.manualMatchesLabel.setText(QCoreApplication.translate("MainWindow", u"Manual Matches", None))
        self.manualMatchesHeader1Label.setText(QCoreApplication.translate("MainWindow", u"Debit ID", None))
        self.manualMatchesHeader2Label.setText(QCoreApplication.translate("MainWindow", u"Credit ID", None))
        self.addManualMatchesRowBtn.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.submitManualMatchesBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loadManualMatchesFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.closeManualUnmatchBtn.setText("")
        self.manualUnmatchLabel.setText(QCoreApplication.translate("MainWindow", u"Manual Unmatch", None))
        self.manualUnmatchHeader1Label.setText(QCoreApplication.translate("MainWindow", u"Debit ID", None))
        self.manualUnmatchHeader2Label.setText(QCoreApplication.translate("MainWindow", u"Credit ID", None))
        self.addManualUnmatchRowBtn.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.submitManualUnmatchBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loadManualUnmatchFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.closeRefTableBtn.setText("")
        self.refTableLabel.setText(QCoreApplication.translate("MainWindow", u"Reference Table", None))
        self.refTableHeader1Label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.refTableHeader2Label.setText(QCoreApplication.translate("MainWindow", u"Search Term", None))
        self.addRefTableRowBtn.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.submitRefTableBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loadRefTableFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.closeCategoriesBtn.setText("")
        self.categoriesLabel.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.categoriesHeader1Label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.categoriesHeader2Label.setText(QCoreApplication.translate("MainWindow", u"Search Term", None))
        self.addCategoriesRowBtn.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
        self.submitCategoriesBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.loadCategoriesFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"L.B", None))
    # retranslateUi

