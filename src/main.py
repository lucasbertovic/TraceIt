import sys
from ui_interface import *
from traceRibbon import *
from matchRibbon import *
from Custom_Widgets.Widgets import *
from tracer_classes import *
import MultiComboBox
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QUrl, QFileSystemWatcher, QThreadPool, Qt
from PySide2.QtWidgets import  QSplitter
from PySide2 import  QtCore
from tkinter import Tk, filedialog
import pandas as pd
from anytree import Node
import copy
import json
from datetime import datetime
import re
import copy
from functions import *
import os
import numpy as np

class Model():
    def __init__(self):
        self._clickedNode = None
        self._observers = []
        self.applicationsDictionary = None
        self.categories = None
        self.conversionLayout6 = None
        self.conversionLayout8 = None
        self.copiedCategory = None
        self.counter = None
        self.currentTraceLevelView = None
        self.currentViewingTransaction = None
        self.db = None
        self.displayMatchesSearchBar = False
        self.displayTraceSearchBar = False
        self.endPointUpdateSwitch = False
        self.graphConfig = {"hSpacing": 60, "vSpacing":80, "outerCircle": 10, "innerCircle": 7, "fontSize":10, "boxOpacity":0, "labelOpacity":0}
        self.lollipopConfig = {"height" : 830}
        self.lollipopLegendColourPalette = ["#673ab7", "#e1bee7", "#ffffff", "#f3e5f5", "#d5a6bd"]
        self.manualMatches = None
        self.manualUnmatch = None
        self.matchContentsView = 'Table'
        self.matchContentsViewChord = None
        self.matchContentsViewTable = None
        self.matchingLayout6 = None
        self.matchingLayout8 = None
        self.matchesFilePath = None
        self.matchesTableString = None
        self.methodology = None
        self.nodes = None
        self.refTable = None
        self.rootNode = None
        self.server = None
        self.stampCategories = None
        self.stampManualMatches = None
        self.stampManualUnmatch = None
        self.stampPossibleMatches = None
        self.stampRefTable = None
        self.startingTransaction = None
        self.startingTransactions = None
        self.traceContentsView = 'Tree'
        self.tracePaths = {}
        self.traceQueue = None
        self.traceTransactionData = {}
        self.transactions = None
        self.transactionsDF = None
        self.transactionsFilePath = None
        self.treeNodeLabelsVisible = False
        self.tracingLayout6 = None
        self.tracingLayout8 = None
        self.uiView = 'Tracing'

    @property
    def clickedNode(self):
        return self._clickedNode

    @clickedNode.setter
    def clickedNode(self, value):
        self._clickedNode = value
        self.notifyObservers()

    def addObserver(self, observer):
        self._observers.append(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer()

class MainWindow(QMainWindow):
    def __init__(self,  serverThread):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serverThread = serverThread
        self.matchesSearchBar = SearchBar()


        #region Trace Search Bar 
        self.traceSearchBar = SearchBar()
        self.traceSearchBar.label = QLabel("")
        self.traceSearchBar.spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.traceSearchBar.previousButton = QPushButton("Previous")
        self.traceSearchBar.nextButton = QPushButton("Next")
        layout = self.traceSearchBar.layout()
        layout.addWidget(self.traceSearchBar.label)
        layout.addSpacerItem(self.traceSearchBar.spacer)
        layout.addWidget(self.traceSearchBar.searchButton)
        layout.addSpacerItem(self.traceSearchBar.spacer)
        layout.addWidget(self.traceSearchBar.previousButton)
        layout.addSpacerItem(self.traceSearchBar.spacer)
        layout.addWidget(self.traceSearchBar.nextButton)
        self.traceSearchBar.results = None
        #endregion
                


        #region Banners
        self.traceBanner = TraceBannerWidget()
        self.matchBanner = MatchBannerWidget()
        self.ui.verticalLayout_8.insertWidget(0,self.traceBanner)
        #endregion

        #region Match/Trace Table
        delegate = CustomDelegate()
        self.ui.matchTable.setItemDelegate(delegate)
        self.ui.matchTable.setSortingEnabled(True)
        self.ui.verticalLayout_8.removeWidget(self.ui.matchTable) # Match table in Qt designer but dont show in trace view. Add it back later
        self.ui.matchTable.hide()
        self.header = self.ui.traceTable.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.header.setSectionResizeMode(QHeaderView.Interactive)
        self.ui.traceTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.traceTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.mainContentsContainer.resizeEvent = lambda event: self.updateColumnWidths(self.ui.mainContentsContainer)
        #endregion

        #region Trace Ribbon 
        self.traceRibbon = QWidget()
        self.traceRibbonUI = Ui_ribbonContainer()
        self.traceRibbonUI.setupUi(self.traceRibbon)
        self.traceRibbonUI.combo = MultiComboBox.CheckableComboBox()
        index = self.traceRibbonUI.verticalLayout.indexOf(self.traceRibbonUI.startingTransactionsComboBox)
        self.traceRibbonUI.verticalLayout.insertWidget(index+1, self.traceRibbonUI.combo)
        self.ui.startingTransactionsBtn = self.traceRibbonUI.startingTransactionsBtn
        self.ui.startingTransactionsBtn.setObjectName(u"startingTransactionsBtn")
        self.ui.verticalLayout_6.addWidget(self.traceRibbon)
        #endregion

        #region Match Ribbon
        self.matchRibbon = QWidget()
        self.matchRibbonUI = Ui_matchRibbonContainer()
        self.matchRibbonUI.setupUi(self.matchRibbon)
        self.ui.loadMatchesFromDBBtn = self.matchRibbonUI.loadMatchesFromDBBtn
        self.ui.loadMatchesFromDBBtn.setObjectName(u"loadMatchesFromDBBtn")
        self.ui.manualMatchesBtn = self.matchRibbonUI.manualMatchesBtn
        self.ui.manualMatchesBtn.setObjectName(u"manualMatchesBtn")
        self.ui.manualUnmatchBtn = self.matchRibbonUI.manualUnmatchBtn
        self.ui.manualUnmatchBtn.setObjectName(u"manualUnmatchBtn")
        self.ui.keyPartiesEntitiesBtn = self.matchRibbonUI.keyPartiesEntitiesBtn
        self.ui.keyPartiesEntitiesBtn.setObjectName(u"keyPartiesEntitiesBtn")
        self.ui.loadCategoriesBtn = self.matchRibbonUI.loadCategoriesBtn
        self.ui.loadCategoriesBtn.setObjectName(u"loadCategoriesBtn")
        self.matchRibbonUI.ribbonSubContainer.resizeEvent = lambda event: self.updateMatchRibbonFontSize(self.matchRibbonUI.ribbonSubContainer)
        self.traceRibbonUI.traceRibbonSubContainer.resizeEvent = lambda event: self.updateMatchRibbonFontSize(self.traceRibbonUI.traceRibbonSubContainer)
        #endregion
        
        #region Tree Diagram
        self.treeWebView = QWebEngineView()
        self.treePage = LoggedPage()
        self.treeWebView.setPage(self.treePage)
        self.treeWebView.setUrl(QUrl("http://localhost:8000/src/index.html"))
        self.treeWebView.page().setBackgroundColor(QColor("#1f232a"))
        self.treeWebView.page().profile().clearHttpCache()
        self.treeWebView.setFocusPolicy(Qt.StrongFocus)
        self.ui.verticalLayout_8.insertWidget(1,self.treeWebView)
        self.treeDiagramFileWatcher = QFileSystemWatcher()
        self.treeDiagramFileWatcher.addPaths(['config/tree.json', 'src/index.html'])
        #endregion

        #region Chord Diagram
        self.chordWebView = QWebEngineView()
        self.chordPage = LoggedPage()
        self.chordWebView.setPage(self.chordPage)
        self.chordWebView.setUrl(QUrl("http://localhost:8000/src/chord.html"))
        self.chordWebView.page().setBackgroundColor(QColor("#1f232a"))
        self.chordWebView.page().profile().clearHttpCache()
        self.chordWebView.setFocusPolicy(Qt.StrongFocus)
        self.chordWebView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chordDiagramFileWatcher = QFileSystemWatcher()
        self.chordDiagramFileWatcher.addPaths(['config/chord.json', 'src/chord.html'])
        #endregion

        #region Lollipop Diagram
        self.lollipopWebView = QWebEngineView()
        self.lollipopPage = LoggedPage()
        self.lollipopWebView.setPage(self.lollipopPage)
        self.lollipopWebView.setUrl(QUrl("http://localhost:8000/src/lollipop.html"))
        self.lollipopWebView.page().setBackgroundColor(QColor("#1f232a"))
        self.lollipopWebView.page().profile().clearHttpCache()
        self.lollipopWebView.setFocusPolicy(Qt.StrongFocus)
        self.lollipopWebView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lollipopDiagramFileWatcher = QFileSystemWatcher()
        self.lollipopDiagramFileWatcher.addPaths(['config/applications.json', 'src/lollipop.html'])
        #endregion

        #region Splitter
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.ui.verticalLayout_8.removeWidget(self.ui.traceTable)
        self.ui.verticalLayout_8.addWidget(self.splitter)
        self.splitter.addWidget(self.treeWebView)
        self.splitter.addWidget(self.ui.traceTable)
        #endregion

        #region Input Data Storage
        self.startingTransactionsLineEdits = [self.ui.startingTransactionsLineEdit]
        self.manualMatchesLineEdits = [[self.ui.manualMatchesLineEdit1, self.ui.manualMatchesLineEdit2]]
        self.manualUnmatchLineEdits = [[self.ui.manualUnmatchLineEdit1, self.ui.manualUnmatchLineEdit2]]
        self.refTableLineEdits = [[self.ui.refTableLineEdit1, self.ui.refTableLineEdit2]]
        self.categoriesLineEdits = [[self.ui.categoriesLineEdit1, self.ui.categoriesLineEdit2]]
        #endregion

        loadJsonStyle(self, self.ui)

    # Adjustable font sizes
    def showEvent(self, event):
        desktop = QDesktopWidget()
        screenGeometry = desktop.availableGeometry()
        self.setGeometry(screenGeometry)

    def updateMatchRibbonFontSize(self, frame):
        frame_size = frame.size()
        font_size = min(9,max(int(frame_size.height() * 0.015),7))
        for button in frame.findChildren(QPushButton):
            button_font = button.font()
            button_font.setPointSize(font_size)
            button.setFont(button_font)
        for label in frame.findChildren(QLabel):
            label_font = label.font()
            label_font.setPointSize(font_size)
            label.setFont(label_font)

    # Columns need to be in the same ratio
    def updateColumnWidths(self, frame):
        if frame.size().width() >= 900:
            scale = (frame.size().width()-40)/31.8 
            columnWeights = [3,   2.6, 2, 2,  7.6 , 2 , 2, 2.6, 3 ,1 ,2,2] # 31.8 units
            column_widths = [x*scale for x in columnWeights]
            for i, width in enumerate(column_widths):
                self.ui.matchTable.setColumnWidth(i, width)
        font = self.ui.matchTable.font()
        default_font_size = font.pointSize()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        #Clear JSON files
        self.clearJSON('config/tree.json')
        self.clearJSON('config/chord.json')
        self.clearJSON('config/applications.json')
        # SET BUTTON CONFIGURATIONS
        self.model.addObserver(self.clickedNodeChanged)
        self.view.chordDiagramFileWatcher.fileChanged.connect(self.reloadChordHTML)
        self.view.lollipopDiagramFileWatcher.fileChanged.connect(self.reloadLollipopHTML)
        self.view.matchRibbonUI.categoriseTransactionsBtn.clicked.connect(self.categoriseTransactionsBtn)
        self.view.matchRibbonUI.exportMatchesToExcelBtn.clicked.connect(self.exportMatchesToExcelBtn)
        self.view.matchRibbonUI.loadMatchesFromExcelBtn.clicked.connect(self.loadMatchesFromExcelBtn)
        self.view.matchRibbonUI.matchTransactionsBtn.clicked.connect(self.matchTransactionsBtn)
        self.view.matchRibbonUI.searchMatchesBtn.clicked.connect(self.toggleMatchesSearch)
        self.view.matchRibbonUI.uploadMatchesToDBBtn.clicked.connect(self.uploadMatchesToDBBtn)
        self.view.matchRibbonUI.visualiseFlowOfFundsBtn.clicked.connect(self.visualiseFlowOfFunds)
        self.view.matchesSearchBar.searchButton.clicked.connect(self.searchMatches)
        self.view.matchesSearchBar.searchEdit.returnPressed.connect(self.searchMatches)
        self.view.traceRibbonUI.applicationOfFundsBtn.clicked.connect(self.visualiseApplications)
        self.view.traceRibbonUI.combo.combo_box.model().itemChanged.connect(self.onEndPointItemChanged)
        self.view.traceRibbonUI.fifoBtn.clicked.connect(lambda: self.updateMethodology('FIFO'))
        self.view.traceRibbonUI.librNRBtn.clicked.connect(lambda: self.updateMethodology('LIBRNR'))
        self.view.traceRibbonUI.librRBtn.clicked.connect(lambda: self.updateMethodology('LIBRR'))
        self.view.traceRibbonUI.lifoBtn.clicked.connect(lambda: self.updateMethodology('LIFO'))
        self.view.traceRibbonUI.poisonChaliceBtn.clicked.connect(lambda: self.updateMethodology('PC'))
        self.view.traceRibbonUI.runTracingBtn.clicked.connect(self.runTracingButton)
        self.view.traceRibbonUI.searchTraceBtn.clicked.connect(self.toggleTraceSearch)
        self.view.traceRibbonUI.showTraceLabelsBtn.clicked.connect(self.toggleTraceLabels)
        self.view.traceRibbonUI.startingTransactionsComboBox.currentTextChanged.connect(self.startingTransactionsComboBoxChanged)
        self.view.traceSearchBar.nextButton.clicked.connect(self.nextTraceSearchResult)
        self.view.traceSearchBar.previousButton.clicked.connect(self.previousTraceSearchResult)
        self.view.traceSearchBar.searchButton.clicked.connect(self.searchTrace)
        self.view.traceSearchBar.searchEdit.returnPressed.connect(self.searchTrace)
        self.view.treeDiagramFileWatcher.fileChanged.connect(self.reloadTreeHTML)
        self.view.treePage.newData.connect(self.returnJavaScriptConsoleLog)
        self.view.ui.addCategoriesRowBtn.clicked.connect(self.addCategoriesRow)
        self.view.ui.addManualMatchesRowBtn.clicked.connect(self.addManualMatchesRow)
        self.view.ui.addManualUnmatchRowBtn.clicked.connect(self.addManualUnmatchRow)
        self.view.ui.addRefTableRowBtn.clicked.connect(self.addRefTableRow)
        self.view.ui.addStartingTransactionsRowBtn.clicked.connect(self.addStartingTransactionsRow)
        self.view.ui.closeCategoriesBtn.clicked.connect(self.closeCategories)
        self.view.ui.closeCenterMenuBtn.clicked.connect(lambda: self.view.ui.centerMenuContainer.collapseMenu())
        self.view.ui.closeManualMatchesBtn.clicked.connect(self.closeManualMatches)
        self.view.ui.closeManualUnmatchBtn.clicked.connect(self.closeManualUnmatch)
        self.view.ui.closeNotificationBtn.clicked.connect(lambda: self.view.ui.popupNotificationContainer.collapseMenu())
        self.view.ui.closeRefTableBtn.clicked.connect(self.closeRefTable)
        self.view.ui.closeRightMenuBtn.clicked.connect(lambda: self.view.ui.rightMenuContainer.collapseMenu())
        self.view.ui.closeServerDBBtn.clicked.connect(self.closeServerDB)
        self.view.ui.closeStartingTransactionsBtn.clicked.connect(self.closeStartingTransactions)
        self.view.ui.loadCategoriesFromFileBtn.clicked.connect(self.loadCategoriesFromFile)
        self.view.ui.loadManualMatchesFromFileBtn.clicked.connect(self.loadManualMatchesFromFile)
        self.view.ui.loadManualUnmatchFromFileBtn.clicked.connect(self.loadManualUnmatchFromFile)
        self.view.ui.loadRefTableFromFileBtn.clicked.connect(self.loadRefTableFromFile)
        self.view.ui.loadStartingTransactionsFromFileBtn.clicked.connect(self.loadStartingTransactionsFromFile)
        self.view.ui.matchTable.cellChanged.connect(self.matchTableCategoryChanged)
        self.view.ui.matchTable.customContextMenuRequested.connect(self.matchTableRightClickMenu)
        self.view.ui.matchTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.ui.matchTable.updateCategoryChanges = True
        self.view.ui.matchingBtn.clicked.connect(self.matchingBtnClicked)
        self.view.ui.moreMenuBtn.clicked.connect(lambda: self.view.ui.centerMenuContainer.expandMenu())
        self.view.ui.submitCategoriesBtn.clicked.connect(self.submitCategories)
        self.view.ui.submitManualMatchesBtn.clicked.connect(self.submitManualMatches)
        self.view.ui.submitManualUnmatchBtn.clicked.connect(self.submitManualUnmatch)
        self.view.ui.submitRefTableBtn.clicked.connect(self.submitRefTable)
        self.view.ui.submitStartingTransactionsBtn.clicked.connect(self.submitStartingTransactions)
        self.view.ui.submitTraceServerDBBtn.clicked.connect(self.submitServerDB)
        self.view.ui.traceTable.cellDoubleClicked.connect(self.onCellDbouleClicked)
        self.view.ui.traceTable.customContextMenuRequested.connect(self.traceTableRightClickMenu)
        self.view.ui.traceTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.view.ui.tracingBtn.clicked.connect(self.tracingBtnClicked)

    #region Update Banner Labels
    #Trace Banner
    def updateTransactionCountLabel(self, number):
        transactionCount = "{:,}".format(number)
        text = f'{transactionCount} transactions loaded'
        styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
        self.view.traceBanner.label1.setText(text)
        self.view.traceBanner.label1.setStyleSheet(styleSheet)

    def updateMatchedTransactionCountLabel(self, number):
        if number > 0:
            matchedTransactionCount = "{:,}".format(number)
            text = f'{matchedTransactionCount} transactions matched'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.traceBanner.label2.setText(text)
            self.view.traceBanner.label2.setStyleSheet(styleSheet)

    def updateStartingTransactionCountLabel(self, number):
        if number > 0:
            startingTransactionCount = "{:,}".format(number)
            text = f'{startingTransactionCount} starting transactions selected'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.traceBanner.label3.setText(text)
            self.view.traceBanner.label3.setStyleSheet(styleSheet)

    def updateMethodologyLabel(self, text):
        styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
        self.view.traceBanner.label4.setText(text)
        self.view.traceBanner.label4.setStyleSheet(styleSheet)
    
    def updateStartingAmountLabel(self, text):
        styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
        self.view.traceBanner.label5.setText(text)
        self.view.traceBanner.label5.setStyleSheet(styleSheet)

    def updateEndPointsAmountLabel(self, text):
        styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
        self.view.traceBanner.label6.setText(text)
        self.view.traceBanner.label6.setStyleSheet(styleSheet)

    #Match Banner
    def updateTransactionsLoadedLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} transactions loaded'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label1.setText(text)
            self.view.matchBanner.label1.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label1.setText('0 transactions loaded')
            self.view.matchBanner.label1.setStyleSheet("background-color:  #2c313c; color: #949494")
    
    def updateManualMatchesCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} manual matches'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label2.setText(text)
            self.view.matchBanner.label2.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label2.setText('0 manual matches')
            self.view.matchBanner.label2.setStyleSheet("background-color:  #2c313c; color: #949494")

    def updateManualUnmatchCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} manual unmatches'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label3.setText(text)
            self.view.matchBanner.label3.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label3.setText('0 manual unmatches')
            self.view.matchBanner.label3.setStyleSheet("background-color:  #2c313c; color: #949494")

    def updateRefTableCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} party/entity search terms'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label4.setText(text)
            self.view.matchBanner.label4.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label4.setText("0 party/entity search terms")
            self.view.matchBanner.label4.setStyleSheet("background-color:  #2c313c; color: #949494")

    def updateCategoriesCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} category search terms'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label5.setText(text)
            self.view.matchBanner.label5.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label5.setText('0 category search terms')
            self.view.matchBanner.label5.setStyleSheet("background-color:  #2c313c; color: #949494")

    def updateMatchedTransactionsCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} matched transactions'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label6.setText(text)
            self.view.matchBanner.label6.setStyleSheet(styleSheet)
        else:
            self.view.matchBanner.label6.setText('0 transactions categorised')
            self.view.matchBanner.label6.setStyleSheet("0 party/entity search terms")

    def updateTransactionsCategorisedCountLabel(self, number):
        if number > 0:
            transactionCount = "{:,}".format(number)
            text = f'{transactionCount} transactions categorised'
            styleSheet = "background-color: #2c313c; border-top: 2px solid #8cffff; font-weight: bold;"
            self.view.matchBanner.label7.setText(text)
            self.view.matchBanner.label7.setStyleSheet(styleSheet)
    #endregion

    #region Pop Up Window Button Config
    # Add Row
    def addStartingTransactionsRow(self):
        # Add a new line edit
        new_line_edit = QLineEdit()
        self.view.ui.verticalLayout_10.insertWidget(self.view.ui.verticalLayout_10.count()-1, new_line_edit) 
        self.view.startingTransactionsLineEdits.append(new_line_edit)

    def addDoubleLineEditRow(self, layout, valuesList, value1='', value2=''):
        # Add a new line edit
        new_frame = QFrame()
        new_frame.setFrameShape(QFrame.StyledPanel)
        
        # Create a horizontal layout for the frame
        horizontal_layout = QHBoxLayout(new_frame)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(2) 
        new_frame.setLayout(horizontal_layout)
        styleSheet = '''QLineEdit {
                    background-color: #343a40; /* or #454f55 */
                    border: 1px solid #666666; /* or #808080 */
                    border-radius: 5px; /* or 8px */
                }'''
        
        # Add two line edits to the horizontal layout
        line_edit1 = QLineEdit()
        line_edit1.setText(str(value1))
        line_edit1.setStyleSheet(styleSheet)
        line_edit2 = QLineEdit()
        line_edit2.setText(str(value2))
        line_edit2.setStyleSheet(styleSheet)
        horizontal_layout.addWidget(line_edit1)
        horizontal_layout.addWidget(line_edit2)
        
        # Insert the new frame into the vertical layout
        layout.insertWidget(layout.count() - 1, new_frame)
        valuesList.append([line_edit1, line_edit2])
        
    def addManualMatchesRow(self):
        self.addDoubleLineEditRow(self.view.ui.verticalLayout_16, self.view.manualMatchesLineEdits)

    def addManualUnmatchRow(self):
        self.addDoubleLineEditRow(self.view.ui.verticalLayout_23, self.view.manualUnmatchLineEdits)

    def addRefTableRow(self):
        self.addDoubleLineEditRow(self.view.ui.verticalLayout_25, self.view.refTableLineEdits)

    def addCategoriesRow(self):
        self.addDoubleLineEditRow(self.view.ui.verticalLayout_27, self.view.categoriesLineEdits)

    # Load From File 
    def openExcelDialogue(self):
        root = Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Excel or CSV files", "*.xlsx *.csv")]
        )
        return file_path
    
    def clearLineEditsFromLayout(self, layout, valuesList):
        # Remove all line edits from a layout. Will be used to clear a popup before loading from a file
        items_to_remove = []
        
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget and isinstance(widget, QLineEdit):
                items_to_remove.append(widget)
                valuesList.pop(0)
        
        # Remove collected items
        for widget in items_to_remove:
            layout.removeWidget(widget)
            widget.setParent(None) 

    def clearLineEditFramesFromLayout(self, layout, valuesList):
        # Remove all line edit frames from a layout. Will be used to clear a popup before loading from a file
        items_to_remove = []
        
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget and isinstance(widget, QFrame):
                items_to_remove.append(widget)
                valuesList.pop(0)
        
        # Remove collected items
        for widget in items_to_remove:
            layout.removeWidget(widget)
            widget.setParent(None) 
  
    def loadStartingTransactionsFromFile(self):
        self.populateSingleLineEditsFromFile(self.view.ui.verticalLayout_10, self.view.startingTransactionsLineEdits)
    
    def populateSingleLineEditsFromFile(self, layout, valueList):
        # This will be used when loading starting transactions from file.
        file_path =self.openExcelDialogue()
        
        if file_path:
            vals = pd.read_csv(file_path).values.tolist()
            self.clearLineEditsFromLayout(layout, valueList)
            for val in vals:
                new_line_edit = QLineEdit()
                new_line_edit.setText(str(val[0]))
                layout.insertWidget(layout.count()-1, new_line_edit) 
                valueList.append(new_line_edit)

    def populateDoubleLineEditsFromFile(self, layout, valueList):
        # This will be used when loading input data like manual matches/unmatches/ref table/categories from file.
        file_path =self.openExcelDialogue()
        
        if file_path:
            vals = pd.read_csv(file_path).values.tolist()
            self.clearLineEditFramesFromLayout(layout, valueList)
            for i in range(len(vals)):
                self.addDoubleLineEditRow(layout, valueList, vals[i][0], vals[i][1])

    def loadManualMatchesFromFile(self):
        self.populateDoubleLineEditsFromFile(self.view.ui.verticalLayout_16, self.view.manualMatchesLineEdits)

    def loadRefTableFromFile(self):
        self.populateDoubleLineEditsFromFile(self.view.ui.verticalLayout_25, self.view.refTableLineEdits)

    def loadManualUnmatchFromFile(self):
        self.populateDoubleLineEditsFromFile(self.view.ui.verticalLayout_23, self.view.manualUnmatchLineEdits)

    def loadCategoriesFromFile(self):
        self.populateDoubleLineEditsFromFile(self.view.ui.verticalLayout_27, self.view.categoriesLineEdits)

    # Submit 
    def submitStartingTransactions(self):
        # Only load line edits which meet the transaction id format
        text_list = [line_edit.text() for line_edit in self.view.startingTransactionsLineEdits if bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', line_edit.text()))]
        self.model.startingTransactions = text_list

        self.updateStartingTransactionCountLabel(len(self.model.startingTransactions))
        self.view.ui.startingTransactionsContainer.collapseMenu()

    def submitServerDB(self):
        server = self.view.ui.dataBaseLineEdit.text()
        db = self.view.ui.serverLineEdit.text()
        table = self.view.ui.tableLineEdit.text()
        self.view.ui.serverDBContainer.collapseMenu()
        self.model.server = server
        self.model.db = db
        self.model.matchesTableString = table

    def submitManualMatches(self):
        # Only load line edits which meet the transaction id format
        refIDPattern = r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$'
        textList = [[l[0].text(), l[1].text()] for l in self.view.manualMatchesLineEdits if  bool(re.match(refIDPattern, l[0].text())) and bool(re.match(refIDPattern, l[1].text()))]
        self.model.manualMatches = textList
        self.updateManualMatchesCountLabel(len(textList))
        self.view.ui.manualMatchesContainer.collapseMenu()

    def submitManualUnmatch(self):
        # Only load line edits which meet the transaction id format
        refIDPattern = r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$'
        textList = [[l[0].text(), l[1].text()] for l in self.view.manualUnmatchLineEdits if  bool(re.match(refIDPattern, l[0].text())) and bool(re.match(refIDPattern, l[1].text()))]
        self.model.manualUnmatch = textList
        self.updateManualUnmatchCountLabel(len(textList))
        self.view.ui.manualUnmatchContainer.collapseMenu()

    def submitRefTable(self):
        textList = [[l[0].text(), l[1].text()] for l in self.view.refTableLineEdits if len(l[0].text()) > 0 and len(l[1].text()) > 0]
        self.model.refTable = textList
        self.updateRefTableCountLabel(len(textList))
        self.view.ui.refTableContainer.collapseMenu()

    def submitCategories(self):
        textList = [[l[0].text(), l[1].text()] for l in self.view.categoriesLineEdits if len(l[0].text()) > 0 and len(l[1].text()) > 0]
        self.model.categories = textList
        self.updateCategoriesCountLabel(len(textList))
        self.view.ui.categoriesContainer.collapseMenu()

    # Close
    def closeStartingTransactions(self):
        self.view.ui.startingTransactionsContainer.collapseMenu()

    def closeServerDB(self):
        self.view.ui.serverDBContainer.collapseMenu()

    def closeManualMatches(self):
        self.view.ui.manualMatchesContainer.collapseMenu()

    def closeManualUnmatch(self):
        self.view.ui.manualUnmatchContainer.collapseMenu()
    
    def closeRefTable(self):
        self.view.ui.refTableContainer.collapseMenu()
    
    def closeCategories(self):
        self.view.ui.categoriesContainer.collapseMenu()
    #endregion
    
    #region Window Switching
    def tracingBtnClicked(self):
        # Switch between windows. Remove widgets from the layout, store them in the model, and replace with the new widgets.
        if self.model.uiView == 'Tracing':
            return
        elif self.model.uiView == 'Matching':
            self.model.matchingLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.matchingLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)
        elif self.model.uiView == 'Conversion':
            self.model.conversionLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.conversionLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)

        self.model.uiView = 'Tracing'
        self.view.ui.tracingBtn.setStyleSheet("background-color: #2c313c;")
        self.leftMenuBtnUnclicked(self.view.ui.matchingBtn)
        self.leftMenuBtnUnclicked(self.view.ui.conversionBtn)
        
        self.addWidgetsBackToLayout(self.view.ui.verticalLayout_8, self.model.tracingLayout8)
        self.addWidgetsBackToLayout(self.view.ui.verticalLayout_6, self.model.tracingLayout6)

    def matchingBtnClicked(self):
        # Switch between windows. Remove widgets from the layout, store them in the model, and replace with the new widgets.
        if self.model.uiView == 'Matching':
            return
        elif self.model.uiView == 'Tracing':
            self.model.tracingLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.tracingLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)
        elif self.model.uiView == 'Conversion':
            self.model.conversionLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.conversionLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)

        
        self.model.uiView = 'Matching'
        self.view.ui.matchingBtn.setStyleSheet("background-color: #2c313c;")
        self.leftMenuBtnUnclicked(self.view.ui.tracingBtn)
        self.leftMenuBtnUnclicked(self.view.ui.conversionBtn)



        if self.model.matchingLayout8 is None and self.model.matchingLayout6 is None:
            
            self.view.ui.verticalLayout_6.addWidget(self.view.ui.frame_4)
            self.view.ui.frame_4.show()
            self.view.ui.verticalLayout_6.addWidget(self.view.matchRibbon)
            self.view.ui.verticalLayout_8.addWidget(self.view.matchBanner, alignment=Qt.Alignment(QtCore.Qt.AlignTop))
            self.view.ui.verticalLayout_8.addWidget(self.view.ui.matchTable)
            self.view.ui.matchTable.show()
            pass 
        else:
            self.addWidgetsBackToLayout(self.view.ui.verticalLayout_8, self.model.matchingLayout8)
            self.addWidgetsBackToLayout(self.view.ui.verticalLayout_6, self.model.matchingLayout6)
            
    def conversionBtnClicked(self):
        # Conversion not currently included in TraceIt. Window is empty
        if self.model.uiView == 'Conversion':
            return
        elif self.model.uiView == 'Tracing':
            self.model.tracingLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.tracingLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)
        elif self.model.uiView == 'Matching':
            self.model.matchingLayout8 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_8)
            self.model.matchingLayout6 = self.removeWidgetsFromLayout(self.view.ui.verticalLayout_6)

        
        self.model.uiView = 'Conversion'
        self.view.ui.conversionBtn.setStyleSheet("background-color: #2c313c;")
        self.leftMenuBtnUnclicked(self.view.ui.tracingBtn)
        self.leftMenuBtnUnclicked(self.view.ui.matchingBtn)



        if self.model.conversionLayout8 is None and self.model.conversionLayout6 is None:
            pass 
        else:
            self.addWidgetsBackToLayout(self.view.ui.verticalLayout_8, self.model.conversionLayout8)
            self.addWidgetsBackToLayout(self.view.ui.verticalLayout_6, self.model.conversionLayout6)

    def leftMenuBtnUnclicked(self, btn):
        btn.setStyleSheet(u"\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #2c313c    ; /* replace with your desired color */\n"
                                    "}")

    def removeWidgetsFromLayout(self, layout):
        # Remove widgets from a layout and hide them. Used for window switching
        items = []
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            widget.hide()  # Hide the widget
            items.append(item)
        return items
    
    def addWidgetsBackToLayout(self, layout, items):
        # Adding widgets back to layout. Used for window switching
        for item in items:
            layout.addItem(item)
            widget = item.widget()
            widget.show()  
    #endregion 

    #region Tracing Mechanics 
    def updateMethodology(self, methodology):
        # Update methodology based on user button click
        if methodology == 'FIFO':
            self.model.methodology = 'FIFO'
            self.updateMethodologyLabel('First-In, First-Out')
        elif methodology == 'LIFO':
            self.model.methodology = 'LIFO'
            self.updateMethodologyLabel('Last-In, First-Out')
        elif methodology == 'LIBRR':
            self.model.methodology = 'LIBRR'
            self.updateMethodologyLabel('Lowest Intermediate Balance Rule (R)')
        elif methodology == 'LIBRNR':
            self.model.methodology = 'LIBRNR'
            self.updateMethodologyLabel('Lowest Intermediate Balance Rule (NR)')
        else:
            self.model.methodology = 'PC'
            self.updateMethodologyLabel('Poisoned Chalice')

    def runTracingButton(self):
        # Map tracing methodology to user selection
        if self.model.methodology == 'LIFO':
            self.findAllPossibleDebits = self.findAllPossibleDebitsLIFO
        elif self.model.methodology == 'FIFO':
            self.findAllPossibleDebits = self.findAllPossibleDebitsFIFO
        elif self.model.methodology == 'LIBRNR':
            self.findAllPossibleDebits = self.findAllPossibleDebitsLIBRNR
        elif self.model.methodology == 'PC':
            self.findAllPossibleDebits = self.findAllPossibleDebitsPoisonedChalice
        else:
            return

        
        self.generateTransactionObjects()
        self.clearStartingtransactionsComboBox()
        self.submitStartingTransactions()
        self.clearJSON('config/tree.json')
        self.clearTraceTable()

        # Loop through starting transactions till theres none left
        if len(self.model.startingTransactions):
            self.initialiseTracingModel()
            self.run_tracing()
        else:
            pass

        # Calculate the Application of funds to be used for the lollipop chart
        self.calculateApplications()
        # Export lollipop chart data to json for the current viewing transactions
        self.exportApplicationsToJSON(self.model.currentViewingTransaction)
        # Update the label in the trace banner
        self.updateEndPointsAmountLabel("${:,.2f} to End Points".format(self.getEndPointAmounts()))
        # Initial update is completed, now switch this to true to update on any combobox change
        self.model.endPointUpdateSwitch = True

    def initialiseTracingModel(self):
        print(f'Running tracing for transaction: {self.model.startingTransactions[0]} with methodology {self.model.methodology}')
        self.model.startingTransaction = next(t for t in self.model.transactions if t.refID == self.model.startingTransactions[0])
        self.model.startingTransaction.taintedBalance = [self.model.startingTransaction.credit]
        self.model.rootNode = Node(name=self.model.startingTransaction.refID 
                                    ,level=0
                                    ,id=self.model.startingTransaction.refID
                                    ,taintedFundsUsed = self.model.startingTransaction.taintedBalance[-1]
                                    ,amount = self.model.startingTransaction.credit
                                    ,account = self.model.startingTransaction.account
                                    ,date = self.model.startingTransaction.date
                                    ,accountName = self.model.startingTransaction.name
                                    ,category='' )
        

        self.model.counter = 0
        self.model.current_level = 0
        self.model.traceQueue = [[self.model.startingTransaction, self.model.current_level]]
        self.model.nodes = [self.model.rootNode]  
        self.model.traceTransactionData[self.model.startingTransactions[0]] = []
        if self.model.methodology == 'PC':
            self.model.startingTransaction.taintedBalance = [self.model.startingTransaction.balance]
        
    def findAllPossibleDebitsLIFO(self, transaction, level):
        priority_balance = 0
        self.writeTransactionDetailsToTrace(transaction, transaction,priority_balance, level)
        possible_debits = []
        next_transactions = [t for t in self.model.transactions if t.refID >  transaction.refID and t.account == transaction.account]
        next_transactions.sort(key=lambda x: x.refID, reverse=False) 
        for i in range(len(next_transactions)):
            next_transactions[i].taintedFundsUsed = None
            if transaction.taintedBalance[0] <= 0:
                break
            elif next_transactions[i].credit > 0:
                priority_balance += next_transactions[i].credit
                self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
            elif next_transactions[i].debit > 0:
                if priority_balance >= next_transactions[i].debit:
                    priority_balance -= next_transactions[i].debit
                    self.writeTransactionDetailsToTrace(next_transactions[i], transaction, priority_balance, level)
                elif priority_balance < next_transactions[i].debit:
                    #next_transactions[i].effectiveDebit -= priority_balance
                    subtract_pb = copy.deepcopy(priority_balance)
                    priority_balance = 0
                    if next_transactions[i].debit - subtract_pb <= transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        subtact_tb = copy.deepcopy(transaction.taintedBalance[0])
                        transaction.taintedBalance[0] -= min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        next_transactions[i].taintedFundsUsed = min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed
                    else:
                    #elif next_transactions[i].effectiveDebit > transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        next_transactions[i].taintedFundsUsed = min(copy.deepcopy(transaction.taintedBalance[0]), next_transactions[i].effectiveDebit)
                        transaction.taintedBalance[0] -= next_transactions[i].taintedFundsUsed
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed  
        self.model.traceQueue.pop(0) 

        return possible_debits, transaction, len(next_transactions)
    
    def findAllPossibleDebitsFIFO(self, transaction, level):
        priority_balance = transaction.balance - transaction.credit
        self.writeTransactionDetailsToTrace(transaction, transaction,priority_balance, level)
        possible_debits = []
        next_transactions = [t for t in self.model.transactions if t.refID >  transaction.refID and t.account == transaction.account]
        next_transactions.sort(key=lambda x: x.refID, reverse=False) 
        for i in range(len(next_transactions)):
            next_transactions[i].taintedFundsUsed = None
            if transaction.taintedBalance[0] <= 0:
                break
            elif next_transactions[i].credit > 0:
                self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
            elif next_transactions[i].debit > 0:
                if priority_balance >= next_transactions[i].debit:
                    priority_balance -= next_transactions[i].debit
                    self.writeTransactionDetailsToTrace(next_transactions[i], transaction, priority_balance, level)
                elif priority_balance < next_transactions[i].debit:
                    #next_transactions[i].effectiveDebit -= priority_balance
                    subtract_pb = copy.deepcopy(priority_balance)
                    priority_balance = 0
                    if next_transactions[i].debit - subtract_pb <= transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        subtact_tb = copy.deepcopy(transaction.taintedBalance[0])
                        transaction.taintedBalance[0] -= min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        next_transactions[i].taintedFundsUsed = min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed
                    else:
                    #elif next_transactions[i].effectiveDebit > transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        next_transactions[i].taintedFundsUsed = min(copy.deepcopy(transaction.taintedBalance[0]), next_transactions[i].effectiveDebit)
                        transaction.taintedBalance[0] -= next_transactions[i].taintedFundsUsed
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed  
        self.model.traceQueue.pop(0) 

        return possible_debits, transaction, len(next_transactions)

    def findAllPossibleDebitsLIBRNR(self, transaction, level):
        priority_balance = transaction.balance - transaction.credit
        self.writeTransactionDetailsToTrace(transaction, transaction,priority_balance, level)
        possible_debits = []
        next_transactions = [t for t in self.model.transactions if t.refID >  transaction.refID and t.account == transaction.account]
        next_transactions.sort(key=lambda x: x.refID, reverse=False) 
        for i in range(len(next_transactions)):
            next_transactions[i].taintedFundsUsed = None
            if transaction.taintedBalance[0] <= 0:
                break
            elif next_transactions[i].credit > 0:
                priority_balance += next_transactions[i].credit
                self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
            elif next_transactions[i].debit > 0:
                if priority_balance >= next_transactions[i].debit:
                    priority_balance -= next_transactions[i].debit
                    self.writeTransactionDetailsToTrace(next_transactions[i], transaction, priority_balance, level)
                elif priority_balance < next_transactions[i].debit:
                    #next_transactions[i].effectiveDebit -= priority_balance
                    subtract_pb = copy.deepcopy(priority_balance)
                    priority_balance = 0
                    if next_transactions[i].debit - subtract_pb <= transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        subtact_tb = copy.deepcopy(transaction.taintedBalance[0])
                        transaction.taintedBalance[0] -= min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        next_transactions[i].taintedFundsUsed = min((next_transactions[i].debit - subtract_pb), next_transactions[i].effectiveDebit)
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed
                    else:
                    #elif next_transactions[i].effectiveDebit > transaction.taintedBalance[0]:
                        if next_transactions[i].effectiveDebit > 0:
                            possible_debits.append(next_transactions[i])
                        next_transactions[i].taintedFundsUsed = min(copy.deepcopy(transaction.taintedBalance[0]), next_transactions[i].effectiveDebit)
                        transaction.taintedBalance[0] -= next_transactions[i].taintedFundsUsed
                        self.writeTransactionDetailsToTrace( next_transactions[i], transaction, priority_balance, level)
                        next_transactions[i].effectiveDebit -= next_transactions[i].taintedFundsUsed  
        self.model.traceQueue.pop(0) 

        return possible_debits, transaction, len(next_transactions)

    def findAllPossibleDebitsPoisonedChalice(self, transaction, level):
        self.writeTransactionDetailsToTracePoisonedChalice( transaction, transaction, level)
        possible_debits = []
        next_trans = [t for t in self.model.transactions if  t.refID >  transaction.refID  and t.account == transaction.account]
        next_trans.sort(key=lambda x: x.refID, reverse=False)
        for i in range(len(next_trans)):
            if next_trans[i].credit > 0:
                self.writeTransactionDetailsToTracePoisonedChalice(next_trans[i], transaction, level)
            else:
                next_trans[i].taintedFundsUsed = None
                if transaction.taintedBalance[0] <= 0:
                    break
                else:
                    next_trans[i].taintedFundsUsed = next_trans[i].debit
                    transaction.taintedBalance[0] = max(transaction.taintedBalance[0] - next_trans[i].debit, 0)
                    self.writeTransactionDetailsToTracePoisonedChalice(next_trans[i], transaction, level)
                    if next_trans[i].previouslyTraced == False:
                        possible_debits.append(next_trans[i])

        self.model.traceQueue.pop(0)
        return possible_debits, transaction, len(next_trans)

    def build_children_nodes(self, parent, debits):
        
        for debit in debits:
            if debit.taintedFundsUsed == debit.effectiveDebit:
                debit.previouslyTraced = True
            if debit.matchedTransaction is not None:
                match = debit.matchedTransaction

                if self.model.methodology == 'PC':
                    match.taintedBalance.append(match.balance)
                else:
                    match.taintedBalance.append(debit.taintedFundsUsed)




                # Each matching credit will also need to be traced so we add it to the trace queue
                self.model.traceQueue.append([match, parent.level +1])
                
                

                # Creating the child node - note parent=parent (parent is an argument of the function)
                node = Node(name=match.refID, parent=parent,level=parent.level+1, id=match.refID
                                                                                ,parent_id = parent.id
                                                                                ,taintedFundsUsed = match.taintedBalance[-1]
                                                                                ,amount = match.credit
                                                                                ,date = match.date
                                                                                ,account = match.account
                                                                                ,accountName = match.name
                                                                                ,category='')
                self.model.nodes.append(node)

            else:
              
                node = Node(name=debit.refID,parent=parent,level=parent.level+1, id=debit.refID
                                                                                ,parent_id = parent.id
                                                                                ,taintedFundsUsed = debit.taintedFundsUsed
                                                                                ,date = debit.date
                                                                                ,amount=debit.debit
                                                                                ,accountName = debit.name
                                                                                ,account=debit.category
                                                                                ,category=debit.category)
                #self.model.nodes.append(node)
        self.model.counter += 1

            # NO MATCH    
            
    def run_tracing(self):
        while len(self.model.traceQueue) > 0:
            debits, transaction, length = self.findAllPossibleDebits(self.model.traceQueue[0][0], self.model.traceQueue[0][1])
            self.build_children_nodes(self.model.nodes[self.model.counter], debits)
            transaction.taintedBalance.pop(0)

            # When the length of the trace queue becomes 0 - we move to the next starting transaction and start all over again. 
            if len(self.model.traceQueue) == 0:

                # Pop the first index of the starting transactions list to move to the next element. 
                self.model.tracePaths[self.model.startingTransactions[0]] = self.node_to_dict(self.model.rootNode)
                self.view.traceRibbonUI.startingTransactionsComboBox.addItem(self.model.startingTransactions[0])
                self.model.startingTransactions.pop(0)

                # If there are still more elements in the starting transactions list - we will continue tracing. Otherwise the program will end
                if len(self.model.startingTransactions) > 0:

                    self.initialiseTracingModel()

    def writeTransactionDetailsToTrace(self, t, credit, pb, level):
        # Function to write 1 transaction to the trace csv
        row = [
                            self.model.startingTransactions[0]
                            ,credit.refID
                            ,level
                            ,t.refID
                            ,t.refID
                            ,t.date
                            ,t.narrative
                            ,round(t.debit,2)
                            ,copy.deepcopy(round(t.effectiveDebit,2))
                            ,round(t.credit,2)
                            ,round(t.balance, 2)
                            ,t.matchedTransaction.refID if t.matchedTransaction is not None else ''
                            ,t.category if t.matchedTransaction is None and t.debit > 0 else ''
                            ,copy.deepcopy(round(credit.taintedBalance[0],2))
                            ,round(pb, 2)
                            ,round(t.taintedFundsUsed,2) if t.taintedFundsUsed is not None and t.taintedFundsUsed >0 and t.debit > 0 else ''
                            ,credit.matchedTransaction.refID if credit.matchedTransaction is not None else 'N/A'
                            ]
        self.model.traceTransactionData[self.model.startingTransactions[0]].append(row)
        
    def writeTransactionDetailsToTracePoisonedChalice(self, t, credit, level):
        # Function to write 1 transaction to the trace csv
        self.model.traceTransactionData[self.model.startingTransactions[0]].append([
                            self.model.startingTransactions[0]
                            ,credit.refID
                            ,level
                            ,t.refID
                            ,t.refID
                            ,t.date
                            ,t.narrative
                            ,round(t.debit,2)
                            ,round(t.credit,2)
                            ,round(t.balance, 2)
                            ,t.matchedTransaction.refID if t.matchedTransaction is not None else ''
                            ,t.category if t.matchedTransaction is None and t.debit > 0 else ''
                            ,t.previouslyTraced
                            ,copy.deepcopy(round(credit.taintedBalance[0],2))
                            ,credit.matchedTransaction.refID if credit.matchedTransaction is not None else 'N/A'
                            ])
    
    def node_to_dict(self, node):
        # Recursively convert node and its children to a dictionary
        node_dict = {"name": node.id, "category": node.category, "level":node.level, "account":node.account, "date":str(node.date), "amount":node.amount, "taintedAmount": node.taintedFundsUsed, "accountName":node.accountName}
        if node.children:
            node_dict["children"] = [self.node_to_dict(child) for child in node.children]
        return node_dict

    def exportTreeToJSON(self, transactionID, filename="config/tree.json"):
        with open(filename, "w") as json_file:
            json.dump({"config":self.model.graphConfig , "trace":self.model.tracePaths[transactionID]}, json_file, indent=4)

    def get_unique_categories(self, node):
        # Initialize a set to store unique category values
        unique_categories = set()
        
        # Recursive helper function to traverse the tree
        def traverse(node):
            # Add the category to the set if it exists and is not empty
            if 'category' in node and node['category']:
                unique_categories.add(node['category'])
            
            # If the node has children, recursively process each child
            if 'children' in node:
                for child in node['children']:
                    traverse(child)
        
        # Start the traversal from the root node
        traverse(node)
        
        # Return the unique categories as a list
        return list(unique_categories)

    def filter_categories(self, data, categories):
        def recursive_filter(node):
            if 'children' in node:
                node['children'] = [child for child in node['children'] if recursive_filter(child)]
                return len(node['children']) > 0
            else:
                return node['category'] in categories

        filtered_data = copy.deepcopy(data)
        recursive_filter(filtered_data)
        return  filtered_data
    
    def startingTransactionsComboBoxChanged(self, text):
        self.view.traceSearchBar.label.setText("")
        if bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', text)):
            self.model.currentViewingTransaction = text
            self.model.currentTraceLevelView = 0
            # EDIT MULIT COMBO BOX
            categories = sorted(self.get_unique_categories(self.model.tracePaths[text]))
            for _ in range(self.view.traceRibbonUI.combo.combo_box.model().rowCount()):
                self.view.traceRibbonUI.combo.combo_box.removeItem(0)
            self.view.traceRibbonUI.combo.combo_box.addItem("Select All", None, checked=True) 
            for category in categories:
                self.view.traceRibbonUI.combo.combo_box.addItem(category, checked=True)
            # UPDATE TRACE TABLE TABLE
            self.updateTraceTable(text, text, 0)
            startingCreditAmount = self.model.transactionsDF.loc[self.model.transactionsDF['Transaction ID'] == text, 'Credit'].values[0]
            self.updateStartingAmountLabel("${:,.2f} Credit".format(startingCreditAmount))
            if self.model.endPointUpdateSwitch == True:
                self.updateEndPointsAmountLabel("${:,.2f} to End Points".format(self.getEndPointAmounts()))
    
            # UPDATE TREE GRAPH    
            self.exportTreeToJSON(text)
            self.exportApplicationsToJSON(text)
            self.updateJSONNodeColour(self.model.currentViewingTransaction, self.model.currentTraceLevelView)

    def clearStartingtransactionsComboBox(self):
        self.view.traceRibbonUI.startingTransactionsComboBox.clear()

    def resetStartingTransactionsCombobox(self):
        self.view.traceRibbonUI.startingTransactionsComboBox.setCurrentIndex(-1)

    def generateTransactionObjects(self):
        self.model.transactions = []
        #Load Transactions
        for _, row in self.model.transactionsDF.iterrows():
            tran = self.parseRowToTransaction(row)
            self.model.transactions.append(tran)
        for t in self.model.transactions:
            if t.matchedTransactionID is not None:
                t.matchedTransaction = next(m for m in self.model.transactions if m.refID == t.matchedTransactionID)
            else:
                t.matchedTransaction = None

    def parseRowToTransaction(self,row):
        # This function will take 1 row of a dataframe and parse it into a transaction object
        tran = Transaction(row['Transaction ID'])
        tran.name = str(row['Name']).upper()
        tran.account = str(row['Account'])
        tran.date = str(row['Date']) 
        tran.narrative = row['Description']
        tran.debit = row['Debit']
        tran.effectiveDebit = row['Debit']
        tran.credit = row['Credit']
        tran.balance = row['Balance']
        if 'Matched Transaction' in row and bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', str(row['Matched Transaction']))): 
            tran.matchedTransactionID = str(row['Matched Transaction'])
        else:
            tran.matchedTransactionID = None
        if 'Category' in row and str(row['Category']) != 'nan':
            tran.category = str(row['Category'])
        else:
            tran.category = None
        return tran    
    #endregion
    
    #region Tree Graph and Trace Table
    def clearJSON(self, path):
        with open(path, 'w') as f:
            pass

    def clearTraceTable(self):
        self.view.ui.traceTable.setRowCount(0)
        self.view.ui.traceTable.setColumnCount(0)

    def updateTraceTable(self, startingTransactionID, transactionID, level):
        #table testing  
        if self.model.methodology in ['LIFO', 'FIFO', 'LIBRR', 'LIBRNR']:
            traceData = copy.deepcopy(self.model.traceTransactionData[startingTransactionID])
            tableRows = [[row[3] #Ref id 
                        ,row[5] # Date
                        ,row[6] # Descr
                        ,"${:,.2f}".format(row[7])  # Debit 
                        ,"${:,.2f}".format(row[8]) # Effective debit
                        ,"${:,.2f}".format(row[9])  #  Credit
                        ,"${:,.2f}".format(row[10])  # Balance 
                        ,row[11] # Match
                        ,row[12] # category
                        ,"${:,.2f}".format(row[13])  # tainted balance
                        ,"${:,.2f}".format(row[14])  #priority balance
                        ,row[15] if row[15] == '' else "${:,.2f}".format(row[15])] # Tainted funds used
                        for row in traceData if row[1] == transactionID and row[2] == int(level)]
            if len(tableRows) == 0:
                tableRows = [[row[3] #Ref id 
                        ,row[5] # Date
                        ,row[6] # Descr
                        ,"${:,.2f}".format(row[7])  # Debit 
                        ,"${:,.2f}".format(row[8]) # Effective debit
                        ,"${:,.2f}".format(row[9])  #  Credit
                        ,"${:,.2f}".format(row[10])  # Balance 
                        ,row[11] # Match
                        ,row[12] # category
                        ,"${:,.2f}".format(row[13])  # tainted balance
                        ,"${:,.2f}".format(row[14])  #priority balance
                        ,row[15] if row[15] == '' else "${:,.2f}".format(row[15])] # Tainted funds used
                        for row in traceData if row[3] == transactionID and row[2] == int(level)-1]
            self.view.ui.traceTable.setRowCount(len(tableRows))
            self.view.ui.traceTable.setColumnCount(12)

            # Set column Names
            header_labels = ["Transaction ID", "Date", "Description", "Debtit", "Effective Debit", "Credit", "Balance", "Matched Transaction", "Category", "Tainted Balance", "Priority Balance", "Tainted Used", ]
            self.view.ui.traceTable.setHorizontalHeaderLabels(header_labels)

            # Set column Widths 
            column_widths = [130, 90,340,90,90,90,100,140,100,100,100, 100] 
            for i, width in enumerate(column_widths):
                self.view.ui.traceTable.setColumnWidth(i, width)
            for row in range(len(tableRows)):
                for column in range(12):
                    item = QtWidgets.QTableWidgetItem(str(tableRows[row][column]))
                    if column in [1, 3,4,5,6,9,10,11]:  
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)  # Right-align the text
                    self.view.ui.traceTable.setItem(row, column, item)
            self.view.ui.traceTable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        else:
            traceData = copy.deepcopy(self.model.traceTransactionData[startingTransactionID])
            tableRows = [[row[3] #Ref id 
                        ,row[5] # Date
                        ,row[6] # Descr
                        ,"${:,.2f}".format(row[7])  # Debit 
                        ,"${:,.2f}".format(row[8]) # credit
                        ,"${:,.2f}".format(row[9])  #  balance
                        ,row[10] # Match
                        ,row[11] # category
                        ,row[12]  # previously traced
                        ,"${:,.2f}".format(row[13])  ] # tainted balance
                        for row in traceData if row[1] == transactionID and row[2] == int(level)]
            if len(tableRows) == 0:
                tableRows = [[row[3] #Ref id 
                        ,row[5] # Date
                        ,row[6] # Descr
                        ,"${:,.2f}".format(row[7])  # Debit 
                        ,"${:,.2f}".format(row[8]) # credit
                        ,"${:,.2f}".format(row[9])  #  balance
                        ,row[10] # Match
                        ,row[11] # category
                        ,row[12]  # previously traced
                        ,"${:,.2f}".format(row[13])  ] # tainted balance
                        for row in traceData if row[3] == transactionID and row[2] == int(level)-1]
            self.view.ui.traceTable.setRowCount(len(tableRows))
            self.view.ui.traceTable.setColumnCount(10)

            # Set column Names
            header_labels = ["Transaction ID", "Date", "Description", "Debtit", "Credit", "Balance", "Matched Transaction", "Category", "Previously Traced",  "Tainted Balance"]
            self.view.ui.traceTable.setHorizontalHeaderLabels(header_labels)

            # Set column Widths 
            column_widths = [150, 90,340,130,130,130,150,140,100,100]  # Example widths for each column
            for i, width in enumerate(column_widths):
                self.view.ui.traceTable.setColumnWidth(i, width)
            for row in range(len(tableRows)):
                for column in range(10):
                    item = QtWidgets.QTableWidgetItem(str(tableRows[row][column]))
                    if column in [1, 3,4,5,9]: 
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)  # Right-align the text
                    self.view.ui.traceTable.setItem(row, column, item)
            self.view.ui.traceTable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def returnJavaScriptConsoleLog(self, data):
        info = data[0].split(' ')
        if len(info) == 2:
            if bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', info[0])):
                self.model.clickedNode = info

    def reloadTreeHTML(self):
        self.view.treeWebView.reload()

    def onCellDbouleClicked(self, row, col):
        if self.model.methodology in ['LIFO', 'FIFO']:
            item = self.view.ui.traceTable.item(row, col)      
            if item:
                    if (len([row for row in self.model.traceTransactionData[self.model.currentViewingTransaction] if 
                            row[2] == self.model.currentTraceLevelView+1 
                            and row[1] == item.text()])) >0:
                        self.updateJSONNodeColour(item.text(), self.model.currentTraceLevelView+1)
                        self.updateTraceTable(self.model.currentViewingTransaction, item.text(), self.model.currentTraceLevelView+1)
                        self.model.currentTraceLevelView +=1


        elif self.model.methodology == 'PC':
            item = self.view.ui.traceTable.item(row, col)      
            if item:
                    if (len([row for row in self.model.traceTransactionData[self.model.currentViewingTransaction] if 
                            row[2] == self.model.currentTraceLevelView+1 
                            and row[1] == item.text()])) >0:
                        self.updateJSONNodeColour(item.text(), self.model.currentTraceLevelView+1)
                        self.updateTraceTable(self.model.currentViewingTransaction, item.text(), self.model.currentTraceLevelView+1)
                        self.model.currentTraceLevelView +=1

    def onEndPointItemChanged(self, item):
        if item.text() == "Select All":
            if item.checkState() == Qt.Checked:
                for i in range(1, self.view.traceRibbonUI.combo.combo_box.model().rowCount()):
                    self.view.traceRibbonUI.combo.combo_box.model().item(i).setCheckState(Qt.Checked)
            else:
                for i in range(1, self.view.traceRibbonUI.combo.combo_box.model().rowCount()):
                    self.view.traceRibbonUI.combo.combo_box.model().item(i).setCheckState(Qt.Unchecked)
        checked_items = [self.view.traceRibbonUI.combo.combo_box.model().item(i).text() for i in range(1, self.view.traceRibbonUI.combo.combo_box.model().rowCount()) if self.view.traceRibbonUI.combo.combo_box.model().item(i).checkState() == Qt.Checked]
        self.updateEndPointsAmountLabel("${:,.2f} to End Points".format(self.getEndPointAmounts()))
        filtered_data = self.filter_categories(self.model.tracePaths[self.model.currentViewingTransaction], checked_items)
        with open('config/tree.json', "w") as json_file:
            json.dump({"config":self.model.graphConfig , "trace":filtered_data}, json_file, indent=4)
        self.updateTraceTable(self.model.currentViewingTransaction, self.model.currentViewingTransaction, 0)
    
    def getEndPointAmounts(self):
        checked_items = [self.view.traceRibbonUI.combo.combo_box.model().item(i).text() for i in range(1, self.view.traceRibbonUI.combo.combo_box.model().rowCount()) if self.view.traceRibbonUI.combo.combo_box.model().item(i).checkState() == Qt.Checked]
        transactionApplications = self.model.applicationsDictionary[self.model.currentViewingTransaction]["data"]
        return sum([a["0"] for a in transactionApplications if a["name"] in checked_items])

    def clickedNodeChanged(self):
        clicked_node = self.model.clickedNode
        self.model.currentTraceLevelView = int(self.model.clickedNode[1])
        self.updateTraceTable(self.model.currentViewingTransaction, self.model.clickedNode[0], self.model.currentTraceLevelView)

    def updateJSONNodeColour(self, TransactionID, level):
        javascriptCode = """nodes = document.querySelectorAll('svg g g.node');
                                     nodes.forEach(node => {if (node.__data__.data.name === '"""
        javascriptCode += TransactionID
        javascriptCode += """' && node.__data__.depth === """
        javascriptCode += str(level)
        javascriptCode += """) {
                                    node.querySelectorAll('circle').forEach(circle => {
                                        circle.setAttribute('fill', 'yellow');
                                        });
                                    } else {
                                        node.querySelectorAll('circle')[0].setAttribute('fill', '#8cffff'); // outer circle
                                        node.querySelectorAll('circle')[1].setAttribute('fill', '#ebebeb'); // inner circle
                                    }
                                     });
                                    """
        self.view.treePage.runJavaScript(javascriptCode)

    def updatevSpacingConfig(self, value):
        self.model.graphConfig['vSpacing'] = value
        if self.model.currentViewingTransaction is not None:
            self.exportTreeToJSON(self.model.currentViewingTransaction)
       
    def updatehSpacingConfig(self, value):
        self.model.graphConfig['hSpacing'] = value
        if self.model.currentViewingTransaction is not None:
            self.exportTreeToJSON(self.model.currentViewingTransaction)

    def updatefontSizeConfig(self, value):
        self.model.graphConfig['fontSize'] = value

    def toggleTraceSearch(self):
        if self.model.displayTraceSearchBar == False:
            self.view.ui.verticalLayout_8.insertWidget(1, self.view.traceSearchBar)
            self.view.traceSearchBar.show()
            self.model.displayTraceSearchBar = True
        else:
            self.view.ui.verticalLayout_8.removeWidget(self.view.traceSearchBar)
            self.view.traceSearchBar.hide()
            self.model.displayTraceSearchBar = False

    def searchTrace(self):
        if self.model.currentViewingTransaction is not None:
            searchText = self.view.traceSearchBar.searchEdit.text()
            if bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', searchText)):
                results = [row for row in self.model.traceTransactionData[self.model.currentViewingTransaction] if row[3] == searchText]
                if len(results) > 0:
                    self.view.traceSearchBar.results = results
                    self.view.traceSearchBar.label.setText(f'{len(results)} matches found. Showing result {1} of {len(results)}')
                    self.updateJSONNodeColour(results[0][1], results[0][2])
                    self.updateTraceTable(self.model.currentViewingTransaction, results[0][1], results[0][2])
                    self.view.traceSearchBar.currentView = 0
                else:
                    self.view.traceSearchBar.results = None
                    self.view.traceSearchBar.label.setText('No matches found.')
                return
            else:
                return
            
    def traceTableRightClickMenu(self, position):
        selected_cells = self.view.ui.traceTable.selectedItems()
        if len(selected_cells) == 1 and selected_cells[0].column() == 7 and bool(re.match(r'^[a-zA-Z]{3}_[a-zA-Z]{3}_[0-9]{4}_[0-9]{6}$', selected_cells[0].text())):
            unmatchRefID = [item.text() for item in selected_cells][0]
            menu = QMenu()
            menu.addAction("Add to Unmatch list")
            # Execute the menu
            action = menu.exec_(self.view.ui.traceTable.mapToGlobal(position))
            # Handle the selected action
            if action:
                dfValues = self.model.transactionsDF[self.model.transactionsDF['Transaction ID']  == unmatchRefID]
                rows = dfValues.values.tolist()
                if rows[0][5] > 0:
                    debitID = rows[0][0]
                    creditID = rows[0][8]
                else:
                    debitID = rows[0][8]
                    creditID = rows[0][0]
                self.addDoubleLineEditRow(self.view.ui.verticalLayout_23, self.view.manualUnmatchLineEdits, debitID, creditID)
            self.submitManualUnmatch()

    def previousTraceSearchResult(self):
        if self.view.traceSearchBar.results == None or self.view.traceSearchBar.currentView == 0:
            return
        else:
            self.view.traceSearchBar.currentView -= 1
            self.updateJSONNodeColour(self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][1], self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][2])
            self.updateTraceTable(self.model.currentViewingTransaction, self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][1], self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][2])
            self.view.traceSearchBar.label.setText(f'{len(self.view.traceSearchBar.results)} matches found. Showing result {self.view.traceSearchBar.currentView + 1} of {len(self.view.traceSearchBar.results)}')

    def nextTraceSearchResult(self):
        if self.view.traceSearchBar.results == None or self.view.traceSearchBar.currentView == len(self.view.traceSearchBar.results) -1:
            return
        else:
            self.view.traceSearchBar.currentView += 1
            self.updateJSONNodeColour(self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][1], self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][2])
            self.updateTraceTable(self.model.currentViewingTransaction, self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][1], self.view.traceSearchBar.results[self.view.traceSearchBar.currentView][2])
            self.view.traceSearchBar.label.setText(f'{len(self.view.traceSearchBar.results)} matches found. Showing result {self.view.traceSearchBar.currentView + 1} of {len(self.view.traceSearchBar.results)}')
    
    def toggleTraceLabels(self):
        if self.model.treeNodeLabelsVisible == False:
            self.model.graphConfig['hSpacing'] = 120
            self.model.graphConfig['boxOpacity'] = 0.75
            self.model.graphConfig['labelOpacity'] = 1
            self.exportTreeToJSON(self.model.currentViewingTransaction)
            self.model.treeNodeLabelsVisible = True
        else:
            self.model.graphConfig['hSpacing'] = 60
            self.model.graphConfig['boxOpacity'] = 0
            self.model.graphConfig['labelOpacity'] = 0
            self.exportTreeToJSON(self.model.currentViewingTransaction)
            self.model.treeNodeLabelsVisible = False
        pass
    
    #endregion

    #region Lollipop Diagram
    def reloadLollipopHTML(self):
        self.view.lollipopWebView.reload()

    def visualiseApplications(self):
        if self.model.traceContentsView == 'Tree':
            for i in reversed(range(self.view.ui.verticalLayout_8.count())):  # Reverse loop to avoid index issues
                item = self.view.ui.verticalLayout_8.itemAt(i)
                widget = item.widget()
                if widget and widget != self.view.traceBanner:
                    self.view.ui.verticalLayout_8.removeWidget(widget)
                    widget.hide()
            self.reloadLollipopHTML()
            self.view.ui.verticalLayout_8.insertWidget(1,self.view.lollipopWebView)
            self.view.lollipopWebView.show()
            self.model.traceContentsView = 'Lollipop'
        else:
            for i in reversed(range(self.view.ui.verticalLayout_8.count())):  # Reverse loop to avoid index issues
                item = self.view.ui.verticalLayout_8.itemAt(i)
                widget = item.widget()
                if widget and widget != self.view.traceBanner:
                    self.view.ui.verticalLayout_8.removeWidget(widget)
                    widget.hide()
            self.view.ui.verticalLayout_8.insertWidget(1,self.view.splitter)
            self.view.splitter.show()
            self.model.traceContentsView = 'Tree'

    def calculateApplications(self):
        calculatedApplications = {}
        for key in self.model.tracePaths:
            categorySumAndCount = self.categorySumAndCount(self.model.tracePaths[key])
            aggregatedCategorySumAndCount = self.lollipopDataFormatter(categorySumAndCount)
            results, names = self.unifyAndSortKeys(aggregatedCategorySumAndCount)
            calculatedApplications[key] = {}
            calculatedApplications[key]['data'] = results
            calculatedApplications[key]['names'] = names
            calculatedApplications[key]['config'] = self.model.lollipopConfig 
            calculatedApplications[key]['colours'] = sample_distinct_colors(len(names))
        self.model.applicationsDictionary = calculatedApplications
        

    def categorySumAndCount(self, data):
        result = {}

        def recurse(node):
            if 'children' not in node:
                category = node.get('category', 'Unknown')
                account_name = node.get('accountName', 'Unknown')
                tainted_amount = node.get('taintedAmount', 0)

                if category not in result:
                    result[category] = {}
                if account_name not in result[category]:
                    result[category][account_name] = {'sum': 0, 'count': 0}

                result[category][account_name]['sum'] += tainted_amount
                result[category][account_name]['count'] += tainted_amount
            else:
                for child in node['children']:
                    recurse(child)

        recurse(data)
        return result

    def lollipopDataFormatter(self, data):
        listOfDicts = []
        for category, names in data.items():
            category_entry = {"category": category, "amount": 0}
            for name, values in names.items():
                category_entry["amount"] += values["sum"]
                category_entry[name] = values["count"]
            listOfDicts.append(category_entry)
        return listOfDicts

    def unifyAndSortKeys(self, dicts):
        all_keys = set()
        for d in dicts:
            all_keys.update(d.keys())

        # Remove 'category' and 'amount' as they should be handled separately
        all_keys.discard('category')
        all_keys.discard('amount')

        # Sort the remaining keys alphabetically
        sorted_keys = sorted(all_keys)

        # Step 2: Ensure each dictionary has all keys with missing ones set to 0
        new_dicts = []
        names_set = set()  # Use a set to store unique names

        for d in dicts:
            # Handle category replacement for null or empty values
            category = d.get('category')
            if category in [None, '', 'null', 'none']:
                category = 'No Category'
            
            # Create a new dictionary with all keys initialized to 0 and rename keys to '1', '2', etc.
            unified_dict = {str(i+1): d.get(key, 0) for i, key in enumerate(sorted_keys)}
            unified_dict['0'] = d['amount']
            unified_dict['name'] = category

            # Step 3: Order keys ensuring '0' (amount) comes first and 'name' (category) comes last
            ordered_dict = {'0': unified_dict.pop('0')}
            ordered_dict.update(unified_dict)
            ordered_dict['name'] = unified_dict.pop('name')

            new_dicts.append(ordered_dict)

            # Collect names corresponding to '1', '2', '3', ... up until but not including the last key
            names_set.update(sorted_keys)

        # Remove 'name' from names_set
        names_set.discard('name')

        # Convert names_set to a sorted list (optional: you can sort it alphabetically)
        names_list = sorted(names_set)

        # Step 4: Sort the list of dictionaries in descending order based on the '0' element
        new_dicts = sorted(new_dicts, key=lambda x: x['0'], reverse=True)

        # Return both new_dicts and names_list
        return new_dicts, names_list

    
    def exportApplicationsToJSON(self, startingTransactionID, filename="config/applications.json"):
        with open(filename, "w") as json_file:
            json.dump(self.model.applicationsDictionary[startingTransactionID], json_file, indent=4)
    #endregion

    #region Chord Diagram 
    def updateChordJSON(self):
        accountNameData = self.model.transactionsDF[self.model.transactionsDF['Matched Transaction'].notna()]
        accountAndName = accountNameData[['Account', 'Name']].drop_duplicates().sort_values(by=['Name', 'Account'])
        nameList = accountAndName['Name'].tolist()
        accountList = accountAndName['Account'].tolist()
        merged_df = self.model.transactionsDF.merge(self.model.transactionsDF, how='left', left_on='Matched Transaction', right_on='Transaction ID', suffixes=('', '_matched'))
        result_df = merged_df[['Transaction ID', 'Account', 'Debit', 'Matched Transaction', 'Account_matched']].rename(columns={'Account_matched': 'Matched Transaction Account'})
        grouped_sum = result_df.groupby(['Account', 'Matched Transaction Account'])['Debit'].sum()
        pivot_df = grouped_sum.unstack(fill_value=0)
        pivot_df = pivot_df[accountList]
        #pivot_df = pivot_df.reindex(index=accountList) COMMENTING OUT BECAUSE THE VISUAL LOOKS BETTER
        # PURELY VISUAL BUT SETTING DIAGONALS TO 0
        pivot_df.values[np.arange(26), np.arange(26)] = 0
        headers = pivot_df.columns.tolist()
        matrixData = pivot_df.values.tolist()
        self.clearJSON("config/chord.json")
        self.exportChordMatrixToJSON(matrixData, headers, nameList)

    def exportChordMatrixToJSON(self, matrixData, headers, names, filename="config/chord.json"):
        with open(filename, "w") as json_file:
            json.dump({"matrix":matrixData, "headers":headers, "names":names, "height":self.view.ui.mainContentsContainer.size().height(), "width":self.view.ui.mainContentsContainer.size().width()}, json_file, indent=4)

    def reloadChordHTML(self):
        self.view.chordWebView.reload()

    def visualiseFlowOfFunds(self):
        if self.model.matchContentsView == 'Table':
            for i in reversed(range(self.view.ui.verticalLayout_8.count())):  # Reverse loop to avoid index issues
                item = self.view.ui.verticalLayout_8.itemAt(i)
                widget = item.widget()
                if widget and widget != self.view.matchBanner:
                    self.view.ui.verticalLayout_8.removeWidget(widget)
                    widget.hide()
            self.view.ui.verticalLayout_8.insertWidget(1,self.view.chordWebView)
            self.view.chordWebView.show()
            self.model.matchContentsView = 'Chord'
        else:
            for i in reversed(range(self.view.ui.verticalLayout_8.count())):  # Reverse loop to avoid index issues
                item = self.view.ui.verticalLayout_8.itemAt(i)
                widget = item.widget()
                if widget and widget != self.view.matchBanner:
                    self.view.ui.verticalLayout_8.removeWidget(widget)
                    widget.hide()
            self.view.ui.verticalLayout_8.insertWidget(1,self.view.ui.matchTable)
            self.view.ui.matchTable.show()
            self.model.matchContentsView = 'Table'
    #endregion

    #region Match Window and Match Table
    def loadMatchesFromExcelBtn(self):
        root = Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Excel or CSV files", "*.xlsx *.csv")]
        )
        
        if file_path:
            self.model.transactionsFilePath = file_path
            selectedColumns = ['Transaction ID', 'Name', 'Account', "Date","Description","Debit","Credit","Balance"]
            self.model.transactionsDF = pd.read_csv(self.model.transactionsFilePath, usecols=selectedColumns)
            self.model.transactionsDF['Account'] = self.model.transactionsDF['Account'].astype(str)
            self.model.transactionsDF['Matched Transaction'] = None
            self.model.transactionsDF['Score'] = None 
            self.model.transactionsDF['Group'] = None
            self.updateMatchTable(self.model.transactionsDF)
            self.updateTransactionsLoadedLabel(len(self.model.transactionsDF))
            self.updateTransactionCountLabel(len(self.model.transactionsDF))

    def openMatchesFileDialog(self):
        root = Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Excel or CSV files", "*.xlsx *.csv")]
        )
        
        if file_path:
            progress_dialog = QProgressDialog("Processing...", "Cancel", 0, 100)
            progress_dialog.show()
            self.model.matchesFilePath = file_path
            runnable = MyRunnable(self.generateTransactionsListCSV, file_path)
            QThreadPool.globalInstance().start(runnable)

    def matchTransactionsBtn(self) :
        self.view.ui.matchTable.sortByColumn(-1, QtCore.Qt.AscendingOrder)
        manualUnmatchDF = pd.DataFrame(self.model.manualUnmatch, columns=['Debit ID', 'Credit ID'])
        self.model.stampManualUnmatch = manualUnmatchDF
        manualMatchesDF = pd.DataFrame(self.model.manualMatches, columns=['Transaction ID_a','Transaction ID_b'])
        self.model.stampManualMatches = manualMatchesDF
        manualMatchesDF['Debit_Score'] = 100
        refTableDF = pd.DataFrame(self.model.refTable, columns=['Name','Search Term'])
        self.model.stampRefTable = refTableDF
        searchToName = dict(zip(refTableDF['Search Term'], refTableDF['Name']))
        searchToName = {key.lower(): value for key, value in searchToName.items()}
        refTableSearchTerms = '|'.join(refTableDF['Search Term'])
        refTablePattern = re.compile(refTableSearchTerms, re.IGNORECASE)
        def checkNameInIdentifiedNames(row, score):
            nameA = row['Name_a'].lower()
            nameB = row['Name_b'].lower()
            identifiedA = [identified.lower() for identified in row['Identified Names_a']]
            identifiedB = [identified.lower() for identified in row['Identified Names_b']]
            if nameA in identifiedB and nameB in identifiedA:
                return 2*score
            elif nameA in identifiedB or nameB in identifiedA:
                return score
            else:
                return 0

        #region Variable extraction
        minScore = float(self.view.matchRibbonUI.minThresholdLineEdit.text()) if isNumber(self.view.matchRibbonUI.minThresholdLineEdit.text()) else 0
        narrativeSimilarityWeight = float(self.view.matchRibbonUI.narrativeSimilarityLineEdit.text()) if isNumber(self.view.matchRibbonUI.narrativeSimilarityLineEdit.text()) else 1
        matchedWordsWeight = float(self.view.matchRibbonUI.matchedWordLineEdit.text()) if isNumber(self.view.matchRibbonUI.matchedWordLineEdit.text()) else 0.33
        matchedNumbersWeight =  float(self.view.matchRibbonUI.matchedNumberLineEdit.text()) if isNumber( self.view.matchRibbonUI.matchedNumberLineEdit.text()) else 1
        accountweight = float(self.view.matchRibbonUI.accountNumberMatchLineEdit.text()) if isNumber(self.view.matchRibbonUI.accountNumberMatchLineEdit.text()) else 3
        account4DigitsWeight = float(self.view.matchRibbonUI.accountNumber4DigitsMatchFrameLineEdit.text()) if isNumber(self.view.matchRibbonUI.accountNumber4DigitsMatchFrameLineEdit.text()) else 2
        minAmount = float(self.view.matchRibbonUI.minAmountLineEdit.text()) if isNumber(self.view.matchRibbonUI.minAmountLineEdit.text()) else 0 
        nonRoundScore = float(self.view.matchRibbonUI.nonRoundedAmountLineEdit.text()) if isNumber(self.view.matchRibbonUI.nonRoundedAmountLineEdit.text()) else 1
        keyWordScore = float(self.view.matchRibbonUI.keywordMatchLineEdit.text()) if isNumber(self.view.matchRibbonUI.keywordMatchLineEdit.text()) else  1
        #endregion
        queryDF = copy.deepcopy(self.model.transactionsDF)
        if 'Category' in queryDF.columns:
            queryDF = queryDF[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance', 'Category']]
        else:
            queryDF = queryDF[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance']]

        #region Score Possible Matches
        debits = queryDF[queryDF['Debit'] > minAmount]
        credits = queryDF[queryDF['Credit'] > minAmount]

        # Convert date column to datetime
        debits['Date'] = pd.to_datetime(debits['Date'], format='%d/%m/%Y')
        credits['Date'] = pd.to_datetime(credits['Date'], format='%d/%m/%Y')


        
        # Add a column with the number of days to add to the date
        debits['days_to_add'] = debits['Date'].apply(getDaysToAdd)

        # Merge debits and credits DataFrames
        mergedDF = pd.merge(debits, credits, left_on='Debit', right_on='Credit', suffixes=('_a', '_b'))

        # Filter rows based on conditions
        filteredDF = mergedDF[
            (mergedDF['Date_b'] >= mergedDF['Date_a']) &
            (mergedDF['Date_b'] <= mergedDF['Date_a'] + pd.to_timedelta(mergedDF['days_to_add'], unit='days')) &
            (mergedDF['Account_a'] != mergedDF['Account_b'])
        ]

        
        resultDF = filteredDF.sort_values(by='Transaction ID_a')


        resultDF['Narrative Similarity'] = resultDF.apply(lambda row: narrativeSimilarityScore(str(row['Description_a']), str(row['Description_b'])), axis=1)*narrativeSimilarityWeight
        resultDF['Matched Words Score'] = resultDF.apply(lambda row: matchedWordsScore(str(row['Description_a']), str(row['Description_b']), matchedWordsWeight), axis=1)
        resultDF['Matched Numbers Score'] = resultDF.apply(lambda row: matchedNumbersScore(str(row['Description_a']), str(row['Description_b']), matchedNumbersWeight), axis=1)
        resultDF['Account Number Score'] = resultDF.apply(lambda row: accountNumberScore(str(row['Description_a']), str(row['Account_a']), str(row['Description_b']) , str(row['Account_b']), accountweight, account4DigitsWeight), axis=1)
        resultDF['Non Rounded Score'] = resultDF.apply(lambda row: nonRoundScore if row['Debit_a'] % 10 != 0 else 0, axis=1)
        if self.model.refTable is not None:
            resultDF['Search Terms_a'] = resultDF['Description_a'].str.findall(refTablePattern)
            resultDF['Identified Names_a'] = resultDF['Search Terms_a'].apply(lambda terms: list({searchToName[term.lower()] for term in terms}) if isinstance(terms, list) else [])
            resultDF['Search Terms_b'] = resultDF['Description_b'].str.findall(refTablePattern)
            resultDF['Identified Names_b'] = resultDF['Search Terms_b'].apply(lambda terms: list({searchToName[term.lower()] for term in terms}) if isinstance(terms, list) else [])
            resultDF['Ref Table Score'] = resultDF.apply(checkNameInIdentifiedNames, axis=1, args=(keyWordScore,))
        else:
            resultDF['Ref Table Score'] = 0
        resultDF['Score'] = resultDF.apply(lambda row: round(row['Narrative Similarity'] + row['Matched Words Score'] + row['Matched Numbers Score']+ row['Account Number Score']+ row['Non Rounded Score'] + row['Ref Table Score'],2), axis=1)
        self.model.stampPossibleMatches = copy.deepcopy(resultDF)
        resultDF = resultDF[resultDF['Score'] > minScore]
        #endregion


        #region Select Matches
        while True:
            # Find the highest score for each debit
            
            highest_debit_scores = resultDF.loc[resultDF.groupby('Transaction ID_a')['Score'].idxmax()].reset_index(drop=True)
            highest_debit_scores = highest_debit_scores[['Transaction ID_a', 'Transaction ID_b', 'Score']]
            highest_debit_scores.rename(columns={'Transaction ID_b': 'Credit_High', 'Score': 'Debit_Score'}, inplace=True)

            # Find the highest score for each credit
            highest_credit_scores = resultDF.loc[resultDF.groupby('Transaction ID_b')['Score'].idxmax()].reset_index(drop=True)
            highest_credit_scores = highest_credit_scores[['Transaction ID_b', 'Transaction ID_a', 'Score']]
            highest_credit_scores.rename(columns={'Transaction ID_a': 'Debit_High', 'Score': 'Credit_Score'}, inplace = True)

            # Merge on both Debit and Credit to find mutual highest scores
            merged = pd.merge(highest_debit_scores, highest_credit_scores, left_on=['Transaction ID_a', 'Credit_High'], right_on=['Debit_High', 'Transaction ID_b'])

            # Filter where Debit_Score == Credit_Score
            result = merged[merged['Debit_Score'] == merged['Credit_Score']]
            
            if result.empty:
                break

            # Select relevant columns
            result = result[['Transaction ID_a', 'Transaction ID_b', 'Debit_Score']]

            # Drop matched rows from the original DataFrame
            resultDF = resultDF[~(resultDF['Transaction ID_a'].isin(result['Transaction ID_a']))].reset_index(drop=True)
            resultDF = resultDF[~(resultDF['Transaction ID_b'].isin(result['Transaction ID_b']))].reset_index(drop=True)
            # Append results
            if 'selectedMatches' in locals():
                selectedMatches = pd.concat([selectedMatches, result])
            else:
                selectedMatches = result
            




        unmatchedSelectedMatchesJoin = selectedMatches.merge(manualUnmatchDF
                                  ,left_on=['Transaction ID_a', 'Transaction ID_b']
                                  ,right_on=['Debit ID', 'Credit ID']
                                  ,how='left')
        
        postUnmatch = unmatchedSelectedMatchesJoin[unmatchedSelectedMatchesJoin['Debit ID'].isna()]
        postUnmatch = postUnmatch[['Transaction ID_a','Transaction ID_b','Debit_Score']]
        
        manualMatchAddition = pd.concat([postUnmatch,manualMatchesDF])

        
        manualMatchAddition = manualMatchAddition.sort_values('Debit_Score', ascending=False)
        matches = manualMatchAddition.drop_duplicates('Transaction ID_a', keep='first')
        matches = matches.drop_duplicates('Transaction ID_b', keep='first')

        matches['Group'] = range(1, len(matches) + 1)
        matches['Group'] = matches['Group'].apply(lambda x: f'{x:04d}')
        

        #endregion

        #region Update self.model.transactionsDF based on FINAL_RESULT
        matchJoin1 = queryDF.merge(matches, 
                                                    left_on='Transaction ID', 
                                                    right_on='Transaction ID_a', 
                                                    how='left')
        matchJoin1['Matched Transaction1'] = matchJoin1['Transaction ID_b']
        matchJoin1['Score1'] = matchJoin1['Debit_Score']
        if 'Category' in matchJoin1.columns:
            matchJoin1 = matchJoin1[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance', 'Matched Transaction1', 'Score1', 'Group', 'Category']]
        else:
            matchJoin1 = matchJoin1[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance', 'Matched Transaction1', 'Score1', 'Group']]
        

        matchJoin2 = matchJoin1.merge(matches, 
                                                    left_on='Transaction ID', 
                                                    right_on='Transaction ID_b', 
                                                    how='left')
        matchJoin2['Matched Transaction2'] = matchJoin2['Transaction ID_a']
        matchJoin2['Score2'] = matchJoin2['Debit_Score']

        matchJoin2['Matched Transaction'] = matchJoin2['Matched Transaction1'].combine_first(matchJoin2['Matched Transaction2'])
        matchJoin2['Score'] = matchJoin2['Score1'].combine_first(matchJoin2['Score2'])
        matchJoin2['Group'] = matchJoin2['Group_x'].combine_first(matchJoin2['Group_y'])
        
        if 'Category' in self.model.transactionsDF.columns:
            self.model.transactionsDF = matchJoin2[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance', 'Matched Transaction', 'Score', 'Group', 'Category']]
        else:
            self.model.transactionsDF = matchJoin2[['Transaction ID', 'Name', 'Account', 'Date', 'Description', 'Debit', 'Credit', 'Balance', 'Matched Transaction', 'Score', 'Group']]

        #endregion

        self.updateMatchTable(self.model.transactionsDF)
        self.updateMatchedTransactionsCountLabel(len(set(self.model.transactionsDF['Matched Transaction'].values.tolist()))-1)
        self.updateMatchedTransactionCountLabel(len(set(self.model.transactionsDF['Matched Transaction'].values.tolist()))-1)
        self.updateChordJSON()

    def updateMatchTable(self, df):
        self.view.ui.matchTable.updateCategoryChanges = False
        matchTableData = df.values.tolist()
        self.view.ui.matchTable.setRowCount(len(matchTableData))
        self.view.ui.matchTable.setColumnCount(12)
        header_labels = ["Transaction ID", "Name", "Account",  "Date", "Description", "Debtit",  "Credit", "Balance", "Matched Transaction", "Score", "Group" , "Category"]
        self.view.ui.matchTable.setHorizontalHeaderLabels(header_labels)
        scale = (self.view.ui.mainContentsContainer.size().width()-40)/31.8 
        columnWeights = [3,   2.6, 2, 2,  7.6 , 2 , 2, 2.6, 3 ,1 ,2,2] # 31.8 units
        column_widths = [x*scale for x in columnWeights]
        for i, width in enumerate(column_widths):
            self.view.ui.matchTable.setColumnWidth(i, width)
        if self.view.ui.mainContentsContainer.size().width() < 1200:
            fontSize = 8
        else:
            fontSize = 9
        font = self.view.ui.matchTable.font()
        font.setPointSize(fontSize)
        font = self.view.ui.matchTable.setFont(font)
        for row in range(len(matchTableData)):
            for column in range(12):
                if column >= len(matchTableData[0]):
                    item = QtWidgets.QTableWidgetItem('')
                else:
                    data = matchTableData[row][column]
                    if data is None or str(data) == 'nan':
                        item = QtWidgets.QTableWidgetItem('')
                        item.setData(QtCore.Qt.DisplayRole, '\x7f') 
                    else:
                        item = QtWidgets.QTableWidgetItem()
                        item.setData(QtCore.Qt.DisplayRole, data)
                        if isinstance(data, (int, float)):
                            item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter) 
                            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                if column == 3:
                    item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter) 
                self.view.ui.matchTable.setItem(row, column, item)
        self.view.ui.matchTable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.view.ui.matchTable.updateCategoryChanges = True
        return
        
    def categoriseTransactionsBtn(self):
        self.view.ui.matchTable.sortByColumn(-1, QtCore.Qt.AscendingOrder)
        categoriesDF = pd.DataFrame(self.model.categories, columns=['Category','Search Term'])
        self.model.stampCategories = categoriesDF
        categoriesDF = categoriesDF.drop_duplicates('Search Term')
        if 'Category' in self.model.transactionsDF.columns:
            self.model.transactionsDF = self.model.transactionsDF.drop(columns=['Category'])

        search_terms = '|'.join(categoriesDF['Search Term'])
        self.model.transactionsDF['Search Term'] = self.model.transactionsDF['Description'].str.extract(f'({search_terms})', expand=False)
        self.model.transactionsDF = self.model.transactionsDF.merge(categoriesDF, on='Search Term', how='left')
        self.model.transactionsDF = self.model.transactionsDF.drop(columns=['Search Term'])
        self.updateMatchTable(self.model.transactionsDF)
        self.updateTransactionsCategorisedCountLabel(len([ t for t in self.model.transactionsDF['Category'].values.tolist() if str(t) != 'nan']))
        
        return

    def matchTableRightClickMenu(self, position):
        # Get the cell's row and column under the cursor
        selected_cells = self.view.ui.matchTable.selectedItems()
        if len(selected_cells) == 1 and selected_cells[0].column() == 11:
            menu = QMenu()
            menu.addAction("Copy Category")
            action = menu.exec_(self.view.ui.matchTable.mapToGlobal(position))
            if action:
                self.model.copiedCategory = selected_cells[0].text()
        elif len(selected_cells) > 1 and set([cell.column() for cell in selected_cells]) == {11}:
            menu = QMenu()
            menu.addAction("Paste Category")
            action = menu.exec_(self.view.ui.matchTable.mapToGlobal(position))
            if action:
                for cell in selected_cells:
                    cell.setText(self.model.copiedCategory)
        else:
            validItems = [(item.column(), item.text()) for item in selected_cells if item.column() == 10]
            uniqueGroupsSelected = set(validItems)
            if uniqueGroupsSelected:
                menu = QMenu()
                menu.addAction("Add to Unmatch list")
                # Execute the menu
                action = menu.exec_(self.view.ui.matchTable.mapToGlobal(position))
                # Handle the selected action
                if action:
                    for groupSelected in uniqueGroupsSelected:
                        rows = self.model.transactionsDF[self.model.transactionsDF['Group']  == groupSelected[1]]
                        debitID = rows[rows['Debit'] >0]['Transaction ID'].item()
                        creditID = rows[rows['Credit'] >0]['Transaction ID'].item()
                        self.addDoubleLineEditRow(self.view.ui.verticalLayout_23, self.view.manualUnmatchLineEdits, debitID, creditID)
                    self.submitManualUnmatch()

    def matchTableCategoryChanged(self, row, column):
        if self.view.ui.matchTable.updateCategoryChanges == True and column == 11:
            item = self.view.ui.matchTable.item(row, column)
            refID = self.view.ui.matchTable.item(row, 0).text()
            if item is not None:
                index = self.model.transactionsDF.loc[self.model.transactionsDF['Transaction ID'] == refID].index[0]
                self.model.transactionsDF.at[index, 'Category'] = item.text()
                self.updateTransactionsCategorisedCountLabel(len([ t for t in self.model.transactionsDF['Category'].values.tolist() if str(t) != 'nan']))
                
    def searchMatches(self):
        queryDF = copy.deepcopy(self.model.transactionsDF)
        initialQuery = '''
                Select *
                from queryDF
        '''
        try:
            searchText = self.view.matchesSearchBar.searchEdit.text()
            if searchText == '':
                self.updateMatchTable(self.model.transactionsDF)
                return
            else:
                query = initialQuery + ' WHERE ' + searchText
                result = psql.sqldf(query, locals())

                self.updateMatchTable(result)
        except Exception as e:
            return


    def toggleMatchesSearch(self):
        if self.model.displayMatchesSearchBar == False:
            if self.view.matchesSearchBar is None:
                self.view.matchesSearchBar.df = self.model.transactionsDF
            self.view.ui.verticalLayout_8.insertWidget(1, self.view.matchesSearchBar)
            self.view.matchesSearchBar.show()
            self.model.displayMatchesSearchBar = True
        else:
            self.view.ui.verticalLayout_8.removeWidget(self.view.matchesSearchBar)
            self.view.matchesSearchBar.hide()
            self.model.displayMatchesSearchBar = False

    def uploadMatchesToDBBtn(self):
        return

    def exportMatchesToExcelBtn(self):
        if not os.path.exists('exports'):
            os.makedirs('exports')
        with pd.ExcelWriter('exports/Matches.xlsx', engine='openpyxl') as writer:
            self.model.transactionsDF.to_excel(writer, sheet_name='Matched Transactions')
            worksheet = writer.sheets['Matched Transactions']
            # Set column widths
            for i, width in enumerate([5.5, 21, 16, 12,12, 70, 15, 15,20, 21, 7, 7, 21]):
                col_letter = chr(65 + i)  # Convert number to letter (0 -> 'A', 1 -> 'B', etc.)
                worksheet.column_dimensions[col_letter].width = width   
            self.model.stampPossibleMatches.to_excel(writer, sheet_name='Possible Matches')
            if self.model.stampManualMatches is not None:
                self.model.stampManualMatches.to_excel(writer, sheet_name='Manual Matches')
            if self.model.stampManualUnmatch is not None:
                self.model.stampManualUnmatch.to_excel(writer, sheet_name='Manual Unmatch')
            if self.model.stampRefTable is not None:
                self.model.stampRefTable.to_excel(writer, sheet_name='Ref Table')
            if self.model.stampCategories is not None:
                self.model.stampCategories.to_excel(writer, sheet_name='Categories')
        return

    #endregion


if __name__ == "__main__":
    # Start the local HTTP server in a separate thread
    sys.setrecursionlimit(10000)
    serverThread = HTTPServerThread(port=8000)
    serverThread.start()
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(serverThread.stop)
    window = MainWindow(serverThread)
    model = Model()
    controller = Controller(model, window)
    window.show()
    result = app.exec_()
    serverThread.stop()
    serverThread.join(timeout=5)  # Add a timeout of 1 second
    sys.exit(result)

 
