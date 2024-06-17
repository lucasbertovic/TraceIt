# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_matchRibbonContainer(object):
    def setupUi(self, matchRibbonContainer):
        if matchRibbonContainer.objectName():
            matchRibbonContainer.setObjectName(u"matchRibbonContainer")
        matchRibbonContainer.resize(202, 759)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(matchRibbonContainer.sizePolicy().hasHeightForWidth())
        matchRibbonContainer.setSizePolicy(sizePolicy)
        matchRibbonContainer.setStyleSheet(u"*{\n"
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
        self.horizontalLayout = QHBoxLayout(matchRibbonContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ribbonSubContainer = QWidget(matchRibbonContainer)
        self.ribbonSubContainer.setObjectName(u"ribbonSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ribbonSubContainer.sizePolicy().hasHeightForWidth())
        self.ribbonSubContainer.setSizePolicy(sizePolicy1)
        self.ribbonSubContainer.setStyleSheet(u"*{\n"
"	background-color: #2c313c;\n"
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
"        max-height: 30px; /* Adjust the value to set the desired minimum height */\n"
"    }\n"
"\n"
"QLabel {\n"
"        padding-left: 8px; /* Adjust the value to set the desired padding */\n"
"    }")
        self.verticalLayout = QVBoxLayout(self.ribbonSubContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadMatchesFromDBBtn = QPushButton(self.ribbonSubContainer)
        self.loadMatchesFromDBBtn.setObjectName(u"loadMatchesFromDBBtn")
        sizePolicy1.setHeightForWidth(self.loadMatchesFromDBBtn.sizePolicy().hasHeightForWidth())
        self.loadMatchesFromDBBtn.setSizePolicy(sizePolicy1)
        self.loadMatchesFromDBBtn.setMinimumSize(QSize(0, 0))
        self.loadMatchesFromDBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadMatchesFromDBBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.loadMatchesFromDBBtn)

        self.loadMatchesFromExcelBtn = QPushButton(self.ribbonSubContainer)
        self.loadMatchesFromExcelBtn.setObjectName(u"loadMatchesFromExcelBtn")
        sizePolicy.setHeightForWidth(self.loadMatchesFromExcelBtn.sizePolicy().hasHeightForWidth())
        self.loadMatchesFromExcelBtn.setSizePolicy(sizePolicy)
        self.loadMatchesFromExcelBtn.setMinimumSize(QSize(0, 0))
        self.loadMatchesFromExcelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadMatchesFromExcelBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.loadMatchesFromExcelBtn)

        self.manualMatchesBtn = QPushButton(self.ribbonSubContainer)
        self.manualMatchesBtn.setObjectName(u"manualMatchesBtn")
        sizePolicy.setHeightForWidth(self.manualMatchesBtn.sizePolicy().hasHeightForWidth())
        self.manualMatchesBtn.setSizePolicy(sizePolicy)
        self.manualMatchesBtn.setMinimumSize(QSize(0, 0))
        self.manualMatchesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.manualMatchesBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.manualMatchesBtn)

        self.manualUnmatchBtn = QPushButton(self.ribbonSubContainer)
        self.manualUnmatchBtn.setObjectName(u"manualUnmatchBtn")
        sizePolicy.setHeightForWidth(self.manualUnmatchBtn.sizePolicy().hasHeightForWidth())
        self.manualUnmatchBtn.setSizePolicy(sizePolicy)
        self.manualUnmatchBtn.setMinimumSize(QSize(0, 0))
        self.manualUnmatchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.manualUnmatchBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.manualUnmatchBtn)

        self.keyPartiesEntitiesBtn = QPushButton(self.ribbonSubContainer)
        self.keyPartiesEntitiesBtn.setObjectName(u"keyPartiesEntitiesBtn")
        sizePolicy.setHeightForWidth(self.keyPartiesEntitiesBtn.sizePolicy().hasHeightForWidth())
        self.keyPartiesEntitiesBtn.setSizePolicy(sizePolicy)
        self.keyPartiesEntitiesBtn.setMinimumSize(QSize(0, 0))
        self.keyPartiesEntitiesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.keyPartiesEntitiesBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.keyPartiesEntitiesBtn)

        self.keywordMatchFrame = QFrame(self.ribbonSubContainer)
        self.keywordMatchFrame.setObjectName(u"keywordMatchFrame")
        self.keywordMatchFrame.setStyleSheet(u"")
        self.keywordMatchFrame.setFrameShape(QFrame.StyledPanel)
        self.keywordMatchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.keywordMatchFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.keywordMatchLabel = QLabel(self.keywordMatchFrame)
        self.keywordMatchLabel.setObjectName(u"keywordMatchLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.keywordMatchLabel.sizePolicy().hasHeightForWidth())
        self.keywordMatchLabel.setSizePolicy(sizePolicy2)
        self.keywordMatchLabel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.keywordMatchLabel)

        self.keywordMatchLineEdit = QLineEdit(self.keywordMatchFrame)
        self.keywordMatchLineEdit.setObjectName(u"keywordMatchLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.keywordMatchLineEdit.sizePolicy().hasHeightForWidth())
        self.keywordMatchLineEdit.setSizePolicy(sizePolicy3)
        self.keywordMatchLineEdit.setStyleSheet(u"")
        self.keywordMatchLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.keywordMatchLineEdit)


        self.verticalLayout.addWidget(self.keywordMatchFrame)

        self.narrativeSimilarityFrame = QFrame(self.ribbonSubContainer)
        self.narrativeSimilarityFrame.setObjectName(u"narrativeSimilarityFrame")
        self.narrativeSimilarityFrame.setStyleSheet(u"")
        self.narrativeSimilarityFrame.setFrameShape(QFrame.StyledPanel)
        self.narrativeSimilarityFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.narrativeSimilarityFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.narrativeSimilarityLabel = QLabel(self.narrativeSimilarityFrame)
        self.narrativeSimilarityLabel.setObjectName(u"narrativeSimilarityLabel")
        sizePolicy2.setHeightForWidth(self.narrativeSimilarityLabel.sizePolicy().hasHeightForWidth())
        self.narrativeSimilarityLabel.setSizePolicy(sizePolicy2)
        self.narrativeSimilarityLabel.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.narrativeSimilarityLabel)

        self.narrativeSimilarityLineEdit = QLineEdit(self.narrativeSimilarityFrame)
        self.narrativeSimilarityLineEdit.setObjectName(u"narrativeSimilarityLineEdit")
        sizePolicy3.setHeightForWidth(self.narrativeSimilarityLineEdit.sizePolicy().hasHeightForWidth())
        self.narrativeSimilarityLineEdit.setSizePolicy(sizePolicy3)
        self.narrativeSimilarityLineEdit.setStyleSheet(u"")
        self.narrativeSimilarityLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.narrativeSimilarityLineEdit)


        self.verticalLayout.addWidget(self.narrativeSimilarityFrame)

        self.matchedWordFrame = QFrame(self.ribbonSubContainer)
        self.matchedWordFrame.setObjectName(u"matchedWordFrame")
        self.matchedWordFrame.setStyleSheet(u"")
        self.matchedWordFrame.setFrameShape(QFrame.StyledPanel)
        self.matchedWordFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.matchedWordFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.matchedWordLabel = QLabel(self.matchedWordFrame)
        self.matchedWordLabel.setObjectName(u"matchedWordLabel")
        sizePolicy2.setHeightForWidth(self.matchedWordLabel.sizePolicy().hasHeightForWidth())
        self.matchedWordLabel.setSizePolicy(sizePolicy2)
        self.matchedWordLabel.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.matchedWordLabel)

        self.matchedWordLineEdit = QLineEdit(self.matchedWordFrame)
        self.matchedWordLineEdit.setObjectName(u"matchedWordLineEdit")
        sizePolicy3.setHeightForWidth(self.matchedWordLineEdit.sizePolicy().hasHeightForWidth())
        self.matchedWordLineEdit.setSizePolicy(sizePolicy3)
        self.matchedWordLineEdit.setStyleSheet(u"")
        self.matchedWordLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.matchedWordLineEdit)


        self.verticalLayout.addWidget(self.matchedWordFrame)

        self.matchedNumberFrame = QFrame(self.ribbonSubContainer)
        self.matchedNumberFrame.setObjectName(u"matchedNumberFrame")
        self.matchedNumberFrame.setStyleSheet(u"")
        self.matchedNumberFrame.setFrameShape(QFrame.StyledPanel)
        self.matchedNumberFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.matchedNumberFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.matchedNumberLabel = QLabel(self.matchedNumberFrame)
        self.matchedNumberLabel.setObjectName(u"matchedNumberLabel")
        sizePolicy2.setHeightForWidth(self.matchedNumberLabel.sizePolicy().hasHeightForWidth())
        self.matchedNumberLabel.setSizePolicy(sizePolicy2)
        self.matchedNumberLabel.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.matchedNumberLabel)

        self.matchedNumberLineEdit = QLineEdit(self.matchedNumberFrame)
        self.matchedNumberLineEdit.setObjectName(u"matchedNumberLineEdit")
        sizePolicy3.setHeightForWidth(self.matchedNumberLineEdit.sizePolicy().hasHeightForWidth())
        self.matchedNumberLineEdit.setSizePolicy(sizePolicy3)
        self.matchedNumberLineEdit.setStyleSheet(u"")
        self.matchedNumberLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.matchedNumberLineEdit)


        self.verticalLayout.addWidget(self.matchedNumberFrame)

        self.accountNumberMatchFrame = QFrame(self.ribbonSubContainer)
        self.accountNumberMatchFrame.setObjectName(u"accountNumberMatchFrame")
        self.accountNumberMatchFrame.setStyleSheet(u"")
        self.accountNumberMatchFrame.setFrameShape(QFrame.StyledPanel)
        self.accountNumberMatchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.accountNumberMatchFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountNumberMatchLabel = QLabel(self.accountNumberMatchFrame)
        self.accountNumberMatchLabel.setObjectName(u"accountNumberMatchLabel")
        sizePolicy2.setHeightForWidth(self.accountNumberMatchLabel.sizePolicy().hasHeightForWidth())
        self.accountNumberMatchLabel.setSizePolicy(sizePolicy2)
        self.accountNumberMatchLabel.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.accountNumberMatchLabel)

        self.accountNumberMatchLineEdit = QLineEdit(self.accountNumberMatchFrame)
        self.accountNumberMatchLineEdit.setObjectName(u"accountNumberMatchLineEdit")
        sizePolicy3.setHeightForWidth(self.accountNumberMatchLineEdit.sizePolicy().hasHeightForWidth())
        self.accountNumberMatchLineEdit.setSizePolicy(sizePolicy3)
        self.accountNumberMatchLineEdit.setStyleSheet(u"")
        self.accountNumberMatchLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.accountNumberMatchLineEdit)


        self.verticalLayout.addWidget(self.accountNumberMatchFrame)

        self.accountNumber4DigitsMatchFrame = QFrame(self.ribbonSubContainer)
        self.accountNumber4DigitsMatchFrame.setObjectName(u"accountNumber4DigitsMatchFrame")
        self.accountNumber4DigitsMatchFrame.setStyleSheet(u"")
        self.accountNumber4DigitsMatchFrame.setFrameShape(QFrame.StyledPanel)
        self.accountNumber4DigitsMatchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.accountNumber4DigitsMatchFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.accountNumber4DigitsMatchFrameLabel = QLabel(self.accountNumber4DigitsMatchFrame)
        self.accountNumber4DigitsMatchFrameLabel.setObjectName(u"accountNumber4DigitsMatchFrameLabel")
        sizePolicy2.setHeightForWidth(self.accountNumber4DigitsMatchFrameLabel.sizePolicy().hasHeightForWidth())
        self.accountNumber4DigitsMatchFrameLabel.setSizePolicy(sizePolicy2)
        self.accountNumber4DigitsMatchFrameLabel.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.accountNumber4DigitsMatchFrameLabel)

        self.accountNumber4DigitsMatchFrameLineEdit = QLineEdit(self.accountNumber4DigitsMatchFrame)
        self.accountNumber4DigitsMatchFrameLineEdit.setObjectName(u"accountNumber4DigitsMatchFrameLineEdit")
        sizePolicy.setHeightForWidth(self.accountNumber4DigitsMatchFrameLineEdit.sizePolicy().hasHeightForWidth())
        self.accountNumber4DigitsMatchFrameLineEdit.setSizePolicy(sizePolicy)
        self.accountNumber4DigitsMatchFrameLineEdit.setStyleSheet(u"")
        self.accountNumber4DigitsMatchFrameLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.accountNumber4DigitsMatchFrameLineEdit)


        self.verticalLayout.addWidget(self.accountNumber4DigitsMatchFrame)

        self.nonRoundedAmountFrame = QFrame(self.ribbonSubContainer)
        self.nonRoundedAmountFrame.setObjectName(u"nonRoundedAmountFrame")
        self.nonRoundedAmountFrame.setStyleSheet(u"")
        self.nonRoundedAmountFrame.setFrameShape(QFrame.StyledPanel)
        self.nonRoundedAmountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.nonRoundedAmountFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.nonRoundedAmountLabel = QLabel(self.nonRoundedAmountFrame)
        self.nonRoundedAmountLabel.setObjectName(u"nonRoundedAmountLabel")
        sizePolicy2.setHeightForWidth(self.nonRoundedAmountLabel.sizePolicy().hasHeightForWidth())
        self.nonRoundedAmountLabel.setSizePolicy(sizePolicy2)
        self.nonRoundedAmountLabel.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.nonRoundedAmountLabel)

        self.nonRoundedAmountLineEdit = QLineEdit(self.nonRoundedAmountFrame)
        self.nonRoundedAmountLineEdit.setObjectName(u"nonRoundedAmountLineEdit")
        sizePolicy3.setHeightForWidth(self.nonRoundedAmountLineEdit.sizePolicy().hasHeightForWidth())
        self.nonRoundedAmountLineEdit.setSizePolicy(sizePolicy3)
        self.nonRoundedAmountLineEdit.setStyleSheet(u"")
        self.nonRoundedAmountLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.nonRoundedAmountLineEdit)


        self.verticalLayout.addWidget(self.nonRoundedAmountFrame)

        self.minAmountFrame = QFrame(self.ribbonSubContainer)
        self.minAmountFrame.setObjectName(u"minAmountFrame")
        self.minAmountFrame.setStyleSheet(u"")
        self.minAmountFrame.setFrameShape(QFrame.StyledPanel)
        self.minAmountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.minAmountFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.minAmountLabel = QLabel(self.minAmountFrame)
        self.minAmountLabel.setObjectName(u"minAmountLabel")
        sizePolicy2.setHeightForWidth(self.minAmountLabel.sizePolicy().hasHeightForWidth())
        self.minAmountLabel.setSizePolicy(sizePolicy2)
        self.minAmountLabel.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.minAmountLabel)

        self.minAmountLineEdit = QLineEdit(self.minAmountFrame)
        self.minAmountLineEdit.setObjectName(u"minAmountLineEdit")
        sizePolicy3.setHeightForWidth(self.minAmountLineEdit.sizePolicy().hasHeightForWidth())
        self.minAmountLineEdit.setSizePolicy(sizePolicy3)
        self.minAmountLineEdit.setStyleSheet(u"")
        self.minAmountLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.minAmountLineEdit)


        self.verticalLayout.addWidget(self.minAmountFrame)

        self.minThresholdFrame = QFrame(self.ribbonSubContainer)
        self.minThresholdFrame.setObjectName(u"minThresholdFrame")
        self.minThresholdFrame.setStyleSheet(u"")
        self.minThresholdFrame.setFrameShape(QFrame.StyledPanel)
        self.minThresholdFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.minThresholdFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.minThresholdLabel = QLabel(self.minThresholdFrame)
        self.minThresholdLabel.setObjectName(u"minThresholdLabel")
        sizePolicy2.setHeightForWidth(self.minThresholdLabel.sizePolicy().hasHeightForWidth())
        self.minThresholdLabel.setSizePolicy(sizePolicy2)
        self.minThresholdLabel.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.minThresholdLabel)

        self.minThresholdLineEdit = QLineEdit(self.minThresholdFrame)
        self.minThresholdLineEdit.setObjectName(u"minThresholdLineEdit")
        sizePolicy3.setHeightForWidth(self.minThresholdLineEdit.sizePolicy().hasHeightForWidth())
        self.minThresholdLineEdit.setSizePolicy(sizePolicy3)
        self.minThresholdLineEdit.setStyleSheet(u"")
        self.minThresholdLineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.minThresholdLineEdit)


        self.verticalLayout.addWidget(self.minThresholdFrame)

        self.matchTransactionsBtn = QPushButton(self.ribbonSubContainer)
        self.matchTransactionsBtn.setObjectName(u"matchTransactionsBtn")
        sizePolicy.setHeightForWidth(self.matchTransactionsBtn.sizePolicy().hasHeightForWidth())
        self.matchTransactionsBtn.setSizePolicy(sizePolicy)
        self.matchTransactionsBtn.setMinimumSize(QSize(0, 0))
        self.matchTransactionsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.matchTransactionsBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.matchTransactionsBtn)

        self.loadCategoriesBtn = QPushButton(self.ribbonSubContainer)
        self.loadCategoriesBtn.setObjectName(u"loadCategoriesBtn")
        sizePolicy.setHeightForWidth(self.loadCategoriesBtn.sizePolicy().hasHeightForWidth())
        self.loadCategoriesBtn.setSizePolicy(sizePolicy)
        self.loadCategoriesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadCategoriesBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.loadCategoriesBtn)

        self.categoriseTransactionsBtn = QPushButton(self.ribbonSubContainer)
        self.categoriseTransactionsBtn.setObjectName(u"categoriseTransactionsBtn")
        sizePolicy.setHeightForWidth(self.categoriseTransactionsBtn.sizePolicy().hasHeightForWidth())
        self.categoriseTransactionsBtn.setSizePolicy(sizePolicy)
        self.categoriseTransactionsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.categoriseTransactionsBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.categoriseTransactionsBtn)

        self.searchMatchesBtn = QPushButton(self.ribbonSubContainer)
        self.searchMatchesBtn.setObjectName(u"searchMatchesBtn")
        sizePolicy.setHeightForWidth(self.searchMatchesBtn.sizePolicy().hasHeightForWidth())
        self.searchMatchesBtn.setSizePolicy(sizePolicy)
        self.searchMatchesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchMatchesBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.searchMatchesBtn)

        self.visualiseFlowOfFundsBtn = QPushButton(self.ribbonSubContainer)
        self.visualiseFlowOfFundsBtn.setObjectName(u"visualiseFlowOfFundsBtn")

        self.verticalLayout.addWidget(self.visualiseFlowOfFundsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.uploadMatchesToDBBtn = QPushButton(self.ribbonSubContainer)
        self.uploadMatchesToDBBtn.setObjectName(u"uploadMatchesToDBBtn")
        self.uploadMatchesToDBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uploadMatchesToDBBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.uploadMatchesToDBBtn)

        self.exportMatchesToExcelBtn = QPushButton(self.ribbonSubContainer)
        self.exportMatchesToExcelBtn.setObjectName(u"exportMatchesToExcelBtn")
        self.exportMatchesToExcelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportMatchesToExcelBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.exportMatchesToExcelBtn)


        self.horizontalLayout.addWidget(self.ribbonSubContainer)


        self.retranslateUi(matchRibbonContainer)

        QMetaObject.connectSlotsByName(matchRibbonContainer)
    # setupUi

    def retranslateUi(self, matchRibbonContainer):
        matchRibbonContainer.setWindowTitle(QCoreApplication.translate("matchRibbonContainer", u"Form", None))
        self.loadMatchesFromDBBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Load From Database", None))
        self.loadMatchesFromExcelBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Load From Excel", None))
        self.manualMatchesBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Manual Matches", None))
        self.manualUnmatchBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Manual Unmatch", None))
        self.keyPartiesEntitiesBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Key Parties and Entities", None))
        self.keywordMatchLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Keyword Match", None))
        self.keywordMatchLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"1", None))
        self.narrativeSimilarityLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Narrative Similarity", None))
        self.narrativeSimilarityLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"1", None))
        self.matchedWordLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Matched Word", None))
        self.matchedWordLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"0.33", None))
        self.matchedNumberLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Matched Number", None))
        self.matchedNumberLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"1", None))
        self.accountNumberMatchLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Account Number Match", None))
        self.accountNumberMatchLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"3", None))
        self.accountNumber4DigitsMatchFrameLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Last 4 Digits Match", None))
        self.accountNumber4DigitsMatchFrameLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"2", None))
        self.nonRoundedAmountLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Non-Rounded Amount", None))
        self.nonRoundedAmountLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"1", None))
        self.minAmountLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Minimum Match Amount", None))
        self.minAmountLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"0", None))
        self.minThresholdLabel.setText(QCoreApplication.translate("matchRibbonContainer", u"Minimum Score", None))
        self.minThresholdLineEdit.setText(QCoreApplication.translate("matchRibbonContainer", u"0", None))
        self.matchTransactionsBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Match Transactions", None))
        self.loadCategoriesBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Load Categories", None))
        self.categoriseTransactionsBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Categorise Transactions", None))
        self.searchMatchesBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Search Matches", None))
        self.visualiseFlowOfFundsBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Visualise Flow of Funds", None))
        self.uploadMatchesToDBBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Upload to Database", None))
        self.exportMatchesToExcelBtn.setText(QCoreApplication.translate("matchRibbonContainer", u"Export to Excel", None))
    # retranslateUi

